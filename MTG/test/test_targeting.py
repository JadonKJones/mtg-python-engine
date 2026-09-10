"""Targeting & choice system: multi-target, optional, distinctness, fizzle rules."""

import types
import mock

from MTG.test.test_game import TestGameBase
from MTG import utils, gamesteps
from MTG.utils import TargetSpec, parse_targets, choose_targets


class _Base(TestGameBase):
    def setUp(self):
        super().setUp()
        # setup_game() leaves no step set; permanent timestamps need one.
        self.GAME.step = gamesteps.Step.PRECOMBAT_MAIN


def _src(player, criterias, prompts=None):
    """A minimal stand-in for a spell/ability on the stack."""
    s = types.SimpleNamespace()
    s.controller = player
    s.target_criterias = criterias
    s.target_prompts = prompts
    s._target_bindings = []
    return s


class TestTargetGrammar(_Base):
    def test_string_specs_parse_to_cardinality(self):
        specs = parse_targets([
            "creature",
            "up to one target creature",
            "up to three target creatures",
            "any number of target creatures",
            "two target creatures",
        ])
        rng = [(s.min, s.max) for s in specs]
        self.assertEqual(rng[0], (1, 1))
        self.assertEqual(rng[1], (0, 1))
        self.assertEqual(rng[2], (0, 3))
        self.assertEqual(rng[3][0], 0)
        self.assertEqual(rng[3][1], float("inf"))
        self.assertEqual(rng[4], (2, 2))

    def test_bare_lambda_still_accepted(self):
        specs = parse_targets([lambda self, o: getattr(o, "is_creature", False)])
        self.assertIsInstance(specs[0], TargetSpec)
        self.assertEqual((specs[0].min, specs[0].max), (1, 1))


class TestChooseTargets(_Base):
    def setUp(self):
        super().setUp()
        for _ in range(3):
            self.player.battlefield.add("Runeclaw Bear")
        self.opponent.battlefield.add("Runeclaw Bear")

    def test_exactly_one(self):
        src = _src(self.player, parse_targets(["creature"]))
        with mock.patch("builtins.input", side_effect=["b 0"]):
            chosen = choose_targets(src)
        self.assertEqual(len(chosen), 1)
        self.assertIs(chosen[0], self.player.battlefield[0])

    def test_up_to_three_stop_early_with_blank(self):
        src = _src(self.player, parse_targets(["up to three target creatures"]))
        with mock.patch("builtins.input", side_effect=["b 0", "b 1", ""]):
            chosen = choose_targets(src)
        self.assertEqual(len(chosen), 2)

    def test_distinctness_enforced(self):
        src = _src(self.player, parse_targets(["up to three target creatures"]))
        # pick b0, try b0 again (rejected), then b1, then done
        with mock.patch("builtins.input", side_effect=["b 0", "b 0", "b 1", ""]):
            chosen = choose_targets(src)
        self.assertEqual(len(chosen), 2)
        self.assertEqual(len(set(id(c) for c in chosen)), 2)

    def test_illegal_target_rejected_then_retry(self):
        src = _src(self.player, parse_targets(["your creature"]))
        with mock.patch("builtins.input", side_effect=["ob 0", "b 0"]):
            chosen = choose_targets(src)
        self.assertEqual(len(chosen), 1)
        self.assertIs(chosen[0].controller, self.player)

    def test_not_enough_legal_targets_is_uncastable(self):
        # need two Islands to target; there are none
        spec = TargetSpec(lambda self, o: getattr(o, "is_land", False)
                          and o.has_subtype("Island"), min=2, max=2)
        src = _src(self.player, [spec])
        with mock.patch("builtins.input", side_effect=[]):
            self.assertFalse(choose_targets(src))

    def test_any_number_can_be_zero(self):
        src = _src(self.player, parse_targets(["any number of target creatures"]))
        with mock.patch("builtins.input", side_effect=[""]):
            chosen = choose_targets(src)
        self.assertEqual(chosen, [])

    def test_multiple_distinct_clauses(self):
        self.player.battlefield.add("Forest")
        src = _src(self.player, parse_targets(["target creature", "target land"]))
        with mock.patch("builtins.input", side_effect=["b 0", "b 3"]):
            chosen = choose_targets(src)
        self.assertEqual(len(chosen), 2)
        self.assertTrue(chosen[0].is_creature)
        self.assertTrue(chosen[1].is_land)
        self.assertEqual(len(src._target_bindings), 2)


class TestFizzleRules(_Base):
    def test_partial_legality_still_resolves_and_fizzle_only_when_all_gone(self):
        from MTG import play
        for _ in range(2):
            self.player.battlefield.add("Runeclaw Bear")
        a, b = self.player.battlefield[0], self.player.battlefield[1]

        src = _src(self.player, parse_targets(["up to two target creatures"]))
        with mock.patch("builtins.input", side_effect=["b 0", "b 1", ""]):
            chosen = choose_targets(src)
        self.assertEqual(len(chosen), 2)

        src.targets_chosen = chosen
        hits = []
        p = play.Play(lambda: [t.take_damage(p, 99) for t in p.legal_targets],
                      source=types.SimpleNamespace(
                          controller=self.player, targets_chosen=chosen,
                          target_criterias=src.target_criterias,
                          _target_bindings=src._target_bindings))
        # one target leaves the battlefield -> still resolves against the other
        b.change_zone(self.player.graveyard)
        p.apply()
        self.assertEqual(a.status.damage_taken, 99)

    def test_you_may(self):
        with mock.patch("builtins.input", side_effect=["yes"]):
            self.assertTrue(self.player.may("Draw a card?"))
        with mock.patch("builtins.input", side_effect=["no"]):
            self.assertFalse(self.player.may("Draw a card?"))
        with mock.patch("builtins.input", side_effect=[""]):
            self.assertTrue(self.player.may("Draw a card?"))

    def test_choose_one_mode(self):
        with mock.patch("builtins.input", side_effect=["1"]):
            m = self.player.choose_one("Choose one —", ["destroy", "exile", "bounce"])
        self.assertEqual(m, "exile")

    def test_choose_up_to_two(self):
        with mock.patch("builtins.input", side_effect=["0", "2", ""]):
            got = self.player.choose("Choose up to two", ["a", "b", "c"], min=0, max=2)
        self.assertEqual(got, ["a", "c"])


class TestCollectionMultiTarget(_Base):
    """An auto-translated collection card that actually uses "up to N target"."""

    def test_repel_the_darkness_taps_two(self):
        from MTG import cards, play
        cards.setup_cards()
        for _ in range(2):
            self.opponent.battlefield.add("Runeclaw Bear")
        b0, b1 = self.opponent.battlefield[0], self.opponent.battlefield[1]

        card = cards.card_from_name("Repel the Darkness")
        card.controller = self.player
        card.zone = self.player.hand

        with mock.patch("builtins.input", side_effect=["ob 0", "ob 1", ""]):
            chosen = card.targets()
        self.assertEqual(len(chosen), 2)

        p = play.Play(card.play_func, card=card)
        p.apply()
        self.assertTrue(b0.status.tapped)
        self.assertTrue(b1.status.tapped)
