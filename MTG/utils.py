import math
import traceback
import re

# any length > 0 of the following: { X, numbers, hybrid e.g. (U/R), WUBRGC }
mana_pattern = re.compile(
    '(X|' '\d|' '(\([WUBRGC2]/[WUBRGC]\))|' '[WUBRGC])+')

def get_card_from_user_input(player, string):
    """Convert a user input (naming a card in a zone) to an actual game object

    b 2 --> 2nd(3rd) card on battlefield
    b Grizzly Bear --> Grizzly Bear on battlefield

    s 0 --> 1st card on stack (from top)

    h -1 --> last card in hand

    og 3 --> 3rd(4th) card on opponent's graveyard
    """
    if not string:
        return None

    if string[0] == 'o':  # opponent; continue parsing rest of string
        string = string[1:]
        player = player.game.opponent(player)

    if string[0] == 'p':
        return player

    if string[0] == 'b':
        zone = player.battlefield
    elif string[0] == 's':
        zone = player.game.stack
    elif string[0] == 'h':
        zone = player.hand
    elif string[0] == 'g':
        zone = player.graveyard
    else:
        return None

    try:
        i = int(string[2:])
        if i < len(zone):
            return zone[i]
        else:
            return None
    except ValueError:
        return zone.get_card_by_name(string[2:])


class TargetSpec:
    """One "target ..." clause on a spell or ability.

    ``criteria(source, obj) -> bool`` decides whether ``obj`` is a legal target.
    ``min``/``max`` are the number of targets this clause wants (1/1 by default;
    ``max`` may be ``math.inf`` for "any number of"). ``distinct`` forbids
    choosing the same object twice for this clause.

    A bare criteria function is still accepted everywhere a spec is (it behaves
    as exactly one target), so pre-existing cards keep working unchanged.
    """

    def __init__(self, criteria, min=1, max=1, prompt=None, distinct=True):
        self.criteria = criteria
        self.min = min
        self.max = max
        self.prompt = prompt
        self.distinct = distinct

    def __call__(self, source, obj):
        # so legacy code that treats a spec as `crit(src, obj)` still works
        return bool(self.criteria(source, obj))

    def __repr__(self):
        rng = "%s" % self.min if self.min == self.max else "%s-%s" % (
            self.min, "inf" if self.max == math.inf else self.max)
        return "TargetSpec(%s targets)" % rng


def as_target_spec(v):
    if isinstance(v, TargetSpec):
        return v
    if isinstance(v, str):
        return _string_to_spec(v)
    if callable(v):
        return TargetSpec(v)
    raise TypeError("target criteria must be a TargetSpec, str, or callable: %r" % v)


def _all_targetable_objects(game):
    """Every object a spell/ability could legally target: permanents on every
    battlefield, cards in every graveyard/exile, objects on the stack, and the
    players themselves."""
    objs = []
    for p in game.players_list:
        objs.append(p)
        for z in (p.battlefield, p.graveyard, p.exile):
            objs.extend(list(z))
    objs.extend(list(game.stack))
    return objs


def _legal_targets_for(source, spec, pool):
    out = []
    for o in pool:
        try:
            if spec.criteria(source, o):
                out.append(o)
        except Exception:
            pass
    return out


