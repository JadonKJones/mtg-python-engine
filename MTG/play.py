import inspect
from MTG import gameobject
from MTG import zone

class Play(gameobject.GameObject):
    """
    Represents an ability or spell on the stack.

    Spells: card = original card
    Abilities: source = card that owns this ability
    """

    # TODO: unify this with gameObject init (particularly with targetting)
    def __init__(self, apply_func, apply_condition=lambda: True, 
                 card=None, source=None, name=None,
                 targets_chosen=None, target_criterias=None, is_mana_ability=False):
        
        # TODO: okay this is really ugly and bug-prone.
        # Think about how to fix this initialization.
        if card:
            controller = card.controller
        elif source:
            controller = source.controller
        else:
            controller = None

        super().__init__(zone=controller.stack if controller else None,
                         controller = controller,
                         characteristics=card.characteristics if card else None)

        self.is_special_action = False
        self.is_mana_ability = is_mana_ability
        self.apply_func = apply_func
        self.apply_condition = apply_condition
        self.original_card = card
        self.source = source
        self.targets_chosen = targets_chosen
        self.target_criterias = target_criterias
        self.countered = False

        if self.characteristics and name:
            self.characteristics.name = name

        origin = None
        if not targets_chosen and card:
            origin = card
        elif not targets_chosen and source:
            origin = source
        if origin is not None:
            self.targets_chosen = origin.targets_chosen
            self.target_criterias = origin.target_criterias
            # (spec, obj) pairs recorded by utils.choose_targets, so resolution
            # re-checks each target against the clause that actually chose it.
            self._target_bindings = getattr(origin, '_target_bindings', None)

        if self.targets_chosen:
            self.target_timestamps = [t.timestamp for t in self.targets_chosen]


    def __repr__(self):
        return "%s (ID: %r)" % (self.name, id(self))
        # + '\n' + inspect.getsource(self.apply)

    # TODO: make this modifiable via temporary effects
    def can_be_countered(self, source=None):
        return True

    def counter(self, source):
        if not self.countered and self.can_be_countered(source):
            self.countered = True
            self.game.apply_stack_item(self)  # will trigger fizzle, 
                                              # remove from stack, move to graveyard
            return True
        return False

    def _still_legal(self):
        """Per chosen target: still the same object (timestamp) AND still a
        legal target for the clause that chose it."""
        chosen = self.targets_chosen or []
        stamps = getattr(self, 'target_timestamps', [None] * len(chosen))
        bindings = getattr(self, '_target_bindings', None)
        if bindings:
            checks = [(spec.criteria, obj) for spec, obj in bindings]
        else:
            crits = self.target_criterias or []
            checks = list(zip(crits, chosen))
        out = []
        for (crit, obj), stamp in zip(checks, stamps):
            try:
                ok = bool(crit(self, obj)) and obj.timestamp == stamp
            except Exception:
                ok = False
            out.append(ok)
        return out

    @property
    def legal_targets(self):
        return [t for t, ok in zip(self.targets_chosen or [], self._still_legal()) if ok]

    def apply(self):
        fizzles = False

        if self.countered:
            print("%r was countered" % self)
            fizzles = True

        # A targeted spell/ability fizzles only if EVERY target is now illegal
        # (CR 608.2b). Partially-legal targeting still resolves; the effect code
        # should act on ``self.legal_targets``.
        elif self.targets_chosen and not any(self._still_legal()):
            print("All targets invalid. %r fizzles." % self)
            fizzles = True

        elif not self.apply_condition():
            print("Intervening-if for %r not satisfied" % self)
            fizzles = True

        if fizzles:
            if self.original_card is not None:
                self.original_card.owner.graveyard.add(self.original_card)
            return

        self.apply_func()

