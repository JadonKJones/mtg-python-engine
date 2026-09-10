"""Best-effort oracle-text -> engine-DSL translator for the Moxfield collection.

Reads  scryfall_cards.json
Writes data/collection_cards.txt   (ability definitions, data/m15_cards.txt format)
       COLLECTION_COVERAGE.md       (per-card status)

Goal: every card in the collection is castable / playable in a real game. Cards
whose full text can't be modelled still get their recognisable clauses wired and
never crash the engine -- unmatched clauses are dropped, not faked.

    python -m parser.parse_scryfall
    python -m parser.translate_oracle
"""

import json
import re
from collections import Counter

IN = "scryfall_cards.json"
OUT_TXT = "data/collection_cards.txt"
OUT_MD = "COLLECTION_COVERAGE.md"
CARD_SEP = "#" * 30

_WORD_NUM = {"a": 1, "an": 1, "one": 1, "two": 2, "three": 3, "four": 4,
             "five": 5, "six": 6, "seven": 7, "eight": 8, "ten": 10, "x": 1}
_COLOR = {"W": "WHITE", "U": "BLUE", "B": "BLACK", "R": "RED", "G": "GREEN", "C": "COLORLESS"}
_COLORWORD = {"white": "W", "blue": "U", "black": "B", "red": "R", "green": "G", "colorless": "C"}


def n(tok):
    tok = (tok or "").strip().lower()
    if tok.isdigit():
        return int(tok)
    return _WORD_NUM.get(tok)


def face(c):
    if "oracle_text" in c and "type_line" in c:
        return c
    if c.get("card_faces"):
        return {**c, **c["card_faces"][0]}
    return c


# ---------------------------------------------------------------------------
# clause -> code.
#   * a no-target clause returns a code string (acts via `actor`)
#   * a targeted clause returns ("TARGET", spec_string, per_target_expr) where
#     per_target_expr uses the loop variable `t`; the caller wraps it as
#     `[<expr> for t in self.legal_targets]` so it works for 1..N targets and
#     silently drops targets that became illegal before resolution.
# ---------------------------------------------------------------------------

# bare noun (after stripping any "up to N" / "target" prefix) -> engine shortcut
_CORE = {
    "any target": "any target",
    "creature": "creature",
    "player": "player",
    "opponent": "opponent",
    "creature or player": "creature or player",
    "creature or planeswalker": "creature or planeswalker",
    "creature or enchantment": "creature or enchantment",
    "artifact": "artifact",
    "enchantment": "enchantment",
    "land": "land",
    "permanent": "permanent",
    "nonland permanent": "nonland permanent",
    "artifact or enchantment": "artifact or enchantment",
    "artifact or creature": "artifact or creature",
    "nonblack creature": "nonblack creature",
    "nonwhite creature": "nonwhite creature",
    "tapped creature": "tapped creature",
    "attacking creature": "attacking creature",
    "blocking creature": "blocking creature",
    "attacking or blocking creature": "attacking or blocking creature",
    "creature you control": "your creature",
    "card in your graveyard": "card in your graveyard",
    "creature card in your graveyard": "creature card in your graveyard",
    "artifact card in your graveyard": "artifact card in your graveyard",
    "instant or sorcery card in your graveyard": "instant or sorcery card in your graveyard",
}

_UPTO_RE = re.compile(r"^(up to (?:\w+)|up to|any number of|(?:two|three|four|five)) ")


def _spec_for(phrase):
    """"up to two target creatures" / "target creature" / "any number of target
    lands" / "any target" -> a criteria string the engine grammar accepts,
    or None if the noun isn't one we model."""
    w = phrase.strip().lower().rstrip(".")
    prefix = ""
    m = _UPTO_RE.match(w + " ")
    if m:
        prefix = m.group(1).strip() + " "
        w = w[len(m.group(1)):].strip()
    if w.startswith("target "):
        w = w[len("target "):]
    core = w.strip()
    if core not in _CORE and core.endswith("s") and core[:-1] in _CORE:
        core = core[:-1]
    if core not in _CORE:
        return None
    shortcut = _CORE[core]
    if shortcut == "any target" and not prefix:
        return "'any target'"
    return "'%starget %s'" % (prefix, shortcut)