def choose_targets(source):
    """Interactively choose targets for ``source`` (a spell or ability).

    Returns
      * ``True``                -- the source has no target clauses
      * a flat ``list`` of chosen objects (possibly empty for all-optional)
      * ``False``               -- targeting is impossible (not enough legal
                                   targets for a mandatory clause); the caller
                                   must treat the spell/ability as uncastable

    Also records ``source._target_bindings`` -- a list of ``(spec, obj)`` pairs
    -- so resolution can re-check each target against the clause that chose it.
    """
    specs = source.target_criterias
    if specs is None:
        source._target_bindings = []
        return True

    specs = [as_target_spec(s) for s in specs]
    game = source.controller.game
    pool = _all_targetable_objects(game)

    prompts = source.target_prompts or []
    chosen, bindings = [], []

    for i, spec in enumerate(specs):
        legal = _legal_targets_for(source, spec, pool)
        if len(legal) < spec.min:
            print("%r: only %d legal target(s), needs %d." % (source, len(legal), spec.min))
            return False

        base_prompt = (spec.prompt
                       or (prompts[i] if i < len(prompts) else None)
                       or "Choose target(s)\n").rstrip()
        cap = spec.max if spec.max != math.inf else len(legal)
        picked = []

        while len(picked) < cap:
            need_more = len(picked) < spec.min
            p = base_prompt
            if spec.min != spec.max:
                tail = "" if need_more else ", or blank when done"
                p = "%s  [%d/%d%s]" % (base_prompt, len(picked), cap, tail)
            try:
                ans = source.controller.make_choice(p + "\n")
            except Exception:
                traceback.print_exc()
                return False

            if not str(ans).strip():
                if need_more:
                    print("Must choose at least %d." % spec.min)
                    continue
                break

            obj = get_card_from_user_input(source.controller, str(ans).strip())
            if obj is None:
                print("No such object.")
                continue
            if spec.distinct and obj in picked:
                print("Already chosen for this clause.")
                continue
            try:
                ok = spec.criteria(source, obj)
            except Exception:
                ok = False
            if not ok:
                print("Illegal target.")
                continue
            picked.append(obj)

        chosen.extend(picked)
        bindings.extend((spec, o) for o in picked)

    source._target_bindings = bindings
    return chosen


# --- string target grammar -------------------------------------------------

