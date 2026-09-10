"""Play every wired collection card in a real game and report crashes.

For each card the translator wired (implemented / partial), start a 2-player
game with a dummy creature on each side, put the card in hand with full mana,
cast/activate it, resolve the stack, and record any exception.

    python -m parser.validate_collection          # summary
    python -m parser.validate_collection -v       # + tracebacks
"""

import io
import re
import sys
import contextlib
import traceback

import mock

from MTG import game, cards

cards.setup_cards()


def wired_cards():
    names, section = [], None
    with open("COLLECTION_COVERAGE.md") as f:
        for line in f:
            h = re.match(r"## (\w+)", line)
            if h:
                section = h.group(1)
            m = re.match(r"- (.+?) —", line)
            if m and section in ("implemented", "partial"):
                names.append(m.group(1).split(" // ")[0])
    return names


class Responder:
    """Answers the engine's input() prompts to cast one card and pass."""

    _TARGETS = ("ob 0", "op", "b 0", "s 0", "b 1", "")

    def __init__(self, card_name):
        self.card_name = card_name
        self.cast = False
        self.calls = 0
        self.t = 0

    def __call__(self, prompt=""):
        self.calls += 1
        if self.calls > 400:
            raise StopIteration  # safety: end the game
        p = prompt.lower()
        if "what would you like to do" in p:
            if "*" not in prompt or "precombat_main" not in p:
                return ""                    # opp priority, or not our main phase
            if not getattr(self, "_bear1", False):
                self._bear1 = True
                return '__self.battlefield.add("Runeclaw Bear")'
            if not getattr(self, "_bear2", False):
                self._bear2 = True
                return '__self.game.opponent(self).battlefield.add("Runeclaw Bear")'
            if not getattr(self, "_mana", False):
                self._mana = True
                return '__self.mana.add_str("WWWWWWUUUUUUBBBBBBRRRRRRGGGGGG' + "1" * 30 + '")'
            if not self.cast:
                self.cast = True
                return "p %s" % self.card_name
            return ""
        if "keep" in p and "on top" in p:
            return "yes"
        if "would you like to" in p or "you may" in p:
            return "yes"
        if "which" in p or "choose" in p or "target" in p or "avaliable" in p:
            cand = self._TARGETS[self.t % len(self._TARGETS)]
            self.t += 1
            return cand
        if re.search(r"order|first", p):
            return "0"
        return ""


def play_card(name):
    decks = [cards.read_deck("data/decks/deck1.txt"),
             cards.read_deck("data/decks/deck1.txt")]
    g = game.Game(decks, test=True)
    g.setup_game()
    pl, opp = g.players_list
    for player in (pl, opp):
        player.hand.clear()
        player.autoPayMana = True
    pl.add_card_to_hand(name)
    pl.mana.add_str("WWWWWUUUUUBBBBBRRRRRGGGGG" + "1" * 20)

    resp = Responder(name)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), mock.patch("builtins.input", side_effect=resp):
        try:
            g.handle_turn()
        except StopIteration:
            pass
    left_hand = not any(c.name.split(" // ")[0] == name for c in pl.hand)
    return resp.cast and left_hand


def main():
    verbose = "-v" in sys.argv
    names = wired_cards()
    ok, noop, fail = [], [], []
    for name in names:
        try:
            if play_card(name):
                ok.append(name)
            else:
                noop.append(name)
        except Exception as e:  # noqa
            fail.append((name, e, traceback.format_exc()))

    print("\n=== validate_collection ===")
    print("cast & resolved : %d / %d" % (len(ok), len(names)))
    print("could not cast  : %d  %s" % (len(noop), noop if noop else ""))
    print("crashed         : %d" % len(fail))
    for name, e, tb in fail:
        print("  x %-28s %s" % (name, repr(e)))
        if verbose:
            print(tb)
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
