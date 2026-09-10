# Engine features missing for the Moxfield collection

482 unique cards. 74 have working rules today; **376 need one or more of the
features below**. Ordered roughly by how many cards each blocks. "Scope" is a
rough sense of the work, not an estimate.

Regenerate the per-card breakdown with `python -m parser.translate_oracle`
(`COLLECTION_COVERAGE.md`).

---

## 1. Targeting & choice system  *(blocks ~150 cards — foundational)*

`utils.choose_targets` demands **exactly one legal target per criteria**. That
single limitation is the biggest blocker.

| missing | example cards | scope |
|---|---|---|
| **"up to one/two/N target"** (optional targets) | Ephemeral Shields, Fungal Infection, most modern removal | medium |
| **"any number of target"** | Fanning the Flames, Rolling Thunder | medium |
| **Optional targeting / "you may"** on triggers and spells | Bogardan Lancer, Scrapper Champion, half of ETB creatures | medium |
| **Divide N damage/counters among targets** | Forked Bolt, Arc Trail, Rites of Reaping | medium |
| **Multi-target with distinct effects** (already half-wired) | Gravitic Punch ("target creature deals dmg to target player") | medium |
| **Choose from a list that isn't a game object** — colors, card types, names, numbers, modes | anything with "choose a color", "name a card" | medium |
| **Modal spells** — "Choose one —", "Choose one or both —", escalate, entwine | Consign // Oblivion, Iona's Judgment-style, Repel the Darkness | large |
| **Targeting cards in graveyard / exile / library / hand** as the actual target | every graveyard-recursion spell, Beacon Bolt | medium |

## 2. Casting — alternative & additional costs  *(~40 cards)*

The cast path in `player.get_action` only knows mana cost + the fixed cost
strings in `utils.parse_ability_costs` (`T`, mana, `Pay N life`, `Sacrifice ~`).

| missing | example cards | scope |
|---|---|---|
| **Convoke** (tap creatures to pay) — partially stubbed, not wired | Chord of Calling, Siege Wurm, Overgrown Battlement decks | medium |
| **Improvise** (tap artifacts to pay) | Maverick Thopterist, Reverse Engineer | medium |
| **Kicker / "as an additional cost, …"** (sacrifice, discard, reveal, pay life) | Wet-Toed Coral Merfolk-likes, additional-cost burn | medium |
| **Alternative costs** — "you may pay {X} rather than", free spells | — | medium |
| **Cast from graveyard** — Flashback, Jump-start, Aftermath, Retrace, Escape | Beacon Bolt, Gravitic Punch, Consign // Oblivion, Devious Cover-Up | large |
| **X spells** — `X` in cost, chosen on cast, readable in the effect | Syncopate, Rolling Thunder, Fireball-likes | medium |
| **Cost reduction / increase** — `reduceCost`/`additionalCost` effect hooks exist but are `pass` | affinity, "costs {1} less" | medium |
| **Additional/replacement targets while on the stack**, "can't be countered" as a property | Terra Stomper | small |

## 3. Named keyword mechanics  *(each is self-contained; ~90 cards total)*

None of these are modeled. Each needs a trigger condition or static hook plus its
own resolution. Small individually, many in aggregate.

- **Energy counters** ({E}) — a whole player resource pool (Scrapper Champion, Aether Hub-likes) — *medium, and only worth it for the ~4 energy cards*
- **Surveil N** (~15 cards) — like scry but to graveyard — *small, once `scry` is real*
- **Mentor** (~4) — attack trigger, +1/+1 counter on a lesser-power attacker
- **Battalion** / "attacks with at least two other creatures" (~4)
- **Undergrowth** — count creature cards in your graveyard (~6)
- **Revolt** — "a permanent you controlled left the battlefield this turn" (~5)
- **Bloodthirst** — ETB conditional on an opponent having been dealt damage (~2)
- **Heroic** — trigger when you cast a spell targeting this creature (~2)
- **Bloodrush** — discard from hand for a combat pump (~2)
- **Cycling / Landcycling / Typecycling** — discard-to-draw activated from hand (~2)
- **Bestow** — cast a creature as an Aura (~2)
- **Monstrosity**, **Unleash**, **Evolve**, **Extort**, **Graft**, **Landfall**, **Detain**, **Level up**, **Cipher**, **Scavenge**, **Overload**, **Exert**, **Proliferate**, **Crew** / Vehicles, **Fabricate** — 1–3 cards each

