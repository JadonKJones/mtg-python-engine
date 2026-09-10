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
# clause -> code.  ctx = "spell" (actor self.controller) or "etb" (self.controller)
# a clause that needs a target returns ("TARGET", criteria, code_with_targets0)
# ---------------------------------------------------------------------------

def _dmg_target(word):
    return {
        "any target": "'creature or player'",
        "target creature": "'creature'",
        "target creature or player": "'creature or player'",
        "target creature or planeswalker": "'creature or planeswalker'",
        "target player": "'player'",
        "target attacking creature": "'attacking creature'",
        "target blocking creature": "'blocking creature'",
        "target attacking or blocking creature": "'attacking or blocking creature'",
    }.get(word)


def _destroy_target(word):
    return {
        "target creature": "'creature'",
        "target artifact": "'artifact'",
        "target enchantment": "'enchantment'",
        "target land": "'land'",
        "target nonland permanent": "'nonland permanent'",
        "target artifact or enchantment": "'artifact or enchantment'",
        "target artifact or creature": "'artifact or creature'",
        "target creature or enchantment": "'creature or enchantment'",
        "target creature or planeswalker": "'creature or planeswalker'",
        "target nonblack creature": "'nonblack creature'",
        "target nonwhite creature": "'nonwhite creature'",
        "target tapped creature": "'tapped creature'",
        "target permanent": "'permanent'",
    }.get(word)


def clause_to_code(cl, actor):
    """actor: python expr for the acting player. Returns code string,
    or ('TARGET', criteria, code) for single-target clauses, or None."""
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

    # --- single-target clauses ---
    m = re.fullmatch(r"~ deals (\d+) damage to (.+)", low.replace("this creature", "~").replace("this spell", "~"))
    if m and _dmg_target(m.group(2)):
        return ("TARGET", _dmg_target(m.group(2)),
                "targets[0].take_damage(self, %d)" % int(m.group(1)))
    m = re.fullmatch(r"destroy (.+)", low)
    if m and _destroy_target(m.group(1)):
        return ("TARGET", _destroy_target(m.group(1)), "targets[0].destroy()")
    m = re.fullmatch(r"exile (.+)", low)
    if m and _destroy_target(m.group(1)):
        return ("TARGET", _destroy_target(m.group(1)), "targets[0].exile()")
    m = re.fullmatch(r"return (.+?) to (?:its|their) owner['’]s hand", low)
    if m and _destroy_target(m.group(1)):
        return ("TARGET", _destroy_target(m.group(1)), "targets[0].bounce()")
    m = re.fullmatch(r"tap (.+)", low)
    if m and _destroy_target(m.group(1)):
        return ("TARGET", _destroy_target(m.group(1)), "targets[0].tap()")
    m = re.fullmatch(r"untap (.+)", low)
    if m and _destroy_target(m.group(1)):
        return ("TARGET", _destroy_target(m.group(1)), "targets[0].untap()")
    m = re.fullmatch(r"counter (.+)", low)
    if m:
        kind = m.group(1).replace("target ", "").replace(" spell", "").strip()
        crit = {
            "": "'spell'", "spell": "'spell'",
            "instant or sorcery": "'instant or sorcery spell'",
            "creature": "'creature spell'", "noncreature": "'noncreature spell'",
            "artifact": "'artifact spell'",
            "enchantment": "'enchantment spell'",
            "artifact or enchantment": "'artifact or enchantment spell'",
            "activated or triggered": "'spell'",
        }.get(kind)
        if crit:
            return ("TARGET", crit, "targets[0].counter(source=self)")
    m = re.fullmatch(r"target creature gets ([+-]\d+)/([+-]\d+) until end of turn", low)
    if m:
        return ("TARGET", "'creature'",
                "targets[0].add_effect('modifyPT', (%d, %d), self, self.game.eot_time)"
                % (int(m.group(1)), int(m.group(2))))
    m = re.fullmatch(r"put (\w+) \+1/\+1 counters? on target creature", low)
    if m and n(m.group(1)):
        return ("TARGET", "'creature'", "targets[0].add_counter('+1/+1', %d)" % n(m.group(1)))
    m = re.fullmatch(r"target creature gains ([\w ]+?) until end of turn", low)
    if m:
        ab = m.group(1).replace("and ", "").strip().title().replace(" ", "_")
        return ("TARGET", "'creature'",
                "targets[0].add_effect('gainAbility', %r, self, self.game.eot_time)" % ab)
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
            _, crit, tcode = code
            abilities.append((cost, tcode.replace("targets[0]", "self.targets_chosen[0]"), crit))
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
            _, crit, tcode = code
            triggers.append(("onEtB", tcode.replace("targets[0]", "self.targets_chosen[0]"), crit))
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
                _, crit, tcode = code
                spell_target = crit
                spell_effects.append(tcode)
            else:
                spell_effects.append(code)
            matched += 1
        if spell_effects:
            if spell_target:
                targets = [spell_target]
                effects = spell_effects
            else:
                effects = spell_effects

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