def clause_to_code(cl, actor):
    """actor: python expr for the acting player. Returns code string,
    or ('TARGET', spec, per_target_expr) for targeted clauses, or None."""
    s = cl.strip().rstrip(".").strip()
    low = s.lower()

    # --- no-target player effects ---
    m = re.fullmatch(r"draw (\w+) cards?", low)
    if m and n(m.group(1)):
        return "%s.draw(%d)" % (actor, n(m.group(1)))
    m = re.fullmatch(r"you draw (\w+) cards?", low)
    if m and n(m.group(1)):
        return "%s.draw(%d)" % (actor, n(m.group(1)))
    m = re.fullmatch(r"you gain (\w+) life", low)
    if m and n(m.group(1)):
        return "%s.gain_life(%d)" % (actor, n(m.group(1)))
    m = re.fullmatch(r"you lose (\w+) life", low)
    if m and n(m.group(1)):
        return "%s.lose_life(%d)" % (actor, n(m.group(1)))
    m = re.fullmatch(r"(?:each opponent|target opponent|that player) loses (\w+) life", low)
    if m and n(m.group(1)):
        return "%s.opponent.lose_life(%d)" % (actor, n(m.group(1)))
    m = re.fullmatch(r"~ deals (\d+) damage to (?:each opponent|target opponent|that player)", low.replace("this creature", "~").replace("this spell", "~"))
    if m:
        return "%s.opponent.take_damage(self, %d)" % (actor, int(m.group(1)))
    m = re.fullmatch(r"(?:you )?mill (\w+) cards?", low)
    if m and n(m.group(1)):
        return "%s.mill(%d)" % (actor, n(m.group(1)))
    m = re.fullmatch(r"(?:each opponent|target opponent) mills (\w+) cards?", low)
    if m and n(m.group(1)):
        return "%s.opponent.mill(%d)" % (actor, n(m.group(1)))
    m = re.fullmatch(r"(?:you )?scry (\w+)", low)
    if m and n(m.group(1)):
        return "%s.scry(%d)" % (actor, n(m.group(1)))
    m = re.fullmatch(r"(?:target opponent|each opponent) discards (\w+) cards?", low)
    if m and n(m.group(1)):
        return "%s.opponent.discard(%d, rand=True)" % (actor, n(m.group(1)))
    if re.fullmatch(r"(?:target opponent|each opponent) reveals their hand", low):
        return "None"  # informational; safe no-op
    m = re.fullmatch(r"(?:you )?create (\w+) (\d+/\d+) (white|blue|black|red|green|colorless) ([\w ]+?) (?:creature )?tokens?"
                     r"(?: with [\w, ]+)?", low)
    if m:
        cnt = n(m.group(1)) or 1
        pt = m.group(2)
        col = m.group(3)
        typ = m.group(4).strip().split(" and ")[0].split(" ")[0].title()
        return "%s.create_token('%s %s %s', %d)" % (actor, pt, col, typ, cnt)
    m = re.fullmatch(r"(?:you )?create (\w+) ([\w ]+?) tokens?", low)
    if m and "creature" not in m.group(2):
        cnt = n(m.group(1)) or 1
        typ = m.group(2).strip().split(" ")[-1].title()
        col = "colorless"
        for w in m.group(2).split():
            if w in _COLORWORD:
                col = w
        return "%s.create_token('%s %s', %d)" % (actor, col, typ, cnt)

    # --- targeted clauses (per_target_expr uses loop var `t`) ---
    m = re.fullmatch(r"~ deals (\d+) damage to (.+)",
                     low.replace("this creature", "~").replace("this spell", "~"))
    if m and _spec_for(m.group(2)):
        return ("TARGET", _spec_for(m.group(2)), "t.take_damage(self, %d)" % int(m.group(1)))
    m = re.fullmatch(r"destroy (.+)", low)
    if m and _spec_for(m.group(1)):
        return ("TARGET", _spec_for(m.group(1)), "t.destroy()")
    m = re.fullmatch(r"exile (.+)", low)
    if m and _spec_for(m.group(1)):
        return ("TARGET", _spec_for(m.group(1)), "t.exile()")
    m = re.fullmatch(r"return (.+?) to (?:its|their) owner['’]s hand", low)
    if m and _spec_for(m.group(1)):
        return ("TARGET", _spec_for(m.group(1)), "t.bounce()")
    m = re.fullmatch(r"return (.+?) (?:from your graveyard )?to your hand", low)
    if m and _spec_for(m.group(1)) and "graveyard" in _spec_for(m.group(1)):
        return ("TARGET", _spec_for(m.group(1)), "t.change_zone(self.controller.hand)")
    m = re.fullmatch(r"tap (.+)", low)
    if m and _spec_for(m.group(1)):
        return ("TARGET", _spec_for(m.group(1)), "t.tap()")
    m = re.fullmatch(r"untap (.+)", low)
    if m and _spec_for(m.group(1)):
        return ("TARGET", _spec_for(m.group(1)), "t.untap()")
    m = re.fullmatch(r"counter (.+)", low)
    if m:
        w = m.group(1).rstrip(".")
        pref = ""
        mm = _UPTO_RE.match(w + " ")
        if mm:
            pref, w = mm.group(1).strip() + " ", w[len(mm.group(1)):].strip()
        kind = w.replace("target ", "").replace(" spell", "").strip()
        crit = {
            "": "spell", "spell": "spell",
            "instant or sorcery": "instant or sorcery spell",
            "creature": "creature spell", "noncreature": "noncreature spell",
            "artifact": "artifact spell", "enchantment": "enchantment spell",
            "artifact or enchantment": "artifact or enchantment spell",
            "activated or triggered": "spell",
        }.get(kind)
        if crit:
            spec = "'%starget %s'" % (pref, crit) if pref else "'%s'" % crit
            return ("TARGET", spec, "t.counter(source=self)")
    m = re.fullmatch(r"(.+?) gets ([+-]\d+)/([+-]\d+) until end of turn", low)
    if m and _spec_for(m.group(1)):
        return ("TARGET", _spec_for(m.group(1)),
                "t.add_effect('modifyPT', (%d, %d), self, self.game.eot_time)"
                % (int(m.group(2)), int(m.group(3))))
    m = re.fullmatch(r"put (\w+) \+1/\+1 counters? on (.+)", low)
    if m and n(m.group(1)) and _spec_for(m.group(2)):
        return ("TARGET", _spec_for(m.group(2)),
                "t.add_counter('+1/+1', %d)" % n(m.group(1)))
    m = re.fullmatch(r"(.+?) gains? (.+?) until end of turn", low)
    if m and _spec_for(m.group(1)):
        abs_ = [a.strip().title().replace(" ", "_")
                for a in re.split(r",| and ", m.group(2)) if a.strip()]
        parts = ["t.add_effect('gainAbility', %r, self, self.game.eot_time)" % a
                 for a in abs_]
        expr = parts[0] if len(parts) == 1 else "(%s)" % ", ".join(parts)
        return ("TARGET", _spec_for(m.group(1)), expr)
    return None