## 4. Effect primitives the engine can't express  *(~120 cards)*

Verbs with no method / no support in `player.py` / `permanent.py`:

| missing | example cards | scope |
|---|---|---|
| **Blink / flicker / exile-and-return** as a spell or ETB effect | Illusionist's Stratagem, Cloudshift-likes | medium |
| **Graveyard recursion** — "return target creature card from your graveyard to your hand/battlefield" (~21) | Gravedigger-likes, Liturgy of Blood, Pilfered Plans | medium |
| **Library search with a real criteria & destination** — `search_lib` exists but library cards are inert `Card`s whose keywords/subtypes aren't queryable | Mwonvuli Beast Tracker, all tutors | medium |
| **Reveal cards** from hand/library and act on them (~16) | Duress-likes, Lay Bare the Heart, impulse draw | medium |
| **Targeted discard / "target player discards a card of your choice"** (~21) | Harsh Scrutiny, Mind Rot-likes | small |
| **Dynamic values** — "for each", "equal to the number of", "equal to its power" (~22) | Beacon Bolt, Congregate-style, Collective effects | medium |
| **Token creation beyond a single vanilla body** — typed tokens with keywords, multiple abilities, "create a copy of", Clue/Treasure/Food with their sac abilities | Call of the Conclave (works), Talrand's Invocation, Efficient Construction | medium |
| **+1/+1 (and −1/−1, other) counter placement outside ETB** — on attack, on cast, on activate, "distribute" (~26) | The Crystal's Chosen, Pursuit of Flight | small–medium |
| **Control-changing effects** — "gain control of target creature" | Portent of Betrayal, Act of Treason-likes | medium |
| **Regeneration** — "the next time this would be destroyed…" | Ancient Silverback-likes | medium |
| **Fight** | Hunt the Weak-likes | small |
| **"Deals damage equal to its power to …"** (creature as damage source) | Gravitic Punch | small |
| **Mill a player / each player, then act on milled cards** | Wand of Vertebrae | small |
| **Life-total set / exchange, "lose half", damage can't reduce below 1** | — | small |
| **Add mana of any color / "in any combination" / conditional mana** | dual lands, Guildmage 5-color asks | small |

## 5. Triggered-ability conditions not in `triggers.triggerConditions`

`triggers.py` has a decent set, but missing:

