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


class Target:
    def __init__(self, criteria_func, min_targets=1, max_targets=1):
        self.criteria_func = criteria_func
        self.min_targets = min_targets
        self.max_targets = max_targets

    def __call__(self, source, target):
        return self.criteria_func(source, target)


def choose_targets(source):
    # TODO: ensure boolean/card return values of this func
    # is being parsed correctly.
    if source.target_criterias is None:
        return True

    # No valid targets
    if not source.has_valid_target():
        return False

    targets_chosen = []
    source.targets_chosen_criterias = []

    for criteria, prompt in zip(source.target_criterias, source.target_prompts):
        
        min_targets = getattr(criteria, 'min_targets', 1)
        max_targets = getattr(criteria, 'max_targets', 1)

        for i in range(max_targets if max_targets != float('inf') else 999):
            card = None
            try:
                while not card:
                    if max_targets > 1 or min_targets == 0:
                        ans_prompt = f"{prompt.strip()} (Target {i+1}/{max_targets}, leave blank if done)\n"
                    else:
                        ans_prompt = prompt

                    answer = source.controller.make_choice(ans_prompt)

                    if not answer.strip():
                        if i >= min_targets:
                            break
                        else:
                            print(f"You must choose at least {min_targets} target(s).")
                            continue

                    card = get_card_from_user_input(source.controller, answer)
                    if card is None: continue
                    if not criteria(source, card):
                        print("Invalid target.")
                        card = None

                if card is None:
                    break
            except:
                traceback.print_exc()
                return False

            targets_chosen.append(card)
            source.targets_chosen_criterias.append(criteria)

    return targets_chosen

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
    'creature card from your graveyard': lambda self, p: p.zone == self.controller.graveyard and p.is_creature,
    'creature card in your graveyard': lambda self, p: p.zone == self.controller.graveyard and p.is_creature,
    'card from your graveyard': lambda self, p: p.zone == self.controller.graveyard,
    'card in your graveyard': lambda self, p: p.zone == self.controller.graveyard,
    'card from a graveyard': lambda self, p: p.zone and p.zone.zone_type == 'GRAVEYARD',
    'card in a graveyard': lambda self, p: p.zone and p.zone.zone_type == 'GRAVEYARD',
    'artifact card from your graveyard': lambda self, p: p.zone == self.controller.graveyard and p.is_artifact,
    'artifact or creature card from your graveyard': lambda self, p: p.zone == self.controller.graveyard and (p.is_artifact or p.is_creature),
    'artifact or creature card in your graveyard': lambda self, p: p.zone == self.controller.graveyard and (p.is_artifact or p.is_creature),
    'artifact or enchantment card from your graveyard': lambda self, p: p.zone == self.controller.graveyard and (p.is_artifact or p.is_enchantment),
}

_WORD_NUM = {"one": 1, "two": 2, "three": 3, "four": 4,
             "five": 5, "six": 6, "seven": 7, "eight": 8, "ten": 10}

def parse_targets(criterias):
    import math
    for i, v in enumerate(criterias):
        if isinstance(v, str):
            min_t = 1
            max_t = 1
            original_v = v

            if v.startswith("up to "):
                v = v[6:]
                min_t = 0
                for word, num in _WORD_NUM.items():
                    if v.startswith(word + " "):
                        max_t = num
                        v = v[len(word)+1:]
                        break
            elif v.startswith("any number of "):
                v = v[14:]
                min_t = 0
                max_t = math.inf

            if v.startswith("target "):
                v = v[7:]

            if v in _TARGET_SHORTCUTS:
                criterias[i] = Target(_TARGET_SHORTCUTS[v], min_t, max_t)
            elif original_v in _TARGET_SHORTCUTS:
                criterias[i] = Target(_TARGET_SHORTCUTS[original_v], min_t, max_t)
            else:
                # If we cannot find it, leave it as is or wrap it in Target if it's somehow evaluable
                pass
        elif callable(v) and not isinstance(v, Target):
            criterias[i] = Target(v)

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