_NUMWORD = {"a": 1, "an": 1, "one": 1, "two": 2, "three": 3, "four": 4,
            "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}


def _string_to_spec(v):
    """Parse "up to two target creatures", "any number of target lands",
    "three target creatures", "target creature", "creature" -> TargetSpec."""
    s = v.strip().lower()
    min_t, max_t = 1, 1

    m = re.match(r"up to (\w+) (.*)", s)
    if m and m.group(1) in _NUMWORD:
        min_t, max_t, s = 0, _NUMWORD[m.group(1)], m.group(2)
    elif s.startswith("up to "):
        min_t, max_t, s = 0, 1, s[len("up to "):]
    elif s.startswith("any number of "):
        min_t, max_t, s = 0, math.inf, s[len("any number of "):]
    else:
        m = re.match(r"(\w+) (.*)", s)
        if m and m.group(1) in _NUMWORD and _NUMWORD[m.group(1)] > 1:
            min_t = max_t = _NUMWORD[m.group(1)]
            s = m.group(2)

    if s.startswith("target "):
        s = s[len("target "):]
    s = s.strip()

    crit = _TARGET_SHORTCUTS.get(s)
    if crit is None and s.endswith("s"):            # "creatures" -> "creature"
        crit = _TARGET_SHORTCUTS.get(s[:-1])
    if crit is None:
        raise KeyError("unknown target shortcut: %r (from %r)" % (s, v))

    return TargetSpec(crit, min=min_t, max=max_t)

_TARGET_SHORTCUTS = {
    'creature': lambda self, p: p.is_permanent and p.is_creature,
    'your creature': lambda self, p: p.is_permanent and p.is_creature and p.controller == self.controller,
    'other creature': lambda self, p: p.is_permanent and p.is_creature and p != self,
    'your other creature': lambda self, p: (p.is_permanent and p.is_creature
                                            and p.controller == self.controller and p != self),
    'opponent creature': lambda self, p: p.is_creature and p.controller != self.controller,
    'opponent': lambda self, p: p.is_player and p != self.controller,
    'player': lambda self, p: p.is_player,
    'creature or player': lambda self, p: p.is_player or (p.is_creature and p.is_permanent),
    'any target': lambda self, p: p.is_player or (p.is_creature and p.is_permanent),
    'spell': lambda self, s: s.is_spell,
    'instant or sorcery spell': lambda self, s: s.is_spell and (s.is_instant or s.is_sorcery),
    'creature spell': lambda self, s: s.is_spell and s.is_creature,
    'noncreature spell': lambda self, s: s.is_spell and not s.is_creature,
    'artifact spell': lambda self, s: s.is_spell and s.is_artifact,
    'enchantment spell': lambda self, s: s.is_spell and s.is_enchantment,
    'artifact or enchantment spell': lambda self, s: s.is_spell and (s.is_artifact or s.is_enchantment),
    # permanents by type -- auto-generated collection cards lean on these
    'permanent': lambda self, p: p.is_permanent,
    'artifact': lambda self, p: p.is_permanent and p.is_artifact,
    'enchantment': lambda self, p: p.is_permanent and p.is_enchantment,
    'land': lambda self, p: p.is_permanent and p.is_land,
    'nonland permanent': lambda self, p: p.is_permanent and not p.is_land,
    'planeswalker': lambda self, p: p.is_permanent and p.is_planeswalker,
    'artifact or enchantment': lambda self, p: p.is_permanent and (p.is_artifact or p.is_enchantment),
    'artifact or creature': lambda self, p: p.is_permanent and (p.is_artifact or p.is_creature),
    'creature or planeswalker': lambda self, p: p.is_permanent and (p.is_creature or p.is_planeswalker),
    'creature or enchantment': lambda self, p: p.is_permanent and (p.is_creature or p.is_enchantment),
    'nonblack creature': lambda self, p: p.is_permanent and p.is_creature and not p.has_color('B'),
    'nonwhite creature': lambda self, p: p.is_permanent and p.is_creature and not p.has_color('W'),
    'attacking creature': lambda self, p: p.is_creature and p.status.is_attacking,
    'blocking creature': lambda self, p: p.is_creature and p.status.is_blocking,
    'attacking or blocking creature': lambda self, p: p.is_creature and (p.status.is_attacking or p.status.is_blocking),
    'tapped creature': lambda self, p: p.is_creature and p.status.tapped,
    # cards in graveyards (utils._all_targetable_objects surfaces these)
    'card in your graveyard': lambda self, p: getattr(p, 'zone', None) is self.controller.graveyard,
    'creature card in your graveyard': lambda self, p: getattr(p, 'zone', None) is self.controller.graveyard and p.is_creature,
    'artifact card in your graveyard': lambda self, p: getattr(p, 'zone', None) is self.controller.graveyard and p.is_artifact,
    'instant or sorcery card in your graveyard': lambda self, p: getattr(p, 'zone', None) is self.controller.graveyard and (p.is_instant or p.is_sorcery),
    'card in a graveyard': lambda self, p: getattr(getattr(p, 'zone', None), 'zone_type', None) == 'GRAVEYARD',
}


def parse_targets(criterias):
    """Normalise a card's raw target-criteria list into TargetSpec objects.

    Accepts, per entry: a shortcut string ("creature", "up to two target
    creatures", ...), a bare ``lambda self, obj: ...`` (exactly one target), or
    an already-built TargetSpec. Unknown strings are left untouched so an
    obvious mistake surfaces loudly at first use rather than silently.
    """
    for i, v in enumerate(criterias):
        try:
            criterias[i] = as_target_spec(v)
        except (KeyError, TypeError):
            pass
    return criterias

def parse_ability_costs(cost):
    _costs = cost.split(', ')
    costs = []

    if 'T' in _costs:
        costs.append("self.tap() and not self.is_summoning_sick")

    for itm in _costs:
        if mana_pattern.match(itm):
            costs.append("self.controller.pay('%s')" % itm)

        if re.match('[pP]ay [\dX]+ life', itm):
            costs.append("self.controller.pay(life=%s)" %
                         re.search('[\dX]+', itm).group(0))

        if itm == 'Sacrifice ~':
            costs.append("self.sacrifice()")

    # elif other costs

    costs = " and ".join(costs)
    return costs