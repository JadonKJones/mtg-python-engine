"""Smoke tests for the Moxfield collection integration."""

import json
import re

from MTG.test.test_game import TestGameBase
from MTG import cards


def _wired_cards():
    names = []
    with open("COLLECTION_COVERAGE.md") as f:
        section = None
        for line in f:
            h = re.match(r"## (\w+)", line)
            if h:
                section = h.group(1)
            m = re.match(r"- (.+?) —", line)
            if m and section in ("implemented", "partial"):
                names.append(m.group(1).split(" // ")[0])
    return names


class TestCollectionBuild(TestGameBase):
    def test_every_collection_card_constructs(self):
        obj = json.load(open("collection.json"))
        failed = []
        for name in obj:
            try:
                cards.card_from_name(name)
            except Exception as e:  # noqa
                failed.append((name, repr(e)))
        self.assertEqual(failed, [])

    def test_collection_deck_loads(self):
        deck = cards.read_deck("data/decks/collection.txt")
        self.assertEqual(len(deck), 1234)

    def test_wired_cards_play_without_crashing(self):
        from parser.validate_collection import play_card, wired_cards
        crashed = []
        for name in wired_cards():
            try:
                play_card(name)
            except Exception as e:  # noqa
                crashed.append((name, repr(e)))
        self.assertEqual(crashed, [])

    def test_translated_cards_have_rules_wired(self):
        # setup_cards() ran at import; each implemented/partial card should now
        # carry targets, a custom play_func, an activated ability, a trigger,
        # a static effect, or aura continuous effects.
        unwired = []
        for name in _wired_cards():
            k = cards.card_from_name(name, get_instance=False)
            wired = (
                getattr(k, "target_criterias", None)
                or k.play_func is not cards.card.Card.play_func
                or k.activated_abilities
                or k.triggers
                or k.static_effects
                or k.continuous_effects
            )
            if not wired:
                unwired.append(name)
        self.assertEqual(unwired, [])