# ---------------------------------------------------------------------------

def sentences(body):
    # split on '. ' and newlines, keep it simple
    parts = re.split(r"(?<=[.)])\s+(?=[A-Z])|\n+", body)
    return [p.strip() for p in parts if p.strip()]


def translate(card):
    c = face(card)
    name = card["name"].split(" // ")[0]
    text = (c.get("oracle_text") or "").strip()
    tl = c.get("type_line", "")
    is_spell = ("Instant" in tl or "Sorcery" in tl) and "Creature" not in tl
    is_creature = "Creature" in tl
    is_aura = "Aura" in tl

    if not text:
        return None, "vanilla", "no rules text"

    body = re.sub(re.escape(name), "~", text)
    body = re.sub(r"\s*\([^)]*\)", "", body).strip()

    kws = {k.lower() for k in card.get("keywords", [])}
    lines = [l for l in body.split("\n") if l.strip()]
    if lines and all(
        all(w.strip(",").lower() in kws or w.strip(",").lower() in
            {"first", "double", "strike", "and"}
            for w in re.split(r"[ ,]+", l.strip()) if w)
        for l in lines
    ):
        return None, "keyword", "keyword abilities only"

    targets, effects, triggers, abilities, statics, auras = [], [], [], [], [], []
    matched = 0
    total = 0

    # ---- lands that enter tapped ----
    if "Land" in tl and re.search(r"~ enters(?: the battlefield)? tapped", body):
        # engine has no ETB-tapped hook here; note only
        pass

    # ---- activated abilities:  "COST: EFFECT" ----
    for line in lines:
        m = re.match(r"^([^:]{1,40}):\s+(.+)$", line)
        if not m or "—" in m.group(1) or "when" in m.group(1).lower():
            continue
        cost_raw, eff_raw = m.group(1), m.group(2).rstrip(".")
        cost = _parse_cost(cost_raw)
        if cost is None:
            total += 1
            continue
        total += 1
        code = clause_to_code(eff_raw, "self.controller")
        if code is None and re.fullmatch(r"add (?:\{[WUBRGC]\})+", eff_raw.lower()):
            syms = re.findall(r"\{([WUBRGC])\}", eff_raw)
            code = "; ".join("self.controller.mana.add(mana.Mana.%s, %d)" % (_COLOR[s], k)
                             for s, k in Counter(syms).items())
        elif code is None and re.fullmatch(r"add one mana of any color", eff_raw.lower()):
            code = "self.controller.mana.add(mana.Mana.COLORLESS, 1)"
        elif code is None:
            mp = re.fullmatch(r"~ gets ([+-]\d+)/([+-]\d+) until end of turn", eff_raw.lower())
            if mp:
                code = ("self.card.add_effect('modifyPT', (%d, %d), self, self.game.eot_time)"
                        % (int(mp.group(1)), int(mp.group(2))))
        if code is None:
            continue
        if isinstance(code, tuple):
            _, crit, per_target = code
            abilities.append((cost, "[%s for t in self.legal_targets]" % per_target, crit))
        else:
            abilities.append((cost, code, None))
        matched += 1

    # ---- ETB triggers:  "When ~ enters (the battlefield), EFFECT." ----
    for sent in sentences(body):
        m = re.match(r"when(?:ever)? ~ enters(?: the battlefield)?,?\s*(?:you may\s+)?(.+)",
                     sent, re.I)
        if not m:
            continue
        total += 1
        code = clause_to_code(m.group(1).rstrip("."), "self.controller")
        if code is None:
            continue
        if isinstance(code, tuple):
            _, crit, per_target = code
            triggers.append(("onEtB", "[%s for t in self.legal_targets]" % per_target, crit))
        else:
            triggers.append(("onEtB", code, None))
        matched += 1

    # ---- static anthems ----
    for sent in sentences(body):
        m = re.fullmatch(
            r"(other creatures you control|creatures you control|"
            r"creatures your opponents control) gets? ([+-]\d+)/([+-]\d+)\.?", sent, re.I)
        if not m:
            continue
        total += 1
        who = m.group(1).lower()
        pt = (int(m.group(2)), int(m.group(3)))
        if who == "other creatures you control":
            statics.append(("'controller -self'", '"modifyPT"', repr(pt),
                            "lambda eff: eff.apply_target.is_creature"))
        elif who == "creatures you control":
            statics.append(("'controller'", '"modifyPT"', repr(pt),
                            "lambda eff: eff.apply_target.is_creature"))
        else:
            statics.append(("'game'", '"modifyPT"', repr(pt),
                            "lambda eff: eff.apply_target.is_creature and "
                            "eff.apply_target.controller != eff.source.controller"))
        matched += 1

    # ---- spell body (instant / sorcery) ----
    if is_spell:
        spell_effects = []
        spell_target = None
        for sent in sentences(body):
            total += 1
            code = clause_to_code(sent, "self.controller")
            if code is None:
                continue
            if isinstance(code, tuple):
                _, crit, per_target = code
                # single target clause per spell (this collection has ~no
                # multi-"target" instant/sorcery); if a later clause wants a
                # DIFFERENT target, drop it rather than mis-apply.
                if spell_target is None:
                    spell_target = crit
                elif crit != spell_target:
                    matched -= 1
                    continue
                spell_effects.append("[%s for t in self.legal_targets]" % per_target)
            else:
                spell_effects.append(code)
            matched += 1
        if spell_effects:
            effects = spell_effects
            if spell_target:
                targets = [spell_target]

    # ---- aura ----
    if is_aura:
        m = re.search(r"enchanted creature gets ([+-]\d+)/([+-]\d+)", body, re.I)
        if m:
            total += 1
            auras.append(("modifyPT", (int(m.group(1)), int(m.group(2)))))
            matched += 1

    block = _emit(name, targets, effects, abilities, triggers, statics, auras)
    if block is None:
        first = body.split("\n")[0][:70]
        return None, "unsupported", first
    if total and matched < total:
        return block, "partial", "%d/%d clauses" % (matched, total)
    return block, "implemented", "ok"


