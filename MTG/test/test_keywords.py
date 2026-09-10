"""Tier-1 named keyword mechanics."""

import mock

from MTG.test.test_game import TestGameBase
from MTG import gamesteps, cards


class _KW(TestGameBase):
    def setUp(self):
        super().setUp()
        self.GAME.step = gamesteps.Step.PRECOMBAT_MAIN
        # setup_cards() already ran once at test_game import; calling it again
        # duplicates every card's static effects (it appends to class state).

    def _bf(self, player, name):
        player.battlefield.add(name)
        return player.battlefield[-1]


class TestInfect(_KW):
    def test_infect_damage_to_creature_is_minus_counters(self):
        # Lost Leonin: 2/2 Infect
        leo = self._bf(self.player, "Lost Leonin")
        bear = self._bf(self.opponent, "Runeclaw Bear")  # 2/2
        leo.deals_damage(bear, leo.power, is_combat=True)
        self.assertEqual(bear.num_counters("-1/-1"), 2)
        self.assertEqual(bear.status.damage_taken, 0)
        # 2/2 with two -1/-1 -> 0 toughness -> dies on SBA
        self.assertEqual(bear.toughness, 0)

    def test_infect_damage_to_player_is_poison(self):
        leo = self._bf(self.player, "Lost Leonin")
        leo.deals_damage(self.opponent, 2, is_combat=True)
        self.assertEqual(self.opponent.poison, 2)
        self.assertEqual(self.opponent.life, self.opponent.startingLife)

    def test_ten_poison_loses(self):
        self.opponent.poison = 10
        with self.assertRaises(Exception):
            self.GAME.apply_state_based_actions()  # GameOverException


class TestEvolve(_KW):
    def test_evolve_gets_counter_from_bigger_creature(self):
        one = self._bf(self.player, "Experiment One")  # 1/1 Evolve
        self.assertEqual(one.num_counters("+1/+1"), 0)
        with mock.patch("builtins.input", side_effect=[""]):
            self.player.battlefield.add("Runeclaw Bear")  # 2/2 -> triggers evolve
            self.player.trigger("onControllerCreatureEtB", source=self.player.battlefield[-1])
            for t in self.player.pending_triggers[:]:
                self.GAME.stack.add(t.put_on_stack())
            while self.GAME.stack:
                self.GAME.apply_stack_item(self.GAME.stack[-1])
        self.assertEqual(one.num_counters("+1/+1"), 1)


class TestUnleash(_KW):
    def test_cant_block_while_it_has_a_plus_counter(self):
        # Rakdos Cackler: Unleash -> static "can't block while it has a +1/+1 counter"
        cackler = self._bf(self.player, "Rakdos Cackler")
        self.assertTrue(cackler.can_block())
        cackler.add_counter("+1/+1")
        cackler.check_effect_expiration()
        self.assertFalse(cackler.can_block())
        # remove the counter -> can block again
        cackler.status.counters["+1/+1"] = 0
        cackler.check_effect_expiration()
        self.assertTrue(cackler.can_block())


class TestConditionTriggers(_KW):
    def _resolve_pending(self, player):
        for t in list(player.pending_triggers):
            item = t.put_on_stack()
            if item:
                self.GAME.stack.add(item)
        player.pending_triggers = []
        while self.GAME.stack:
            self.GAME.apply_stack_item(self.GAME.stack[-1])

    def test_bloodthirst_needs_opponent_damaged(self):
        # Gorehorn Minotaurs: Bloodthirst 2
        self.player.battlefield.add("Gorehorn Minotaurs")
        m1 = self.player.battlefield[-1]
        self._resolve_pending(self.player)
        self.assertEqual(m1.num_counters("+1/+1"), 0)  # no damage yet

        self.opponent.turn_events['damaged'] = 3
        self.player.battlefield.add("Gorehorn Minotaurs")
        m2 = self.player.battlefield[-1]
        self._resolve_pending(self.player)
        self.assertEqual(m2.num_counters("+1/+1"), 2)

    def test_revolt_needs_a_permanent_to_have_left(self):
        self.opponent.battlefield.add("Runeclaw Bear")
        bear = self.opponent.battlefield[-1]

        self.player.battlefield.add("Vengeful Rebel")
        # no permanent left this turn -> trigger's intervening-if fails
        self._resolve_pending(self.player)
        self.assertEqual(bear.get_effect("modifyPT"), [])

        self.player.turn_events['permanent_left'] = True
        self.player.battlefield.add("Vengeful Rebel")
        with mock.patch("builtins.input", side_effect=["ob 0"]):
            self._resolve_pending(self.player)
        self.assertEqual(bear.power, 2 - 3)


class TestHandAbilities(_KW):
    def test_cycling_discards_and_draws(self):
        # Stir the Sands: Cycling {3}{B}
        self.player.add_card_to_hand("Stir the Sands")
        card = self.player.hand[-1]
        start_hand = len(self.player.hand)
        start_lib = len(self.player.library)
        self.player.mana.add_str("BBBB1111")
        with mock.patch("builtins.input", side_effect=["c Stir the Sands", ""]):
            item = self.player.get_action()
        self.assertIn(card, self.player.graveyard)   # discard cost paid
        self.GAME.stack.add(item)
        self.GAME.apply_stack_item(item)
        self.assertEqual(len(self.player.library), start_lib - 1)  # drew 1

    def test_improvise_taps_artifacts_for_generic(self):
        # give the player 3 Ornithopters and a spell that costs generic
        for _ in range(3):
            self.player.battlefield.add("Ornithopter")
        arts = list(self.player.battlefield)
        self.player.add_card_to_hand("Maverick Thopterist")  # {3}{U}{R}, Improvise
        self.player.mana.add_str("UR")  # only the coloured pips in pool
        with mock.patch("builtins.input", side_effect=["p Maverick Thopterist", "0 1 2", "", ""]):
            self.player.get_action()
        # 3 artifacts tapped to pay the {3}
        self.assertEqual(sum(1 for a in arts if a.status.tapped), 3)
        self.assertNotIn("Maverick Thopterist",
                         [c.name for c in self.player.hand])


class TestMetalcraft(_KW):
    def test_metalcraft_static_toggles_on_three_artifacts(self):
        warden = self._bf(self.player, "Ghalma's Warden")  # 1/4, metalcraft +2/+2
        base_p = warden.power
        for _ in range(3):
            self.player.battlefield.add("Ornithopter")
        self.GAME.apply_to_battlefield(lambda p: p.check_effect_expiration())
        self.assertEqual(warden.power, base_p + 2)