- **"Whenever you cast an instant or sorcery spell"** (prowess-style, ~9 cards — Talrand, Guildmages)
- **"Whenever this deals combat damage to a player"** (`onCombatDamageToPlayers` exists at the *game* level but there's no per-permanent "this creature" combat-damage-to-player hook wired for cards) (~6)
- **"Whenever this attacks and isn't blocked"**
- **"Whenever a creature you control dies" / "whenever this dies"** — `onDeath` exists for self; "another creature you control dies" is not a controller-scoped condition
- **"Whenever a +1/+1 counter is placed"** on a specific permanent
- **"At the beginning of your upkeep / end step"** on a permanent — phase conditions exist but aren't exposed to the `.txt` trigger vocabulary cleanly
- **"Whenever an Equipment / artifact / enchantment enters"** (typed permanent-ETB, controller-scoped)
- **"Whenever you gain life" beyond the one Ajani's Pridemate case** — `onControllerLifeGain` exists; "lose life", "draw your second card each turn", etc. do not

## 6. Replacement & prevention effects  *(~20 cards)*

The engine has **no replacement-effect layer** at all.

- "If a creature would die this turn, exile it instead" (Annihilating Fire rider, currently dropped)
- "Prevent all combat damage" / "prevent the next N damage" / prevention shields (~10)
- "Damage is dealt to you instead" / redirection
- "Enters with N +1/+1 counters" / "enters tapped" / "enters as a copy" (~11 — `permanent.make_permanent` takes a `status_mod` but nothing computes it from card text)
- "If you would draw, instead …", "skip your draw step"
- Doubling effects ("if an effect would create tokens, create twice as many")

## 7. Continuous effects / layer-system gaps

`_calculate_pt` handles layers 7b–7e only.

- **Ability-granting / ability-removal** as a board-wide static (layer 6) — partial via `gainAbility` but no "loses all abilities", no "base P/T becomes", no type-changing ("becomes an artifact", "is a Vehicle")
- **Characteristic-defining** P/T ("*/*", "power equal to …")
- **Color / type / name changing**
- **"As long as" conditional statics** on other permanents (only self-conditionals work well)
- **Protection from [color/type]** — blocking checks it, nothing grants it
- **Hexproof / shroud granted by an effect** (only printed keyword works)
- **Anthem toggles keyed on subtype/color for *opponents*** — my generator emits a `game`-scoped one but the toggle-func semantics are shaky

## 8. Zones & card state

- **Exile with tracking** — "exile until ~ leaves", "cast it later", "for as long as" — exile is a dumb bin
- **Face-down / manifest / morph**
- **Attaching**: Auras beyond "+N/+N" and one keyword; **Equipment/equip has no code path** (~8 cards); Fortifications
- **"the top card of your library"** interactions, playing from exile
- **Counters other than ±1/±1** on permanents (charge, loyalty, page, etc.) and **counters on players** (energy, experience, poison-as-wincon)

## 9. Planeswalkers

Card type exists; **loyalty abilities, the "activate one per turn" rule, and
damage-to-planeswalker redirection are not implemented.** (Few/none in this
collection, but listed for completeness.)

## 10. Combat gaps

- **Multiple blockers / "can't be blocked except by two or more"**, menace enforcement beyond the flag
- **"Must attack" / "must be blocked" / "can't attack or block"** requirements & restrictions (~11)
- **First-strike step already exists**; **deathtouch + trample**, **damage assignment order**, **trample over planeswalkers** — partial
- **Combat-damage replacement** ("assigns no combat damage", "double strike + first strike interaction with buffs mid-combat")
- **Attack/block triggers on the *blocked/blocking* creature** ("whenever this becomes blocked", "whenever this blocks")

## 11. Multi-face / alternate cards

- **Split cards** (Consign // Oblivion, Integrity // Intervention, Never // Happened, Onward // Victory, etc.) — both halves register to one class using the **front face only**; the second half is uncastable
- **Adventure**, **MDFC**, **transform**, **rooms**, **prototype** — front face only

## 12. Known engine bugs found while wiring the collection

- `permanent.Aura.disenchant()` referenced an undefined `target` — **fixed**
- `gameobject.is_planeswalker` didn't exist — **added**
- `Player.scry` didn't exist — **added (basic)**
- `cards.read_deck` raises `NameError: DecklistFormatException` (not imported) on a malformed line instead of a clean error
- `_calculate_pt` line 385: `effect[1]` should be `effect.value[1]` (setPT path, latent)
- m15 auras use `self.add_PT(...)` but the method is `add_pt` — several shipped M15 aura cards would `AttributeError` on enchant

---

### If you want to prioritize

The highest-leverage items, in order:

1. **Optional / "up to" / multi targeting** (§1) — unlocks the most cards for the least code
2. **A real `scry` + `surveil`** (§3) — ~20 cards, small
3. **Blink/flicker + graveyard-return + reveal/discard primitives** (§4) — ~50 cards
4. **Modal spells** (§1) — ~13 cards, then the split cards
5. **Equip** (§8) — ~8 cards, but a clean self-contained subsystem
6. **Cast-from-graveyard** (§2) — ~5 cards but touches the whole cast pipeline