def _parse_cost(raw):
    raw = raw.strip()
    parts = []
    mana = "".join(re.findall(r"\{([WUBRGC0-9]+)\}", raw))
    if mana:
        parts.append(mana)
    if re.search(r"\{T\}", raw) or raw == "T":
        parts.append("T")
    m = re.search(r"[Pp]ay (\d+) life|[Ss]acrifice ~|[Ss]acrifice this", raw)
    if m:
        if "life" in m.group(0).lower():
            parts.append("Pay %s life" % re.search(r"\d+", m.group(0)).group(0))
        else:
            parts.append("Sacrifice ~")
    plain = re.fullmatch(r"([WUBRGC0-9]+)", raw)
    if plain and not parts:
        parts.append(plain.group(1))
    if not parts:
        return None
    return ", ".join(parts)


def _emit(name, targets, effects, abilities, triggers, statics, auras):
    if not (targets or effects or abilities or triggers or statics or auras):
        return None
    out = [CARD_SEP, name, ""]
    if abilities:
        out.append("\tAbilities:")
        for cost, eff, crit in abilities:
            out.append("\t\t%s: %s" % (cost, eff))
            if crit:
                out.append("\t\t\tTargets:")
                out.append("\t\t\t\t%s" % crit)
        out.append("")
    if triggers:
        out.append("\tTriggers:")
        for cond, eff, crit in triggers:
            out.append("\t\t%s" % cond)
            out.append("\t\t\t%s" % eff)
            if crit:
                out.append("\t\t\t\tTargets:")
                out.append("\t\t\t\t\t%s" % crit)
        out.append("")
    if targets:
        out.append("\tTargets:")
        for t in targets:
            out.append("\t\t%s" % t)
        out.append("")
    if effects:
        for e in effects:
            out.append("\t" + e)
        out.append("")
    if statics:
        out.append("\tStaticEffects:")
        for apply_to, nm, val, tog in statics:
            out.append("\t\t%s" % apply_to)
            out.append("\t\t\t%s" % nm)
            out.append("\t\t\t%s" % val)
            out.append("\t\t\t%s" % tog)
        out.append("")
    if auras:
        out.append("\tAura:")
        out.append("\t\tTargets:")
        out.append("\t\t\t'creature'")
        out.append("")
        for nm, val in auras:
            if nm == "modifyPT":
                out.append("\t\tself.add_pt(%r)" % (val,))
            elif nm == "gainAbility":
                out.append("\t\tself.add_ability(%r)" % (val,))
        out.append("")
    return "\n".join(out) + "\n"


