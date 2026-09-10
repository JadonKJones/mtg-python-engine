"""Generate engine card classes from a Scryfall dump.

Input:  scryfall_cards.json  -- a JSON list of Scryfall card objects
        (produced by fetching /cards/collection for a Moxfield collection).
Output: data/collection_cards.py           -- one card.Card subclass per card
        data/collection_name_to_id_dict.pkl -- {card name: class id}

Run:  python -m parser.parse_scryfall
Then the cards are available to the engine via MTG.parsedcards / MTG.cards
(the 'collection' prefix is registered in both).
"""

import json
import pickle
import re

from MTG import static_abilities

INFILE = "scryfall_cards.json"
NAME = "collection"

# Scryfall keyword string -> StaticAbilities member name
_KEYWORD_MEMBERS = set(static_abilities.StaticAbilities._member_names_)


def _ability_member(keyword):
    m = keyword.strip().replace(" ", "_").replace("-", "_")
    # normalise case to the enum's (First_Strike, Double_Strike, ...)
    for member in _KEYWORD_MEMBERS:
        if member.lower() == m.lower():
            return member
    return None


_TYPE_MAP = {
    "Artifact": "ARTIFACT",
    "Creature": "CREATURE",
    "Enchantment": "ENCHANTMENT",
    "Instant": "INSTANT",
    "Land": "LAND",
    "Planeswalker": "PLANESWALKER",
    "Sorcery": "SORCERY",
    "Tribal": "TRIBAL",
}
_SUPER_MAP = {"Basic": "BASIC", "Legendary": "LEGENDARY", "Snow": "SNOW", "World": "WORLD"}


def star_or_int(c):
    if c is None:
        return None
    c = str(c)
    if c in ("*", "1+*", "*+1", "X"):
        return "*"
    try:
        return int(c)
    except ValueError:
        return "*"


def _face(card):
    """Return the dict of characteristics to use (front face for MDFC/split)."""
    if "type_line" in card and "mana_cost" in card:
        return card
    faces = card.get("card_faces")
    if faces:
        return {**card, **faces[0]}
    return card


def _split_type_line(type_line):
    type_line = type_line.split("//")[0].strip()
    if "—" in type_line:
        left, right = type_line.split("—", 1)
        subtypes = right.split()
    else:
        left, subtypes = type_line, []
    words = left.split()
    supertypes = [_SUPER_MAP[w] for w in words if w in _SUPER_MAP]
    types = [_TYPE_MAP[w] for w in words if w in _TYPE_MAP]
    return supertypes, types, subtypes


def _class_id(card):
    mv = card.get("multiverse_ids") or []
    if mv:
        return "c" + str(mv[0])
    # deterministic fallback from the oracle id
    digits = re.sub(r"\D", "", card.get("oracle_id", card.get("id", "")))
    return "c9" + (digits[:9] or "0")


def run():
    with open(INFILE) as f:
        cards = json.load(f)

    seen_names = {}
    seen_ids = set()
    name_to_id = {}

    out = [
        "from MTG import card\n",
        "from MTG import gameobject\n",
        "from MTG import cardtype\n",
        "from MTG import static_abilities\n",
        "from MTG import mana\n\n",
    ]

    for raw in cards:
        full_name = raw["name"]
        name = full_name.split(" // ")[0]
        if full_name in seen_names:
            continue
        seen_names[full_name] = True

        c = _face(raw)
        ID = _class_id(raw)
        while ID in seen_ids:
            ID += "b"
        seen_ids.add(ID)

        supertypes, types, subtypes = _split_type_line(c.get("type_line", ""))
        if not types:
            types = ["ARTIFACT"]  # last-resort so the class is still constructible

        ch = {
            "name": name,
            "text": c.get("oracle_text", "") or "",
            "color": raw.get("color_identity", []) or [],
            "mana_cost": (c.get("mana_cost", "") or "").replace("{", "").replace("}", ""),
        }
        if "CREATURE" in types:
            ch["power"] = star_or_int(c.get("power"))
            ch["toughness"] = star_or_int(c.get("toughness"))
        if "PLANESWALKER" in types:
            ch["loyalty"] = star_or_int(c.get("loyalty"))
        if subtypes:
            ch["subtype"] = subtypes

        abilities = []
        for kw in raw.get("keywords", []):
            member = _ability_member(kw)
            if member:
                abilities.append("static_abilities.StaticAbilities." + member)

        supertype_src = (
            "[" + ", ".join("cardtype.SuperType." + s for s in supertypes) + "]"
        )
        types_src = "[" + ", ".join("cardtype.CardType." + t for t in types) + "]"
        abilities_src = "[" + ", ".join(abilities) + "]"

        out.append(
            'class {id}(card.Card):\n'
            '    "{name}"\n'
            "    def __init__(self):\n"
            "        super({id}, self).__init__(gameobject.Characteristics("
            "**{ch!r}, supertype={sup}, types={typ}, abilities={ab}))\n\n".format(
                id=ID,
                name=name.replace('"', '\\"'),
                ch=ch,
                sup=supertype_src,
                typ=types_src,
                ab=abilities_src,
            )
        )
        name_to_id[name] = ID
        name_to_id[full_name] = ID  # decklists / Moxfield use the combined name

    with open("data/%s_cards.py" % NAME, "w") as f:
        f.writelines(out)
    with open("data/%s_name_to_id_dict.pkl" % NAME, "wb") as f:
        pickle.dump(name_to_id, f)

    print("wrote %d card classes to data/%s_cards.py" % (len(name_to_id), NAME))


if __name__ == "__main__":
    run()