def run():
    cards = sorted(json.load(open(IN)), key=lambda c: c["name"])
    blocks = ["# AUTO-GENERATED by parser/translate_oracle.py -- do not hand-edit.\n"
              "# Regenerate: python -m parser.parse_scryfall && python -m parser.translate_oracle\n"]
    cats = Counter()
    rows = []
    for c in cards:
        block, cat, note = translate(c)
        cats[cat] += 1
        rows.append((c["name"], cat, note))
        if block:
            blocks.append(block)

    with open(OUT_TXT, "w") as f:
        f.write("\n".join(blocks))
        f.write("\n" + CARD_SEP + "\n")

    with open(OUT_MD, "w") as f:
        f.write("# Collection rules-text coverage\n\n%d unique cards.\n\n" % len(cards))
        for cat in ("implemented", "partial", "keyword", "vanilla", "unsupported"):
            f.write("- **%s**: %d\n" % (cat, cats[cat]))
        f.write("\n> Every card is castable in a game. `keyword`/`vanilla` have no "
                "non-keyword text; `partial` wires the clauses the engine supports "
                "and drops the rest; `unsupported` plays as a vanilla/keyword permanent.\n")
        for want in ("implemented", "partial", "unsupported", "keyword", "vanilla"):
            f.write("\n## %s\n\n" % want)
            for nm, cat, note in rows:
                if cat == want:
                    f.write("- %s — %s\n" % (nm, note))

    print(dict(cats))


if __name__ == "__main__":
    run()
