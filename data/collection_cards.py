from MTG import card
from MTG import gameobject
from MTG import cardtype
from MTG import static_abilities
from MTG import mana

class c420849(card.Card):
    "Zhur-Taa Druid"
    def __init__(self):
        super(c420849, self).__init__(gameobject.Characteristics(**{'name': 'Zhur-Taa Druid', 'text': '{T}: Add {G}.\nWhenever you tap this creature for mana, it deals 1 damage to each opponent.', 'color': ['G', 'R'], 'mana_cost': 'RG', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Druid']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c190167(card.Card):
    "Zephyr Sprite"
    def __init__(self):
        super(c190167, self).__init__(gameobject.Characteristics(**{'name': 'Zephyr Sprite', 'text': 'Flying', 'color': ['U'], 'mana_cost': 'U', 'power': 1, 'toughness': 1, 'subtype': ['Faerie']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c466795(card.Card):
    "Yoked Ox"
    def __init__(self):
        super(c466795, self).__init__(gameobject.Characteristics(**{'name': 'Yoked Ox', 'text': '', 'color': ['W'], 'mana_cost': 'W', 'power': 0, 'toughness': 4, 'subtype': ['Ox']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452965(card.Card):
    "Worldsoul Colossus"
    def __init__(self):
        super(c452965, self).__init__(gameobject.Characteristics(**{'name': 'Worldsoul Colossus', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nThis creature enters with X +1/+1 counters on it.", 'color': ['G', 'W'], 'mana_cost': 'XGW', 'power': 0, 'toughness': 0, 'subtype': ['Elemental']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Convoke]))

class c9857669744(card.Card):
    "Wojek Bodyguard"
    def __init__(self):
        super(c9857669744, self).__init__(gameobject.Characteristics(**{'name': 'Wojek Bodyguard', 'text': "Mentor (Whenever this creature attacks, put a +1/+1 counter on target attacking creature with lesser power.)\nThis creature can't attack or block alone.", 'color': ['R'], 'mana_cost': '2R', 'power': 3, 'toughness': 3, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373622(card.Card):
    "Witches' Eye"
    def __init__(self):
        super(c373622, self).__init__(gameobject.Characteristics(**{'name': "Witches' Eye", 'text': 'Equipped creature has "{1}, {T}: Scry 1." (To scry 1, look at the top card of your library, then you may put that card on the bottom.)\nEquip {1}', 'color': [], 'mana_cost': '1', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c9519882455(card.Card):
    "Wishcoin Crab"
    def __init__(self):
        super(c9519882455, self).__init__(gameobject.Characteristics(**{'name': 'Wishcoin Crab', 'text': '', 'color': ['U'], 'mana_cost': '3U', 'power': 2, 'toughness': 5, 'subtype': ['Crab']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9198126280(card.Card):
    "Windurst, Federation Center"
    def __init__(self):
        super(c9198126280, self).__init__(gameobject.Characteristics(**{'name': 'Windurst, Federation Center', 'text': 'This land enters tapped.\n{T}: Add {G} or {W}.', 'color': ['G', 'W'], 'mana_cost': '', 'subtype': ['Town']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c9744126460(card.Card):
    "Wind-Kin Raiders"
    def __init__(self):
        super(c9744126460, self).__init__(gameobject.Characteristics(**{'name': 'Wind-Kin Raiders', 'text': "Improvise (Your artifacts can help cast this spell. Each artifact you tap after you're done activating mana abilities pays for {1}.)\nFlying", 'color': ['U'], 'mana_cost': '4UU', 'power': 4, 'toughness': 3, 'subtype': ['Human', 'Artificer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Improvise]))

class c240098(card.Card):
    "Wildwood Geist"
    def __init__(self):
        super(c240098, self).__init__(gameobject.Characteristics(**{'name': 'Wildwood Geist', 'text': 'During your turn, this creature gets +2/+2.', 'color': ['G'], 'mana_cost': '4G', 'power': 3, 'toughness': 3, 'subtype': ['Spirit']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c370791(card.Card):
    "Wild Guess"
    def __init__(self):
        super(c370791, self).__init__(gameobject.Characteristics(**{'name': 'Wild Guess', 'text': 'As an additional cost to cast this spell, discard a card.\nDraw two cards.', 'color': ['R'], 'mana_cost': 'RR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c452900(card.Card):
    "Wild Ceratok"
    def __init__(self):
        super(c452900, self).__init__(gameobject.Characteristics(**{'name': 'Wild Ceratok', 'text': '', 'color': ['G'], 'mana_cost': '3G', 'power': 4, 'toughness': 3, 'subtype': ['Rhino']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9107392441(card.Card):
    "White Mage's Staff"
    def __init__(self):
        super(c9107392441, self).__init__(gameobject.Characteristics(**{'name': "White Mage's Staff", 'text': 'Job select (When this Equipment enters, create a 1/1 colorless Hero creature token, then attach this to it.)\nEquipped creature gets +1/+1, has "Whenever this creature attacks, you gain 1 life," and is a Cleric in addition to its other types.\nEquip {3} ({3}: Attach to target creature you control. Equip only as a sorcery.)', 'color': ['W'], 'mana_cost': '1W', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c452840(card.Card):
    "Whispering Snitch"
    def __init__(self):
        super(c452840, self).__init__(gameobject.Characteristics(**{'name': 'Whispering Snitch', 'text': 'Whenever you surveil for the first time each turn, this creature deals 1 damage to each opponent and you gain 1 life.', 'color': ['B'], 'mana_cost': '1B', 'power': 1, 'toughness': 3, 'subtype': ['Vampire', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452970(card.Card):
    "Whisper Agent"
    def __init__(self):
        super(c452970, self).__init__(gameobject.Characteristics(**{'name': 'Whisper Agent', 'text': 'Flash\nWhen this creature enters, surveil 1. (Look at the top card of your library. You may put it into your graveyard.)', 'color': ['B', 'U'], 'mana_cost': '1U/BU/B', 'power': 3, 'toughness': 2, 'subtype': ['Human', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash]))

class c9956152480(card.Card):
    "Wee Dragonauts"
    def __init__(self):
        super(c9956152480, self).__init__(gameobject.Characteristics(**{'name': 'Wee Dragonauts', 'text': 'Flying\nWhenever you cast an instant or sorcery spell, this creature gets +2/+0 until end of turn.', 'color': ['R', 'U'], 'mana_cost': '1UR', 'power': 1, 'toughness': 3, 'subtype': ['Faerie', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c426940(card.Card):
    "Watchers of the Dead"
    def __init__(self):
        super(c426940, self).__init__(gameobject.Characteristics(**{'name': 'Watchers of the Dead', 'text': 'Exile this creature: Each opponent chooses two cards in their graveyard and exiles the rest.', 'color': [], 'mana_cost': '2', 'power': 2, 'toughness': 2, 'subtype': ['Cat']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c452899(card.Card):
    "Wary Okapi"
    def __init__(self):
        super(c452899, self).__init__(gameobject.Characteristics(**{'name': 'Wary Okapi', 'text': 'Vigilance', 'color': ['G'], 'mana_cost': '2G', 'power': 3, 'toughness': 2, 'subtype': ['Antelope']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance]))

class c426857(card.Card):
    "Warfire Javelineer"
    def __init__(self):
        super(c426857, self).__init__(gameobject.Characteristics(**{'name': 'Warfire Javelineer', 'text': 'When this creature enters, it deals X damage to target creature an opponent controls, where X is the number of instant and sorcery cards in your graveyard.', 'color': ['R'], 'mana_cost': '3R', 'power': 2, 'toughness': 3, 'subtype': ['Minotaur', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c230078(card.Card):
    "War Report"
    def __init__(self):
        super(c230078, self).__init__(gameobject.Characteristics(**{'name': 'War Report', 'text': 'You gain life equal to the number of creatures on the battlefield plus the number of artifacts on the battlefield.', 'color': ['W'], 'mana_cost': '3W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452992(card.Card):
    "Wand of Vertebrae"
    def __init__(self):
        super(c452992, self).__init__(gameobject.Characteristics(**{'name': 'Wand of Vertebrae', 'text': '{T}: Mill a card.\n{2}, {T}, Exile this artifact: Shuffle up to five target cards from your graveyard into your library.', 'color': [], 'mana_cost': '1'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c9388478042(card.Card):
    "Wall of Fire"
    def __init__(self):
        super(c9388478042, self).__init__(gameobject.Characteristics(**{'name': 'Wall of Fire', 'text': "Defender (This creature can't attack.)\n{R}: This creature gets +1/+0 until end of turn.", 'color': ['R'], 'mana_cost': '1RR', 'power': 0, 'toughness': 5, 'subtype': ['Wall']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c466955(card.Card):
    "Vorstclaw"
    def __init__(self):
        super(c466955, self).__init__(gameobject.Characteristics(**{'name': 'Vorstclaw', 'text': '', 'color': ['G'], 'mana_cost': '4GG', 'power': 7, 'toughness': 7, 'subtype': ['Elemental', 'Horror']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c214381(card.Card):
    "Volt Charge"
    def __init__(self):
        super(c214381, self).__init__(gameobject.Characteristics(**{'name': 'Volt Charge', 'text': 'Volt Charge deals 3 damage to any target. Proliferate. (Choose any number of permanents and/or players, then give each another counter of each kind already there.)', 'color': ['R'], 'mana_cost': '2R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c366267(card.Card):
    "Vizkopa Confessor"
    def __init__(self):
        super(c366267, self).__init__(gameobject.Characteristics(**{'name': 'Vizkopa Confessor', 'text': 'Extort (Whenever you cast a spell, you may pay {W/B}. If you do, each opponent loses 1 life and you gain that much life.)\nWhen this creature enters, pay any amount of life. Target opponent reveals that many cards from their hand. You choose one of them and exile it.', 'color': ['B', 'W'], 'mana_cost': '3WB', 'power': 1, 'toughness': 3, 'subtype': ['Human', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c423505(card.Card):
    "Viridian Emissary"
    def __init__(self):
        super(c423505, self).__init__(gameobject.Characteristics(**{'name': 'Viridian Emissary', 'text': 'When this creature dies, you may search your library for a basic land card, put it onto the battlefield tapped, then shuffle.', 'color': ['G'], 'mana_cost': '1G', 'power': 2, 'toughness': 1, 'subtype': ['Phyrexian', 'Elf', 'Scout']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c107293(card.Card):
    "Vigean Hydropon"
    def __init__(self):
        super(c107293, self).__init__(gameobject.Characteristics(**{'name': 'Vigean Hydropon', 'text': "Graft 5 (This creature enters with five +1/+1 counters on it. Whenever another creature enters, you may move a +1/+1 counter from this creature onto it.)\nThis creature can't attack or block.", 'color': ['G', 'U'], 'mana_cost': '1GU', 'power': 0, 'toughness': 0, 'subtype': ['Plant', 'Mutant']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c366264(card.Card):
    "Viashino Shanktail"
    def __init__(self):
        super(c366264, self).__init__(gameobject.Characteristics(**{'name': 'Viashino Shanktail', 'text': 'First strike\nBloodrush — {2}{R}, Discard this card: Target attacking creature gets +3/+1 and gains first strike until end of turn.', 'color': ['R'], 'mana_cost': '3R', 'power': 3, 'toughness': 1, 'subtype': ['Lizard', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.First_Strike]))

class c265379(card.Card):
    "Viashino Racketeer"
    def __init__(self):
        super(c265379, self).__init__(gameobject.Characteristics(**{'name': 'Viashino Racketeer', 'text': 'When this creature enters, you may discard a card. If you do, draw a card.', 'color': ['R'], 'mana_cost': '2R', 'power': 2, 'toughness': 1, 'subtype': ['Lizard', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c456831(card.Card):
    "Vessel of Endless Rest"
    def __init__(self):
        super(c456831, self).__init__(gameobject.Characteristics(**{'name': 'Vessel of Endless Rest', 'text': "When this artifact enters, put target card from a graveyard on the bottom of its owner's library.\n{T}: Add one mana of any color.", 'color': [], 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c423740(card.Card):
    "Vengeful Rebel"
    def __init__(self):
        super(c423740, self).__init__(gameobject.Characteristics(**{'name': 'Vengeful Rebel', 'text': 'Revolt — When this creature enters, if a permanent left the battlefield under your control this turn, target creature an opponent controls gets -3/-3 until end of turn.', 'color': ['B'], 'mana_cost': '2B', 'power': 3, 'toughness': 2, 'subtype': ['Aetherborn', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452838(card.Card):
    "Veiled Shade"
    def __init__(self):
        super(c452838, self).__init__(gameobject.Characteristics(**{'name': 'Veiled Shade', 'text': '{1}{B}: This creature gets +1/+1 until end of turn.', 'color': ['B'], 'mana_cost': '2B', 'power': 2, 'toughness': 2, 'subtype': ['Shade']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452807(card.Card):
    "Vedalken Mesmerist"
    def __init__(self):
        super(c452807, self).__init__(gameobject.Characteristics(**{'name': 'Vedalken Mesmerist', 'text': 'Whenever this creature attacks, target creature an opponent controls gets -2/-0 until end of turn.', 'color': ['U'], 'mana_cost': '1U', 'power': 2, 'toughness': 1, 'subtype': ['Vedalken', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c366415(card.Card):
    "Urbis Protector"
    def __init__(self):
        super(c366415, self).__init__(gameobject.Characteristics(**{'name': 'Urbis Protector', 'text': 'When this creature enters, create a 4/4 white Angel creature token with flying.', 'color': ['W'], 'mana_cost': '4WW', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452896(card.Card):
    "Urban Utopia"
    def __init__(self):
        super(c452896, self).__init__(gameobject.Characteristics(**{'name': 'Urban Utopia', 'text': 'Enchant land\nWhen this Aura enters, draw a card.\nEnchanted land has "{T}: Add one mana of any color."', 'color': ['G'], 'mana_cost': '1G', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c9715525349(card.Card):
    "Urban Evolution"
    def __init__(self):
        super(c9715525349, self).__init__(gameobject.Characteristics(**{'name': 'Urban Evolution', 'text': 'Draw three cards. You may play an additional land this turn.', 'color': ['G', 'U'], 'mana_cost': '3GU'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c466832(card.Card):
    "Unsummon"
    def __init__(self):
        super(c466832, self).__init__(gameobject.Characteristics(**{'name': 'Unsummon', 'text': "Return target creature to its owner's hand.", 'color': ['U'], 'mana_cost': 'U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452806(card.Card):
    "Unexplained Disappearance"
    def __init__(self):
        super(c452806, self).__init__(gameobject.Characteristics(**{'name': 'Unexplained Disappearance', 'text': "Return target creature to its owner's hand.\nSurveil 1. (Look at the top card of your library. You may put that card into your graveyard.)", 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452960(card.Card):
    "Undercity Uprising"
    def __init__(self):
        super(c452960, self).__init__(gameobject.Characteristics(**{'name': 'Undercity Uprising', 'text': "Creatures you control gain deathtouch until end of turn. Then target creature you control fights target creature you don't control. (Each deals damage equal to its power to the other.)", 'color': ['B', 'G'], 'mana_cost': '2BG'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c452837(card.Card):
    "Undercity Necrolisk"
    def __init__(self):
        super(c452837, self).__init__(gameobject.Characteristics(**{'name': 'Undercity Necrolisk', 'text': "{1}, Sacrifice another creature: Put a +1/+1 counter on this creature. It gains menace until end of turn. Activate only as a sorcery. (It can't be blocked except by two or more creatures.)", 'color': ['B'], 'mana_cost': '3B', 'power': 3, 'toughness': 3, 'subtype': ['Zombie', 'Lizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c485491(card.Card):
    "Turn to Slag"
    def __init__(self):
        super(c485491, self).__init__(gameobject.Characteristics(**{'name': 'Turn to Slag', 'text': 'Turn to Slag deals 5 damage to target creature. Destroy all Equipment attached to that creature.', 'color': ['R'], 'mana_cost': '3RR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c240064(card.Card):
    "Trusted Forcemage"
    def __init__(self):
        super(c240064, self).__init__(gameobject.Characteristics(**{'name': 'Trusted Forcemage', 'text': 'Soulbond (You may pair this creature with another unpaired creature when either enters. They remain paired for as long as you control both of them.)\nAs long as this creature is paired with another creature, each of those creatures gets +1/+1.', 'color': ['G'], 'mana_cost': '2G', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452959(card.Card):
    "Truefire Captain"
    def __init__(self):
        super(c452959, self).__init__(gameobject.Characteristics(**{'name': 'Truefire Captain', 'text': 'Mentor (Whenever this creature attacks, put a +1/+1 counter on target attacking creature with lesser power.)\nWhenever this creature is dealt damage, it deals that much damage to target player.', 'color': ['R', 'W'], 'mana_cost': 'RRWW', 'power': 4, 'toughness': 3, 'subtype': ['Human', 'Knight']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c380235(card.Card):
    "Treasured Find"
    def __init__(self):
        super(c380235, self).__init__(gameobject.Characteristics(**{'name': 'Treasured Find', 'text': 'Return target card from your graveyard to your hand. Exile Treasured Find.', 'color': ['B', 'G'], 'mana_cost': 'BG'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c198177(card.Card):
    "Traitorous Instinct"
    def __init__(self):
        super(c198177, self).__init__(gameobject.Characteristics(**{'name': 'Traitorous Instinct', 'text': 'Gain control of target creature until end of turn. Untap that creature. Until end of turn, it gets +2/+0 and gains haste.', 'color': ['R'], 'mana_cost': '3R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c366404(card.Card):
    "Tower Defense"
    def __init__(self):
        super(c366404, self).__init__(gameobject.Characteristics(**{'name': 'Tower Defense', 'text': 'Creatures you control get +0/+5 and gain reach until end of turn.', 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c198175(card.Card):
    "Totem-Guide Hartebeest"
    def __init__(self):
        super(c198175, self).__init__(gameobject.Characteristics(**{'name': 'Totem-Guide Hartebeest', 'text': 'When this creature enters, you may search your library for an Aura card, reveal it, put it into your hand, then shuffle.', 'color': ['W'], 'mana_cost': '4W', 'power': 2, 'toughness': 5, 'subtype': ['Antelope']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9046228849(card.Card):
    "Totally Lost"
    def __init__(self):
        super(c9046228849, self).__init__(gameobject.Characteristics(**{'name': 'Totally Lost', 'text': "Put target nonland permanent on top of its owner's library.", 'color': ['U'], 'mana_cost': '4U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c239989(card.Card):
    "Tormentor's Trident"
    def __init__(self):
        super(c239989, self).__init__(gameobject.Characteristics(**{'name': "Tormentor's Trident", 'text': 'Equipped creature gets +3/+0 and attacks each combat if able.\nEquip {3}', 'color': [], 'mana_cost': '2', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c452869(card.Card):
    "Torch Courier"
    def __init__(self):
        super(c452869, self).__init__(gameobject.Characteristics(**{'name': 'Torch Courier', 'text': 'Haste\nSacrifice this creature: Another target creature gains haste until end of turn.', 'color': ['R'], 'mana_cost': 'R', 'power': 1, 'toughness': 1, 'subtype': ['Goblin']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c383414(card.Card):
    "Tireless Missionaries"
    def __init__(self):
        super(c383414, self).__init__(gameobject.Characteristics(**{'name': 'Tireless Missionaries', 'text': 'When this creature enters, you gain 3 life.', 'color': ['W'], 'mana_cost': '4W', 'power': 2, 'toughness': 3, 'subtype': ['Human', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c240048(card.Card):
    "Timberland Guide"
    def __init__(self):
        super(c240048, self).__init__(gameobject.Characteristics(**{'name': 'Timberland Guide', 'text': 'When this creature enters, put a +1/+1 counter on target creature.', 'color': ['G'], 'mana_cost': '1G', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Scout']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c429677(card.Card):
    "Timber Gorge"
    def __init__(self):
        super(c429677, self).__init__(gameobject.Characteristics(**{'name': 'Timber Gorge', 'text': 'This land enters tapped.\n{T}: Add {R} or {G}.', 'color': ['G', 'R'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c9623187383(card.Card):
    "Thunder Magic"
    def __init__(self):
        super(c9623187383, self).__init__(gameobject.Characteristics(**{'name': 'Thunder Magic', 'text': 'Tiered (Choose one additional cost.)\n• Thunder — {0} — Thunder Magic deals 2 damage to target creature.\n• Thundara — {3} — Thunder Magic deals 4 damage to target creature.\n• Thundaga — {5}{R} — Thunder Magic deals 8 damage to target creature.', 'color': ['R'], 'mana_cost': 'R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c240099(card.Card):
    "Thraben Valiant"
    def __init__(self):
        super(c240099, self).__init__(gameobject.Characteristics(**{'name': 'Thraben Valiant', 'text': 'Vigilance', 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance]))

class c230625(card.Card):
    "Thraben Purebloods"
    def __init__(self):
        super(c230625, self).__init__(gameobject.Characteristics(**{'name': 'Thraben Purebloods', 'text': '', 'color': ['W'], 'mana_cost': '4W', 'power': 3, 'toughness': 5, 'subtype': ['Dog']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452805(card.Card):
    "Thoughtbound Phantasm"
    def __init__(self):
        super(c452805, self).__init__(gameobject.Characteristics(**{'name': 'Thoughtbound Phantasm', 'text': "Defender\nWhenever you surveil, put a +1/+1 counter on this creature.\nAs long as this creature has three or more +1/+1 counters on it, it can attack as though it didn't have defender.", 'color': ['U'], 'mana_cost': 'U', 'power': 2, 'toughness': 2, 'subtype': ['Spirit']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c9288031746(card.Card):
    "The Final Days"
    def __init__(self):
        super(c9288031746, self).__init__(gameobject.Characteristics(**{'name': 'The Final Days', 'text': 'Create two tapped 2/2 black Horror creature tokens. If this spell was cast from a graveyard, instead create X of those tokens, where X is the number of creature cards in your graveyard.\nFlashback {4}{B}{B} (You may cast this card from your graveyard for its flashback cost. Then exile it.)', 'color': ['B'], 'mana_cost': '2BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c9428259143(card.Card):
    "The Crystal's Chosen"
    def __init__(self):
        super(c9428259143, self).__init__(gameobject.Characteristics(**{'name': "The Crystal's Chosen", 'text': 'Create four 1/1 colorless Hero creature tokens. Then put a +1/+1 counter on each creature you control.', 'color': ['W'], 'mana_cost': '5WW'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c74481(card.Card):
    "Terashi's Verdict"
    def __init__(self):
        super(c74481, self).__init__(gameobject.Characteristics(**{'name': "Terashi's Verdict", 'text': 'Destroy target attacking creature with power 3 or less.', 'color': ['W'], 'mana_cost': '1W', 'subtype': ['Arcane']}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452779(card.Card):
    "Tenth District Guard"
    def __init__(self):
        super(c452779, self).__init__(gameobject.Characteristics(**{'name': 'Tenth District Guard', 'text': 'When this creature enters, target creature gets +0/+1 until end of turn.', 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c253649(card.Card):
    "Tenement Crasher"
    def __init__(self):
        super(c253649, self).__init__(gameobject.Characteristics(**{'name': 'Tenement Crasher', 'text': 'Haste', 'color': ['R'], 'mana_cost': '5R', 'power': 5, 'toughness': 4, 'subtype': ['Beast']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c426018(card.Card):
    "Teleportal"
    def __init__(self):
        super(c426018, self).__init__(gameobject.Characteristics(**{'name': 'Teleportal', 'text': 'Target creature you control gets +1/+0 until end of turn and can\'t be blocked this turn.\nOverload {3}{U}{R} (You may cast this spell for its overload cost. If you do, change "target" in its text to "each.")', 'color': ['R', 'U'], 'mana_cost': 'UR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c489339(card.Card):
    "Talrand's Invocation"
    def __init__(self):
        super(c489339, self).__init__(gameobject.Characteristics(**{'name': "Talrand's Invocation", 'text': 'Create two 2/2 blue Drake creature tokens with flying.', 'color': ['U'], 'mana_cost': '2UU'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c452778(card.Card):
    "Take Heart"
    def __init__(self):
        super(c452778, self).__init__(gameobject.Characteristics(**{'name': 'Take Heart', 'text': 'Target creature gets +2/+2 until end of turn. You gain 1 life for each attacking creature you control.', 'color': ['W'], 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c9318770374(card.Card):
    "Syncopate"
    def __init__(self):
        super(c9318770374, self).__init__(gameobject.Characteristics(**{'name': 'Syncopate', 'text': "Counter target spell unless its controller pays {X}. If that spell is countered this way, exile it instead of putting it into its owner's graveyard.", 'color': ['U'], 'mana_cost': 'XU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c45190(card.Card):
    "Sword Dancer"
    def __init__(self):
        super(c45190, self).__init__(gameobject.Characteristics(**{'name': 'Sword Dancer', 'text': '{W}{W}: Target attacking creature gets -1/-0 until end of turn.', 'color': ['W'], 'mana_cost': '1W', 'power': 1, 'toughness': 2, 'subtype': ['Human', 'Rebel']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452952(card.Card):
    "Swathcutter Giant"
    def __init__(self):
        super(c452952, self).__init__(gameobject.Characteristics(**{'name': 'Swathcutter Giant', 'text': 'Vigilance\nWhenever this creature attacks, it deals 1 damage to each creature defending player controls.', 'color': ['R', 'W'], 'mana_cost': '4RW', 'power': 5, 'toughness': 5, 'subtype': ['Giant', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance]))

class c452951(card.Card):
    "Swarm Guildmage"
    def __init__(self):
        super(c452951, self).__init__(gameobject.Characteristics(**{'name': 'Swarm Guildmage', 'text': "{4}{B}, {T}: Creatures you control get +1/+0 and gain menace until end of turn. (They can't be blocked except by two or more creatures.)\n{1}{G}, {T}: You gain 2 life.", 'color': ['B', 'G'], 'mana_cost': 'BG', 'power': 2, 'toughness': 2, 'subtype': ['Elf', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c681244(card.Card):
    "Swamp"
    def __init__(self):
        super(c681244, self).__init__(gameobject.Characteristics(**{'name': 'Swamp', 'text': '({T}: Add {B}.)', 'color': ['B'], 'mana_cost': '', 'subtype': ['Swamp']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c270804(card.Card):
    "Survey the Wreckage"
    def __init__(self):
        super(c270804, self).__init__(gameobject.Characteristics(**{'name': 'Survey the Wreckage', 'text': 'Destroy target land. Create a 1/1 red Goblin creature token.', 'color': ['R'], 'mana_cost': '4R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c87904(card.Card):
    "Surveilling Sprite"
    def __init__(self):
        super(c87904, self).__init__(gameobject.Characteristics(**{'name': 'Surveilling Sprite', 'text': 'Flying\nWhen this creature dies, you may draw a card.', 'color': ['U'], 'mana_cost': '1U', 'power': 1, 'toughness': 1, 'subtype': ['Faerie', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c9212814949(card.Card):
    "Suplex"
    def __init__(self):
        super(c9212814949, self).__init__(gameobject.Characteristics(**{'name': 'Suplex', 'text': 'Choose one —\n• Suplex deals 3 damage to target creature. If that creature would die this turn, exile it instead.\n• Exile target artifact.', 'color': ['R'], 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c177551(card.Card):
    "Sunspring Expedition"
    def __init__(self):
        super(c177551, self).__init__(gameobject.Characteristics(**{'name': 'Sunspring Expedition', 'text': 'Landfall — Whenever a land you control enters, you may put a quest counter on this enchantment.\nRemove three quest counters from this enchantment and sacrifice it: You gain 8 life.', 'color': ['W'], 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c452776(card.Card):
    "Sunhome Stalwart"
    def __init__(self):
        super(c452776, self).__init__(gameobject.Characteristics(**{'name': 'Sunhome Stalwart', 'text': 'First strike (This creature deals combat damage before creatures without first strike.)\nMentor (Whenever this creature attacks, put a +1/+1 counter on target attacking creature with lesser power.)', 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.First_Strike]))

class c452950(card.Card):
    "Sumala Woodshaper"
    def __init__(self):
        super(c452950, self).__init__(gameobject.Characteristics(**{'name': 'Sumala Woodshaper', 'text': 'When this creature enters, look at the top four cards of your library. You may reveal a creature or enchantment card from among them and put it into your hand. Put the rest on the bottom of your library in a random order.', 'color': ['G', 'W'], 'mana_cost': '2GW', 'power': 2, 'toughness': 1, 'subtype': ['Elf', 'Druid']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c407688(card.Card):
    "Submerged Boneyard"
    def __init__(self):
        super(c407688, self).__init__(gameobject.Characteristics(**{'name': 'Submerged Boneyard', 'text': 'This land enters tapped.\n{T}: Add {U} or {B}.', 'color': ['B', 'U'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c452867(card.Card):
    "Street Riot"
    def __init__(self):
        super(c452867, self).__init__(gameobject.Characteristics(**{'name': 'Street Riot', 'text': 'During your turn, creatures you control get +1/+0 and have trample.', 'color': ['R'], 'mana_cost': '4R'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c446856(card.Card):
    "Stoneshock Giant"
    def __init__(self):
        super(c446856, self).__init__(gameobject.Characteristics(**{'name': 'Stoneshock Giant', 'text': "{6}{R}{R}: Monstrosity 3. (If this creature isn't monstrous, put three +1/+1 counters on it and it becomes monstrous.)\nWhen this creature becomes monstrous, creatures without flying your opponents control can't block this turn.", 'color': ['R'], 'mana_cost': '3RR', 'power': 5, 'toughness': 4, 'subtype': ['Giant']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c470822(card.Card):
    "Stone Quarry"
    def __init__(self):
        super(c470822, self).__init__(gameobject.Characteristics(**{'name': 'Stone Quarry', 'text': 'This land enters tapped.\n{T}: Add {R} or {W}.', 'color': ['R', 'W'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c426812(card.Card):
    "Stir the Sands"
    def __init__(self):
        super(c426812, self).__init__(gameobject.Characteristics(**{'name': 'Stir the Sands', 'text': 'Create three 2/2 black Zombie creature tokens.\nCycling {3}{B} ({3}{B}, Discard this card: Draw a card.)\nWhen you cycle this card, create a 2/2 black Zombie creature token.', 'color': ['B'], 'mana_cost': '4BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c452980(card.Card):
    "Status"
    def __init__(self):
        super(c452980, self).__init__(gameobject.Characteristics(**{'name': 'Status', 'text': '', 'color': ['B', 'G'], 'mana_cost': 'B/G // 2BG'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c50138(card.Card):
    "Stand Firm"
    def __init__(self):
        super(c50138, self).__init__(gameobject.Characteristics(**{'name': 'Stand Firm', 'text': 'Target creature gets +1/+1 until end of turn. Scry 2. (Look at the top two cards of your library, then put any number of them on the bottom and the rest on top in any order.)', 'color': ['W'], 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452895(card.Card):
    "Sprouting Renewal"
    def __init__(self):
        super(c452895, self).__init__(gameobject.Characteristics(**{'name': 'Sprouting Renewal', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nChoose one —\n• Create a 2/2 green and white Elf Knight creature token with vigilance.\n• Destroy target artifact or enchantment.", 'color': ['G'], 'mana_cost': '2G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[static_abilities.StaticAbilities.Convoke]))

class c426921(card.Card):
    "Spring"
    def __init__(self):
        super(c426921, self).__init__(gameobject.Characteristics(**{'name': 'Spring', 'text': '', 'color': ['G', 'U'], 'mana_cost': '2G // 4UU'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c265381(card.Card):
    "Splatter Thug"
    def __init__(self):
        super(c265381, self).__init__(gameobject.Characteristics(**{'name': 'Splatter Thug', 'text': "First strike\nUnleash (You may have this creature enter with a +1/+1 counter on it. It can't block as long as it has a +1/+1 counter on it.)", 'color': ['R'], 'mana_cost': '2R', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.First_Strike]))

class c366236(card.Card):
    "Spire Tracer"
    def __init__(self):
        super(c366236, self).__init__(gameobject.Characteristics(**{'name': 'Spire Tracer', 'text': "This creature can't be blocked except by creatures with flying or reach.", 'color': ['G'], 'mana_cost': 'G', 'power': 1, 'toughness': 1, 'subtype': ['Elf', 'Scout']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452836(card.Card):
    "Spinal Centipede"
    def __init__(self):
        super(c452836, self).__init__(gameobject.Characteristics(**{'name': 'Spinal Centipede', 'text': 'When this creature dies, put a +1/+1 counter on target creature you control.', 'color': ['B'], 'mana_cost': '2B', 'power': 3, 'toughness': 2, 'subtype': ['Insect']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c230618(card.Card):
    "Spare from Evil"
    def __init__(self):
        super(c230618, self).__init__(gameobject.Characteristics(**{'name': 'Spare from Evil', 'text': 'Creatures you control gain protection from non-Human creatures until end of turn.', 'color': ['W'], 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c265372(card.Card):
    "Soul Tithe"
    def __init__(self):
        super(c265372, self).__init__(gameobject.Characteristics(**{'name': 'Soul Tithe', 'text': "Enchant nonland permanent\nAt the beginning of the upkeep of enchanted permanent's controller, that player sacrifices it unless they pay {X}, where X is its mana value.", 'color': ['W'], 'mana_cost': '1W', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c240028(card.Card):
    "Somberwald Vigilante"
    def __init__(self):
        super(c240028, self).__init__(gameobject.Characteristics(**{'name': 'Somberwald Vigilante', 'text': 'Whenever this creature becomes blocked by a creature, this creature deals 1 damage to that creature.', 'color': ['R'], 'mana_cost': 'R', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c446075(card.Card):
    "Solemn Offering"
    def __init__(self):
        super(c446075, self).__init__(gameobject.Characteristics(**{'name': 'Solemn Offering', 'text': 'Destroy target artifact or enchantment. You gain 4 life.', 'color': ['W'], 'mana_cost': '2W'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c452866(card.Card):
    "Smelt-Ward Minotaur"
    def __init__(self):
        super(c452866, self).__init__(gameobject.Characteristics(**{'name': 'Smelt-Ward Minotaur', 'text': "Whenever you cast an instant or sorcery spell, target creature an opponent controls can't block this turn.", 'color': ['R'], 'mana_cost': '2R', 'power': 2, 'toughness': 3, 'subtype': ['Minotaur', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c423739(card.Card):
    "Sly Requisitioner"
    def __init__(self):
        super(c423739, self).__init__(gameobject.Characteristics(**{'name': 'Sly Requisitioner', 'text': "Improvise (Your artifacts can help cast this spell. Each artifact you tap after you're done activating mana abilities pays for {1}.)\nWhenever a nontoken artifact you control is put into a graveyard from the battlefield, create a 1/1 colorless Servo artifact creature token.", 'color': ['B'], 'mana_cost': '4B', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Artificer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Improvise]))

class c425962(card.Card):
    "Slime Molding"
    def __init__(self):
        super(c425962, self).__init__(gameobject.Characteristics(**{'name': 'Slime Molding', 'text': 'Create an X/X green Ooze creature token.', 'color': ['G'], 'mana_cost': 'XG'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c452775(card.Card):
    "Skyline Scout"
    def __init__(self):
        super(c452775, self).__init__(gameobject.Characteristics(**{'name': 'Skyline Scout', 'text': 'Whenever this creature attacks, you may pay {1}{W}. If you do, it gains flying until end of turn.', 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Scout']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c289212(card.Card):
    "Skyline Predator"
    def __init__(self):
        super(c289212, self).__init__(gameobject.Characteristics(**{'name': 'Skyline Predator', 'text': 'Flash (You may cast this spell any time you could cast an instant.)\nFlying', 'color': ['U'], 'mana_cost': '4UU', 'power': 3, 'toughness': 4, 'subtype': ['Drake']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Flash]))

class c366338(card.Card):
    "Skyknight Legionnaire"
    def __init__(self):
        super(c366338, self).__init__(gameobject.Characteristics(**{'name': 'Skyknight Legionnaire', 'text': 'Flying, haste', 'color': ['R', 'W'], 'mana_cost': '1RW', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Knight']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Haste]))

class c366238(card.Card):
    "Skullcrack"
    def __init__(self):
        super(c366238, self).__init__(gameobject.Characteristics(**{'name': 'Skullcrack', 'text': "Players can't gain life this turn. Damage can't be prevented this turn. Skullcrack deals 3 damage to target player or planeswalker.", 'color': ['R'], 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c262877(card.Card):
    "Skillful Lunge"
    def __init__(self):
        super(c262877, self).__init__(gameobject.Characteristics(**{'name': 'Skillful Lunge', 'text': 'Target creature gets +2/+0 and gains first strike until end of turn.', 'color': ['W'], 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c366350(card.Card):
    "Skarrg Guildmage"
    def __init__(self):
        super(c366350, self).__init__(gameobject.Characteristics(**{'name': 'Skarrg Guildmage', 'text': "{R}{G}: Creatures you control gain trample until end of turn.\n{1}{R}{G}: Target land you control becomes a 4/4 Elemental creature until end of turn. It's still a land.", 'color': ['G', 'R'], 'mana_cost': 'RG', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c262876(card.Card):
    "Silverclaw Griffin"
    def __init__(self):
        super(c262876, self).__init__(gameobject.Characteristics(**{'name': 'Silverclaw Griffin', 'text': 'Flying, first strike', 'color': ['W'], 'mana_cost': '3WW', 'power': 3, 'toughness': 2, 'subtype': ['Griffin']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.First_Strike]))

class c485560(card.Card):
    "Silent Dart"
    def __init__(self):
        super(c485560, self).__init__(gameobject.Characteristics(**{'name': 'Silent Dart', 'text': '{4}, {T}, Sacrifice this artifact: It deals 3 damage to target creature.', 'color': [], 'mana_cost': '1'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c373573(card.Card):
    "Silent Artisan"
    def __init__(self):
        super(c373573, self).__init__(gameobject.Characteristics(**{'name': 'Silent Artisan', 'text': '', 'color': ['W'], 'mana_cost': '3WW', 'power': 3, 'toughness': 5, 'subtype': ['Giant']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c423766(card.Card):
    "Siege Modification"
    def __init__(self):
        super(c423766, self).__init__(gameobject.Characteristics(**{'name': 'Siege Modification', 'text': "Enchant creature or Vehicle\nAs long as enchanted permanent is a Vehicle, it's a creature in addition to its other types.\nEnchanted creature gets +3/+0 and has first strike.", 'color': ['R'], 'mana_cost': '1RR', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c469865(card.Card):
    "Siege Mastodon"
    def __init__(self):
        super(c469865, self).__init__(gameobject.Characteristics(**{'name': 'Siege Mastodon', 'text': '', 'color': ['W'], 'mana_cost': '4W', 'power': 3, 'toughness': 5, 'subtype': ['Elephant']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c217994(card.Card):
    "Shriek Raptor"
    def __init__(self):
        super(c217994, self).__init__(gameobject.Characteristics(**{'name': 'Shriek Raptor', 'text': 'Flying\nInfect (This creature deals damage to creatures in the form of -1/-1 counters and to players in the form of poison counters.)', 'color': ['W'], 'mana_cost': '3WW', 'power': 2, 'toughness': 3, 'subtype': ['Phyrexian', 'Bird']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Infect]))

class c9868402489(card.Card):
    "Shipwreck Singer"
    def __init__(self):
        super(c9868402489, self).__init__(gameobject.Characteristics(**{'name': 'Shipwreck Singer', 'text': 'Flying\n{1}{U}: Target creature an opponent controls attacks this turn if able.\n{1}{B}, {T}: Attacking creatures get -1/-1 until end of turn.', 'color': ['B', 'U'], 'mana_cost': 'UB', 'power': 1, 'toughness': 2, 'subtype': ['Siren']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c366332(card.Card):
    "Shielded Passage"
    def __init__(self):
        super(c366332, self).__init__(gameobject.Characteristics(**{'name': 'Shielded Passage', 'text': 'Prevent all damage that would be dealt to target creature this turn.', 'color': ['W'], 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c423711(card.Card):
    "Shielded Aether Thief"
    def __init__(self):
        super(c423711, self).__init__(gameobject.Characteristics(**{'name': 'Shielded Aether Thief', 'text': 'Flash (You may cast this spell any time you could cast an instant.)\nWhenever this creature blocks, you get {E} (an energy counter).\n{T}, Pay {E}{E}{E}: Draw a card.', 'color': ['U'], 'mana_cost': '1U', 'power': 0, 'toughness': 4, 'subtype': ['Vedalken', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash]))

class c366307(card.Card):
    "Shadow Alley Denizen"
    def __init__(self):
        super(c366307, self).__init__(gameobject.Characteristics(**{'name': 'Shadow Alley Denizen', 'text': "Whenever another black creature you control enters, target creature gains intimidate until end of turn. (It can't be blocked except by artifact creatures and/or creatures that share a color with it.)", 'color': ['B'], 'mana_cost': 'B', 'power': 1, 'toughness': 1, 'subtype': ['Vampire', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373574(card.Card):
    "Setessan Griffin"
    def __init__(self):
        super(c373574, self).__init__(gameobject.Characteristics(**{'name': 'Setessan Griffin', 'text': 'Flying\n{2}{G}{G}: This creature gets +2/+2 until end of turn. Activate only once each turn.', 'color': ['G', 'W'], 'mana_cost': '4W', 'power': 3, 'toughness': 2, 'subtype': ['Griffin']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c394051(card.Card):
    "Serra Angel"
    def __init__(self):
        super(c394051, self).__init__(gameobject.Characteristics(**{'name': 'Serra Angel', 'text': "Flying\nVigilance (Attacking doesn't cause this creature to tap.)", 'color': ['W'], 'mana_cost': '3WW', 'power': 4, 'toughness': 4, 'subtype': ['Angel']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Vigilance]))

class c373697(card.Card):
    "Sentry of the Underworld"
    def __init__(self):
        super(c373697, self).__init__(gameobject.Characteristics(**{'name': 'Sentry of the Underworld', 'text': 'Flying, vigilance\n{W}{B}, Pay 3 life: Regenerate this creature.', 'color': ['B', 'W'], 'mana_cost': '3WB', 'power': 3, 'toughness': 3, 'subtype': ['Griffin', 'Skeleton']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Vigilance]))

class c370813(card.Card):
    "Sentinel Sliver"
    def __init__(self):
        super(c370813, self).__init__(gameobject.Characteristics(**{'name': 'Sentinel Sliver', 'text': "Sliver creatures you control have vigilance. (Attacking doesn't cause them to tap.)", 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 2, 'subtype': ['Sliver']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9967693117(card.Card):
    "Sensor Splicer"
    def __init__(self):
        super(c9967693117, self).__init__(gameobject.Characteristics(**{'name': 'Sensor Splicer', 'text': 'When this creature enters, create a 3/3 colorless Phyrexian Golem artifact creature token.\nGolem creatures you control have vigilance.', 'color': ['W'], 'mana_cost': '4W', 'power': 1, 'toughness': 1, 'subtype': ['Phyrexian', 'Artificer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9986311948(card.Card):
    "Self-Destruct"
    def __init__(self):
        super(c9986311948, self).__init__(gameobject.Characteristics(**{'name': 'Self-Destruct', 'text': 'Target creature you control deals X damage to any other target and X damage to itself, where X is its power.', 'color': ['R'], 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452990(card.Card):
    "Selesnya Locket"
    def __init__(self):
        super(c452990, self).__init__(gameobject.Characteristics(**{'name': 'Selesnya Locket', 'text': '{T}: Add {G} or {W}.\n{G/W}{G/W}{G/W}{G/W}, {T}, Sacrifice this artifact: Draw two cards.', 'color': ['G', 'W'], 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c376489(card.Card):
    "Selesnya Charm"
    def __init__(self):
        super(c376489, self).__init__(gameobject.Characteristics(**{'name': 'Selesnya Charm', 'text': 'Choose one —\n• Target creature gets +2/+2 and gains trample until end of turn.\n• Exile target creature with power 5 or greater.\n• Create a 2/2 white Knight creature token with vigilance.', 'color': ['G', 'W'], 'mana_cost': 'GW'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452803(card.Card):
    "Selective Snare"
    def __init__(self):
        super(c452803, self).__init__(gameobject.Characteristics(**{'name': 'Selective Snare', 'text': "Return X target creatures of the creature type of your choice to their owner's hand.", 'color': ['U'], 'mana_cost': 'XU'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c9753748276(card.Card):
    "Seek the Horizon"
    def __init__(self):
        super(c9753748276, self).__init__(gameobject.Characteristics(**{'name': 'Seek the Horizon', 'text': 'Search your library for up to three basic land cards, reveal them, put them into your hand, then shuffle.', 'color': ['G'], 'mana_cost': '3G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c270790(card.Card):
    "Security Blockade"
    def __init__(self):
        super(c270790, self).__init__(gameobject.Characteristics(**{'name': 'Security Blockade', 'text': 'Enchant land\nWhen this Aura enters, create a 2/2 white Knight creature token with vigilance.\nEnchanted land has "{T}: Prevent the next 1 damage that would be dealt to you this turn."', 'color': ['W'], 'mana_cost': '2W', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c430595(card.Card):
    "Searing Spear"
    def __init__(self):
        super(c430595, self).__init__(gameobject.Characteristics(**{'name': 'Searing Spear', 'text': 'Searing Spear deals 3 damage to any target.', 'color': ['R'], 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c9637558346(card.Card):
    "Scroll Thief"
    def __init__(self):
        super(c9637558346, self).__init__(gameobject.Characteristics(**{'name': 'Scroll Thief', 'text': 'Whenever this creature deals combat damage to a player, draw a card.', 'color': ['U'], 'mana_cost': '2U', 'power': 1, 'toughness': 3, 'subtype': ['Merfolk', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c423764(card.Card):
    "Scrapper Champion"
    def __init__(self):
        super(c423764, self).__init__(gameobject.Characteristics(**{'name': 'Scrapper Champion', 'text': 'Double strike (This creature deals both first-strike and regular combat damage.)\nWhen this creature enters, you get {E}{E} (two energy counters).\nWhenever this creature attacks, you may pay {E}{E}. If you do, put a +1/+1 counter on it.', 'color': ['R'], 'mana_cost': '3R', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Artificer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Double_Strike]))

class c373692(card.Card):
    "Scholar of Athreos"
    def __init__(self):
        super(c373692, self).__init__(gameobject.Characteristics(**{'name': 'Scholar of Athreos', 'text': '{2}{B}: Each opponent loses 1 life. You gain life equal to the life lost this way.', 'color': ['B', 'W'], 'mana_cost': '2W', 'power': 1, 'toughness': 4, 'subtype': ['Human', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c265388(card.Card):
    "Savage Surge"
    def __init__(self):
        super(c265388, self).__init__(gameobject.Characteristics(**{'name': 'Savage Surge', 'text': 'Target creature gets +2/+2 until end of turn. Untap that creature.', 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c373728(card.Card):
    "Satyr Piper"
    def __init__(self):
        super(c373728, self).__init__(gameobject.Characteristics(**{'name': 'Satyr Piper', 'text': '{3}{G}: Target creature must be blocked this turn if able.', 'color': ['G'], 'mana_cost': '2G', 'power': 2, 'toughness': 1, 'subtype': ['Satyr', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373744(card.Card):
    "Satyr Hedonist"
    def __init__(self):
        super(c373744, self).__init__(gameobject.Characteristics(**{'name': 'Satyr Hedonist', 'text': '{R}, Sacrifice this creature: Add {R}{R}{R}.', 'color': ['G', 'R'], 'mana_cost': '1G', 'power': 2, 'toughness': 1, 'subtype': ['Satyr']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c176438(card.Card):
    "Sangrite Surge"
    def __init__(self):
        super(c176438, self).__init__(gameobject.Characteristics(**{'name': 'Sangrite Surge', 'text': 'Target creature gets +3/+3 and gains double strike until end of turn.', 'color': ['G', 'R'], 'mana_cost': '4RG'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c9985812734(card.Card):
    "Samurai's Katana"
    def __init__(self):
        super(c9985812734, self).__init__(gameobject.Characteristics(**{'name': "Samurai's Katana", 'text': 'Job select (When this Equipment enters, create a 1/1 colorless Hero creature token, then attach this to it.)\nEquipped creature gets +2/+2, has trample and haste, and is a Samurai in addition to its other types.\nMurasame — Equip {5}', 'color': ['R'], 'mana_cost': '2R', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c423710(card.Card):
    "Salvage Scuttler"
    def __init__(self):
        super(c423710, self).__init__(gameobject.Characteristics(**{'name': 'Salvage Scuttler', 'text': "Whenever this creature attacks, return an artifact you control to its owner's hand.", 'color': ['U'], 'mana_cost': '4U', 'power': 4, 'toughness': 4, 'subtype': ['Crab']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c426807(card.Card):
    "Ruthless Sniper"
    def __init__(self):
        super(c426807, self).__init__(gameobject.Characteristics(**{'name': 'Ruthless Sniper', 'text': 'Whenever you cycle or discard a card, you may pay {1}. If you do, put a -1/-1 counter on target creature.', 'color': ['B'], 'mana_cost': 'B', 'power': 1, 'toughness': 2, 'subtype': ['Human', 'Archer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9185973936(card.Card):
    "Rubblebelt Maaka"
    def __init__(self):
        super(c9185973936, self).__init__(gameobject.Characteristics(**{'name': 'Rubblebelt Maaka', 'text': 'Bloodrush — {R}, Discard this card: Target attacking creature gets +3/+3 until end of turn.', 'color': ['R'], 'mana_cost': '3R', 'power': 3, 'toughness': 3, 'subtype': ['Cat']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9543504498(card.Card):
    "Rosemane Centaur"
    def __init__(self):
        super(c9543504498, self).__init__(gameobject.Characteristics(**{'name': 'Rosemane Centaur', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nVigilance", 'color': ['G', 'W'], 'mana_cost': '3GW', 'power': 4, 'toughness': 4, 'subtype': ['Centaur', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance, static_abilities.StaticAbilities.Convoke]))

class c452774(card.Card):
    "Roc Charger"
    def __init__(self):
        super(c452774, self).__init__(gameobject.Characteristics(**{'name': 'Roc Charger', 'text': 'Flying\nWhenever this creature attacks, target attacking creature without flying gains flying until end of turn.', 'color': ['W'], 'mana_cost': '2W', 'power': 1, 'toughness': 3, 'subtype': ['Bird']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c270351(card.Card):
    "Rix Maadi Guildmage"
    def __init__(self):
        super(c270351, self).__init__(gameobject.Characteristics(**{'name': 'Rix Maadi Guildmage', 'text': '{B}{R}: Target blocking creature gets -1/-1 until end of turn.\n{B}{R}: Target player who lost life this turn loses 1 life.', 'color': ['B', 'R'], 'mana_cost': 'BR', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c289219(card.Card):
    "Rites of Reaping"
    def __init__(self):
        super(c289219, self).__init__(gameobject.Characteristics(**{'name': 'Rites of Reaping', 'text': 'Target creature gets +3/+3 until end of turn. Another target creature gets -3/-3 until end of turn.', 'color': ['B', 'G'], 'mana_cost': '4BG'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c290530(card.Card):
    "Risen Sanctuary"
    def __init__(self):
        super(c290530, self).__init__(gameobject.Characteristics(**{'name': 'Risen Sanctuary', 'text': 'Vigilance', 'color': ['G', 'W'], 'mana_cost': '5GW', 'power': 8, 'toughness': 8, 'subtype': ['Elemental']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance]))

class c368979(card.Card):
    "Riot Control"
    def __init__(self):
        super(c368979, self).__init__(gameobject.Characteristics(**{'name': 'Riot Control', 'text': 'You gain 1 life for each creature your opponents control. Prevent all damage that would be dealt to you this turn.', 'color': ['W'], 'mana_cost': '2W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c21023(card.Card):
    "Righteous Charge"
    def __init__(self):
        super(c21023, self).__init__(gameobject.Characteristics(**{'name': 'Righteous Charge', 'text': 'Creatures you control get +2/+2 until end of turn.', 'color': ['W'], 'mana_cost': '1WW'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c452773(card.Card):
    "Righteous Blow"
    def __init__(self):
        super(c452773, self).__init__(gameobject.Characteristics(**{'name': 'Righteous Blow', 'text': 'Righteous Blow deals 2 damage to target attacking or blocking creature.', 'color': ['W'], 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452946(card.Card):
    "Rhizome Lurcher"
    def __init__(self):
        super(c452946, self).__init__(gameobject.Characteristics(**{'name': 'Rhizome Lurcher', 'text': 'Undergrowth — This creature enters with a number of +1/+1 counters on it equal to the number of creature cards in your graveyard.', 'color': ['B', 'G'], 'mana_cost': '2BG', 'power': 2, 'toughness': 2, 'subtype': ['Fungus', 'Zombie']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c423688(card.Card):
    "Restoration Specialist"
    def __init__(self):
        super(c423688, self).__init__(gameobject.Characteristics(**{'name': 'Restoration Specialist', 'text': '{W}, Sacrifice this creature: Return up to one target artifact card and up to one target enchantment card from your graveyard to your hand.', 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 1, 'subtype': ['Dwarf', 'Artificer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c194930(card.Card):
    "Repel the Darkness"
    def __init__(self):
        super(c194930, self).__init__(gameobject.Characteristics(**{'name': 'Repel the Darkness', 'text': 'Tap up to two target creatures.\nDraw a card.', 'color': ['W'], 'mana_cost': '2W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c423800(card.Card):
    "Renegade Rallier"
    def __init__(self):
        super(c423800, self).__init__(gameobject.Characteristics(**{'name': 'Renegade Rallier', 'text': 'Revolt — When this creature enters, if a permanent left the battlefield under your control this turn, return target permanent card with mana value 2 or less from your graveyard to the battlefield.', 'color': ['G', 'W'], 'mana_cost': '1GW', 'power': 3, 'toughness': 2, 'subtype': ['Human', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9660168104(card.Card):
    "Relm's Sketching"
    def __init__(self):
        super(c9660168104, self).__init__(gameobject.Characteristics(**{'name': "Relm's Sketching", 'text': "Create a token that's a copy of target artifact, creature, or land.", 'color': ['U'], 'mana_cost': '2UU'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c9509947300(card.Card):
    "Relentless X-ATM092"
    def __init__(self):
        super(c9509947300, self).__init__(gameobject.Characteristics(**{'name': 'Relentless X-ATM092', 'text': "This creature can't be blocked except by three or more creatures.\n{8}: Return this card from your graveyard to the battlefield tapped with a finality counter on it. (If a creature with a finality counter on it would die, exile it instead.)", 'color': [], 'mana_cost': '6', 'power': 6, 'toughness': 5, 'subtype': ['Robot', 'Spider']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[]))

class c426918(card.Card):
    "Reduce"
    def __init__(self):
        super(c426918, self).__init__(gameobject.Characteristics(**{'name': 'Reduce', 'text': '', 'color': ['R', 'U'], 'mana_cost': '2U // 2R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c423762(card.Card):
    "Reckless Racer"
    def __init__(self):
        super(c423762, self).__init__(gameobject.Characteristics(**{'name': 'Reckless Racer', 'text': 'First strike\nWhenever this creature becomes tapped, you may discard a card. If you do, draw a card.', 'color': ['R'], 'mana_cost': '2R', 'power': 2, 'toughness': 3, 'subtype': ['Human', 'Pilot']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.First_Strike]))

class c253715(card.Card):
    "Reckless Brute"
    def __init__(self):
        super(c253715, self).__init__(gameobject.Characteristics(**{'name': 'Reckless Brute', 'text': 'Haste (This creature can attack and {T} as soon as it comes under your control.)\nThis creature attacks each combat if able.', 'color': ['R'], 'mana_cost': '2R', 'power': 3, 'toughness': 1, 'subtype': ['Ogre', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c373739(card.Card):
    "Ray of Dissolution"
    def __init__(self):
        super(c373739, self).__init__(gameobject.Characteristics(**{'name': 'Ray of Dissolution', 'text': 'Destroy target enchantment. You gain 3 life.', 'color': ['W'], 'mana_cost': '2W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c423761(card.Card):
    "Ravenous Intruder"
    def __init__(self):
        super(c423761, self).__init__(gameobject.Characteristics(**{'name': 'Ravenous Intruder', 'text': 'Sacrifice an artifact: This creature gets +2/+2 until end of turn.', 'color': ['R'], 'mana_cost': '1R', 'power': 1, 'toughness': 2, 'subtype': ['Gremlin']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452989(card.Card):
    "Rampaging Monument"
    def __init__(self):
        super(c452989, self).__init__(gameobject.Characteristics(**{'name': 'Rampaging Monument', 'text': 'Trample\nThis creature enters with three +1/+1 counters on it.\nWhenever you cast a multicolored spell, put a +1/+1 counter on this creature.', 'color': [], 'mana_cost': '4', 'power': 0, 'toughness': 0, 'subtype': ['Cleric']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample]))

class c253585(card.Card):
    "Rakdos Ringleader"
    def __init__(self):
        super(c253585, self).__init__(gameobject.Characteristics(**{'name': 'Rakdos Ringleader', 'text': 'First strike\nWhenever this creature deals combat damage to a player, that player discards a card at random.\n{B}: Regenerate this creature.', 'color': ['B', 'R'], 'mana_cost': '4BR', 'power': 3, 'toughness': 1, 'subtype': ['Skeleton', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.First_Strike]))

class c290525(card.Card):
    "Rakdos Ragemutt"
    def __init__(self):
        super(c290525, self).__init__(gameobject.Characteristics(**{'name': 'Rakdos Ragemutt', 'text': 'Lifelink, haste', 'color': ['B', 'R'], 'mana_cost': '3BR', 'power': 3, 'toughness': 3, 'subtype': ['Elemental', 'Dog']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Lifelink, static_abilities.StaticAbilities.Haste]))

class c470813(card.Card):
    "Rakdos Guildgate"
    def __init__(self):
        super(c470813, self).__init__(gameobject.Characteristics(**{'name': 'Rakdos Guildgate', 'text': 'This land enters tapped.\n{T}: Add {B} or {R}.', 'color': ['B', 'R'], 'mana_cost': '', 'subtype': ['Gate']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c253596(card.Card):
    "Rakdos Cackler"
    def __init__(self):
        super(c253596, self).__init__(gameobject.Characteristics(**{'name': 'Rakdos Cackler', 'text': "Unleash (You may have this creature enter with a +1/+1 counter on it. It can't block as long as it has a +1/+1 counter on it.)", 'color': ['B', 'R'], 'mana_cost': 'B/R', 'power': 1, 'toughness': 1, 'subtype': ['Devil']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c43622(card.Card):
    "Rain of Blades"
    def __init__(self):
        super(c43622, self).__init__(gameobject.Characteristics(**{'name': 'Rain of Blades', 'text': 'Rain of Blades deals 1 damage to each attacking creature.', 'color': ['W'], 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c222921(card.Card):
    "Rage Thrower"
    def __init__(self):
        super(c222921, self).__init__(gameobject.Characteristics(**{'name': 'Rage Thrower', 'text': 'Whenever another creature dies, this creature deals 2 damage to target player or planeswalker.', 'color': ['R'], 'mana_cost': '5R', 'power': 4, 'toughness': 2, 'subtype': ['Human', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452802(card.Card):
    "Radical Idea"
    def __init__(self):
        super(c452802, self).__init__(gameobject.Characteristics(**{'name': 'Radical Idea', 'text': 'Draw a card.\nJump-start (You may cast this card from your graveyard by discarding a card in addition to paying its other costs. Then exile this card.)', 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c265390(card.Card):
    "Pursuit of Flight"
    def __init__(self):
        super(c265390, self).__init__(gameobject.Characteristics(**{'name': 'Pursuit of Flight', 'text': 'Enchant creature\nEnchanted creature gets +2/+2 and has "{U}: This creature gains flying until end of turn."', 'color': ['R', 'U'], 'mana_cost': '1R', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c373505(card.Card):
    "Purphoros's Emissary"
    def __init__(self):
        super(c373505, self).__init__(gameobject.Characteristics(**{'name': "Purphoros's Emissary", 'text': "Bestow {6}{R} (If you cast this card for its bestow cost, it's an Aura spell with enchant creature. It becomes a creature again if it's not attached.)\nMenace (This creature can't be blocked except by two or more creatures.)\nEnchanted creature gets +3/+3 and has menace.", 'color': ['R'], 'mana_cost': '3R', 'power': 3, 'toughness': 3, 'subtype': ['Ox']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Menace]))

class c366296(card.Card):
    "Psychic Strike"
    def __init__(self):
        super(c366296, self).__init__(gameobject.Characteristics(**{'name': 'Psychic Strike', 'text': 'Counter target spell. Its controller mills two cards.', 'color': ['B', 'U'], 'mana_cost': '1UB'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c213814(card.Card):
    "Priests of Norn"
    def __init__(self):
        super(c213814, self).__init__(gameobject.Characteristics(**{'name': 'Priests of Norn', 'text': 'Vigilance\nInfect (This creature deals damage to creatures in the form of -1/-1 counters and to players in the form of poison counters.)', 'color': ['W'], 'mana_cost': '2W', 'power': 1, 'toughness': 4, 'subtype': ['Phyrexian', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance, static_abilities.StaticAbilities.Infect]))

class c452833(card.Card):
    "Price of Fame"
    def __init__(self):
        super(c452833, self).__init__(gameobject.Characteristics(**{'name': 'Price of Fame', 'text': 'This spell costs {2} less to cast if it targets a legendary creature.\nDestroy target creature.\nSurveil 2. (Look at the top two cards of your library, then put any number of them into your graveyard and the rest on top of your library in any order.)', 'color': ['B'], 'mana_cost': '3B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c9312848528(card.Card):
    "Prey Upon"
    def __init__(self):
        super(c9312848528, self).__init__(gameobject.Characteristics(**{'name': 'Prey Upon', 'text': "Target creature you control fights target creature you don't control. (Each deals damage equal to its power to the other.)", 'color': ['G'], 'mana_cost': 'G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c370745(card.Card):
    "Predatory Sliver"
    def __init__(self):
        super(c370745, self).__init__(gameobject.Characteristics(**{'name': 'Predatory Sliver', 'text': 'Sliver creatures you control get +1/+1.', 'color': ['G'], 'mana_cost': '1G', 'power': 1, 'toughness': 1, 'subtype': ['Sliver']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c476400(card.Card):
    "Portent of Betrayal"
    def __init__(self):
        super(c476400, self).__init__(gameobject.Characteristics(**{'name': 'Portent of Betrayal', 'text': 'Gain control of target creature until end of turn. Untap that creature. It gains haste until end of turn. Scry 1. (Look at the top card of your library. You may put that card on the bottom.)', 'color': ['R'], 'mana_cost': '3R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c485518(card.Card):
    "Portcullis Vine"
    def __init__(self):
        super(c485518, self).__init__(gameobject.Characteristics(**{'name': 'Portcullis Vine', 'text': "Defender (This creature can't attack.)\n{2}, {T}, Sacrifice a creature with defender: Draw a card.", 'color': ['G'], 'mana_cost': 'G', 'power': 0, 'toughness': 3, 'subtype': ['Plant', 'Wall']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c9294044681(card.Card):
    "Poison the Waters"
    def __init__(self):
        super(c9294044681, self).__init__(gameobject.Characteristics(**{'name': 'Poison the Waters', 'text': 'Choose one —\n• All creatures get -1/-1 until end of turn.\n• Target player reveals their hand. You choose an artifact or creature card from it. That player discards that card.', 'color': ['B'], 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c9856344946(card.Card):
    "Plummet"
    def __init__(self):
        super(c9856344946, self).__init__(gameobject.Characteristics(**{'name': 'Plummet', 'text': 'Destroy target creature with flying.', 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c681236(card.Card):
    "Plains"
    def __init__(self):
        super(c681236, self).__init__(gameobject.Characteristics(**{'name': 'Plains', 'text': '({T}: Add {W}.)', 'color': ['W'], 'mana_cost': '', 'subtype': ['Plains']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c382325(card.Card):
    "Pillarfield Ox"
    def __init__(self):
        super(c382325, self).__init__(gameobject.Characteristics(**{'name': 'Pillarfield Ox', 'text': '', 'color': ['W'], 'mana_cost': '3W', 'power': 2, 'toughness': 4, 'subtype': ['Ox']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452831(card.Card):
    "Pilfering Imp"
    def __init__(self):
        super(c452831, self).__init__(gameobject.Characteristics(**{'name': 'Pilfering Imp', 'text': 'Flying\n{1}{B}, {T}, Sacrifice this creature: Target opponent reveals their hand. You choose a nonland card from it. That player discards that card. Activate only as a sorcery.', 'color': ['B'], 'mana_cost': 'B', 'power': 1, 'toughness': 1, 'subtype': ['Imp']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c426003(card.Card):
    "Pilfered Plans"
    def __init__(self):
        super(c426003, self).__init__(gameobject.Characteristics(**{'name': 'Pilfered Plans', 'text': 'Target player mills two cards. Draw two cards.', 'color': ['B', 'U'], 'mana_cost': '1UB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c9874185497(card.Card):
    "Phoenix Down"
    def __init__(self):
        super(c9874185497, self).__init__(gameobject.Characteristics(**{'name': 'Phoenix Down', 'text': '{1}{W}, {T}, Exile this artifact: Choose one —\n• Return target creature card with mana value 4 or less from your graveyard to the battlefield tapped.\n• Exile target Skeleton, Spirit, or Zombie.', 'color': ['W'], 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c373722(card.Card):
    "Pharika's Cure"
    def __init__(self):
        super(c373722, self).__init__(gameobject.Characteristics(**{'name': "Pharika's Cure", 'text': "Pharika's Cure deals 2 damage to target creature and you gain 2 life.", 'color': ['B'], 'mana_cost': 'BB'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c423735(card.Card):
    "Perilous Predicament"
    def __init__(self):
        super(c423735, self).__init__(gameobject.Characteristics(**{'name': 'Perilous Predicament', 'text': 'Each opponent sacrifices an artifact creature and a nonartifact creature of their choice.', 'color': ['B'], 'mana_cost': '4B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c238327(card.Card):
    "Peregrine Griffin"
    def __init__(self):
        super(c238327, self).__init__(gameobject.Characteristics(**{'name': 'Peregrine Griffin', 'text': 'Flying\nFirst strike (This creature deals combat damage before creatures without first strike.)', 'color': ['W'], 'mana_cost': '4W', 'power': 2, 'toughness': 4, 'subtype': ['Griffin']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.First_Strike]))

class c423786(card.Card):
    "Peema Aether-Seer"
    def __init__(self):
        super(c423786, self).__init__(gameobject.Characteristics(**{'name': 'Peema Aether-Seer', 'text': 'When this creature enters, you get an amount of {E} (energy counters) equal to the greatest power among creatures you control.\nPay {E}{E}{E}: Target creature blocks this turn if able.', 'color': ['G'], 'mana_cost': '3G', 'power': 3, 'toughness': 2, 'subtype': ['Elf', 'Druid']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373507(card.Card):
    "Peak Eruption"
    def __init__(self):
        super(c373507, self).__init__(gameobject.Characteristics(**{'name': 'Peak Eruption', 'text': "Destroy target Mountain. Peak Eruption deals 3 damage to that land's controller.", 'color': ['R'], 'mana_cost': '2R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c32232(card.Card):
    "Pay No Heed"
    def __init__(self):
        super(c32232, self).__init__(gameobject.Characteristics(**{'name': 'Pay No Heed', 'text': 'Prevent all damage a source of your choice would deal this turn.', 'color': ['W'], 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452890(card.Card):
    "Pause for Reflection"
    def __init__(self):
        super(c452890, self).__init__(gameobject.Characteristics(**{'name': 'Pause for Reflection', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nPrevent all combat damage that would be dealt this turn.", 'color': ['G'], 'mana_cost': '2G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[static_abilities.StaticAbilities.Convoke]))

class c452772(card.Card):
    "Parhelion Patrol"
    def __init__(self):
        super(c452772, self).__init__(gameobject.Characteristics(**{'name': 'Parhelion Patrol', 'text': "Flying\nVigilance (Attacking doesn't cause this creature to tap.)\nMentor (Whenever this creature attacks, put a +1/+1 counter on target attacking creature with lesser power.)", 'color': ['W'], 'mana_cost': '3W', 'power': 2, 'toughness': 3, 'subtype': ['Human', 'Knight']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Vigilance]))

class c9550108450(card.Card):
    "Pacifism"
    def __init__(self):
        super(c9550108450, self).__init__(gameobject.Characteristics(**{'name': 'Pacifism', 'text': "Enchant creature\nEnchanted creature can't attack or block.", 'color': ['W'], 'mana_cost': '1W', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c423799(card.Card):
    "Outland Boar"
    def __init__(self):
        super(c423799, self).__init__(gameobject.Characteristics(**{'name': 'Outland Boar', 'text': "This creature can't be blocked by creatures with power 2 or less.", 'color': ['G', 'R'], 'mana_cost': '2RG', 'power': 4, 'toughness': 4, 'subtype': ['Boar']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c366479(card.Card):
    "Orzhov Keyrune"
    def __init__(self):
        super(c366479, self).__init__(gameobject.Characteristics(**{'name': 'Orzhov Keyrune', 'text': '{T}: Add {W} or {B}.\n{W}{B}: This artifact becomes a 1/4 white and black Thrull artifact creature with lifelink until end of turn.', 'color': ['B', 'W'], 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c9222593914(card.Card):
    "Opera Love Song"
    def __init__(self):
        super(c9222593914, self).__init__(gameobject.Characteristics(**{'name': 'Opera Love Song', 'text': 'Choose one —\n• Exile the top two cards of your library. You may play those cards until your next end step.\n• One or two target creatures each get +2/+0 until end of turn.', 'color': ['R'], 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c426920(card.Card):
    "Onward"
    def __init__(self):
        super(c426920, self).__init__(gameobject.Characteristics(**{'name': 'Onward', 'text': '', 'color': ['R', 'W'], 'mana_cost': '2R // 2W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c366261(card.Card):
    "One Thousand Lashes"
    def __init__(self):
        super(c366261, self).__init__(gameobject.Characteristics(**{'name': 'One Thousand Lashes', 'text': "Enchant creature\nEnchanted creature can't attack or block, and its activated abilities can't be activated.\nAt the beginning of the upkeep of enchanted creature's controller, that player loses 1 life.", 'color': ['B', 'W'], 'mana_cost': '2WB', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c9437324946(card.Card):
    "Omenspeaker"
    def __init__(self):
        super(c9437324946, self).__init__(gameobject.Characteristics(**{'name': 'Omenspeaker', 'text': 'When this creature enters, scry 2. (Look at the top two cards of your library, then put any number of them on the bottom and the rest on top in any order.)', 'color': ['U'], 'mana_cost': '1U', 'power': 1, 'toughness': 3, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452944(card.Card):
    "Ochran Assassin"
    def __init__(self):
        super(c452944, self).__init__(gameobject.Characteristics(**{'name': 'Ochran Assassin', 'text': 'Deathtouch\nAll creatures able to block this creature do so.', 'color': ['B', 'G'], 'mana_cost': '1BG', 'power': 1, 'toughness': 1, 'subtype': ['Elf', 'Assassin']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Deathtouch]))

class c373510(card.Card):
    "Nylea's Emissary"
    def __init__(self):
        super(c373510, self).__init__(gameobject.Characteristics(**{'name': "Nylea's Emissary", 'text': "Bestow {5}{G} (If you cast this card for its bestow cost, it's an Aura spell with enchant creature. It becomes a creature again if it's not attached.)\nTrample\nEnchanted creature gets +3/+3 and has trample.", 'color': ['G'], 'mana_cost': '3G', 'power': 3, 'toughness': 3, 'subtype': ['Cat']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample]))

class c452943(card.Card):
    "Notion Rain"
    def __init__(self):
        super(c452943, self).__init__(gameobject.Characteristics(**{'name': 'Notion Rain', 'text': 'Surveil 2, then draw two cards. Notion Rain deals 2 damage to you. (To surveil 2, look at the top two cards of your library, then put any number of them into your graveyard and the rest on top of your library in any order.)', 'color': ['B', 'U'], 'mana_cost': '1UB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c376432(card.Card):
    "Nivix Guildmage"
    def __init__(self):
        super(c376432, self).__init__(gameobject.Characteristics(**{'name': 'Nivix Guildmage', 'text': '{1}{U}{R}: Draw a card, then discard a card.\n{2}{U}{R}: Copy target instant or sorcery spell you control. You may choose new targets for the copy.', 'color': ['R', 'U'], 'mana_cost': 'UR', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452798(card.Card):
    "Nightveil Sprite"
    def __init__(self):
        super(c452798, self).__init__(gameobject.Characteristics(**{'name': 'Nightveil Sprite', 'text': 'Flying\nWhenever this creature attacks, surveil 1. (Look at the top card of your library. You may put it into your graveyard.)', 'color': ['U'], 'mana_cost': '1U', 'power': 1, 'toughness': 2, 'subtype': ['Faerie', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c452941(card.Card):
    "Nightveil Predator"
    def __init__(self):
        super(c452941, self).__init__(gameobject.Characteristics(**{'name': 'Nightveil Predator', 'text': "Flying, deathtouch\nHexproof (This creature can't be the target of spells or abilities your opponents control.)", 'color': ['B', 'U'], 'mana_cost': 'UUBB', 'power': 3, 'toughness': 3, 'subtype': ['Vampire']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Deathtouch, static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Hexproof]))

class c270367(card.Card):
    "New Prahv Guildmage"
    def __init__(self):
        super(c270367, self).__init__(gameobject.Characteristics(**{'name': 'New Prahv Guildmage', 'text': "{W}{U}: Target creature gains flying until end of turn.\n{3}{W}{U}: Detain target nonland permanent an opponent controls. (Until your next turn, that permanent can't attack or block and its activated abilities can't be activated.)", 'color': ['U', 'W'], 'mana_cost': 'WU', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9418407140(card.Card):
    "Never Happened"
    def __init__(self):
        super(c9418407140, self).__init__(gameobject.Characteristics(**{'name': 'Never Happened', 'text': "Target opponent reveals their hand. You choose a nonland card from that player's graveyard or hand and exile it.", 'color': ['B'], 'mana_cost': '2B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c409603(card.Card):
    "Nephalia Smuggler"
    def __init__(self):
        super(c409603, self).__init__(gameobject.Characteristics(**{'name': 'Nephalia Smuggler', 'text': '{3}{U}, {T}: Exile another target creature you control, then return that card to the battlefield under your control.', 'color': ['U'], 'mana_cost': 'U', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452829(card.Card):
    "Necrotic Wound"
    def __init__(self):
        super(c452829, self).__init__(gameobject.Characteristics(**{'name': 'Necrotic Wound', 'text': 'Undergrowth — Target creature gets -X/-X until end of turn, where X is the number of creature cards in your graveyard. If that creature would die this turn, exile it instead.', 'color': ['B'], 'mana_cost': 'B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c489395(card.Card):
    "Nature's Way"
    def __init__(self):
        super(c489395, self).__init__(gameobject.Characteristics(**{'name': "Nature's Way", 'text': "Target creature you control gains vigilance and trample until end of turn. It deals damage equal to its power to target creature you don't control.", 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c249699(card.Card):
    "Mwonvuli Beast Tracker"
    def __init__(self):
        super(c249699, self).__init__(gameobject.Characteristics(**{'name': 'Mwonvuli Beast Tracker', 'text': 'When this creature enters, search your library for a creature card with deathtouch, hexproof, reach, or trample and reveal it. Shuffle and put that card on top.', 'color': ['G'], 'mana_cost': '1GG', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Scout']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Reach, static_abilities.StaticAbilities.Hexproof]))

class c452796(card.Card):
    "Muse Drake"
    def __init__(self):
        super(c452796, self).__init__(gameobject.Characteristics(**{'name': 'Muse Drake', 'text': 'Flying\nWhen this creature enters, draw a card.', 'color': ['U'], 'mana_cost': '3U', 'power': 1, 'toughness': 3, 'subtype': ['Drake']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c681245(card.Card):
    "Mountain"
    def __init__(self):
        super(c681245, self).__init__(gameobject.Characteristics(**{'name': 'Mountain', 'text': '({T}: Add {R}.)', 'color': ['R'], 'mana_cost': '', 'subtype': ['Mountain']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c423783(card.Card):
    "Monstrous Onslaught"
    def __init__(self):
        super(c423783, self).__init__(gameobject.Characteristics(**{'name': 'Monstrous Onslaught', 'text': 'Monstrous Onslaught deals X damage divided as you choose among any number of target creatures, where X is the greatest power among creatures you control as you cast this spell.', 'color': ['G'], 'mana_cost': '3GG'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c9152414934(card.Card):
    "Monk's Fist"
    def __init__(self):
        super(c9152414934, self).__init__(gameobject.Characteristics(**{'name': "Monk's Fist", 'text': 'Job select (When this Equipment enters, create a 1/1 colorless Hero creature token, then attach this to it.)\nEquipped creature gets +1/+0 and is a Monk in addition to its other types.\nEquip {2} ({2}: Attach to target creature you control. Equip only as a sorcery.)', 'color': [], 'mana_cost': '2', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c466784(card.Card):
    "Moment of Heroism"
    def __init__(self):
        super(c466784, self).__init__(gameobject.Characteristics(**{'name': 'Moment of Heroism', 'text': 'Target creature gets +2/+2 and gains lifelink until end of turn. (Damage dealt by the creature also causes its controller to gain that much life.)', 'color': ['W'], 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452940(card.Card):
    "Molderhulk"
    def __init__(self):
        super(c452940, self).__init__(gameobject.Characteristics(**{'name': 'Molderhulk', 'text': 'Undergrowth — This spell costs {1} less to cast for each creature card in your graveyard.\nWhen this creature enters, return target land card from your graveyard to the battlefield.', 'color': ['B', 'G'], 'mana_cost': '7BG', 'power': 6, 'toughness': 6, 'subtype': ['Fungus', 'Zombie']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9126544573(card.Card):
    "Mist Raven"
    def __init__(self):
        super(c9126544573, self).__init__(gameobject.Characteristics(**{'name': 'Mist Raven', 'text': "Flying\nWhen this creature enters, return target creature to its owner's hand.", 'color': ['U'], 'mana_cost': '2UU', 'power': 2, 'toughness': 2, 'subtype': ['Bird']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c366340(card.Card):
    "Miming Slime"
    def __init__(self):
        super(c366340, self).__init__(gameobject.Characteristics(**{'name': 'Miming Slime', 'text': 'Create an X/X green Ooze creature token, where X is the greatest power among creatures you control.', 'color': ['G'], 'mana_cost': '2G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c476075(card.Card):
    "Mighty Leap"
    def __init__(self):
        super(c476075, self).__init__(gameobject.Characteristics(**{'name': 'Mighty Leap', 'text': 'Target creature gets +2/+2 and gains flying until end of turn.', 'color': ['W'], 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c9734168405(card.Card):
    "Might of the Masses"
    def __init__(self):
        super(c9734168405, self).__init__(gameobject.Characteristics(**{'name': 'Might of the Masses', 'text': 'Target creature gets +1/+1 until end of turn for each creature you control.', 'color': ['G'], 'mana_cost': 'G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c368976(card.Card):
    "Maze Sentinel"
    def __init__(self):
        super(c368976, self).__init__(gameobject.Characteristics(**{'name': 'Maze Sentinel', 'text': 'Vigilance\nMulticolored creatures you control have vigilance.', 'color': ['W'], 'mana_cost': '5W', 'power': 3, 'toughness': 6, 'subtype': ['Elemental']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance]))

class c9708910649(card.Card):
    "Maximize Altitude"
    def __init__(self):
        super(c9708910649, self).__init__(gameobject.Characteristics(**{'name': 'Maximize Altitude', 'text': 'Target creature gets +1/+1 and gains flying until end of turn.\nJump-start (You may cast this card from your graveyard by discarding a card in addition to paying its other costs. Then exile this card.)', 'color': ['U'], 'mana_cost': 'U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c9716126448(card.Card):
    "Maverick Thopterist"
    def __init__(self):
        super(c9716126448, self).__init__(gameobject.Characteristics(**{'name': 'Maverick Thopterist', 'text': "Improvise (Your artifacts can help cast this spell. Each artifact you tap after you're done activating mana abilities pays for {1}.)\nWhen this creature enters, create two 1/1 colorless Thopter artifact creature tokens with flying.", 'color': ['R', 'U'], 'mana_cost': '3UR', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Artificer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Improvise]))

class c423782(card.Card):
    "Maulfist Revolutionary"
    def __init__(self):
        super(c423782, self).__init__(gameobject.Characteristics(**{'name': 'Maulfist Revolutionary', 'text': 'Trample\nWhen this creature enters or dies, for each kind of counter on target permanent or player, give that permanent or player another counter of that kind.', 'color': ['G'], 'mana_cost': '1GG', 'power': 3, 'toughness': 3, 'subtype': ['Human', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample]))

class c370708(card.Card):
    "Master of Diversion"
    def __init__(self):
        super(c370708, self).__init__(gameobject.Characteristics(**{'name': 'Master of Diversion', 'text': 'Whenever this creature attacks, tap target creature defending player controls.', 'color': ['W'], 'mana_cost': '2W', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Scout']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c435381(card.Card):
    "Marauding Looter"
    def __init__(self):
        super(c435381, self).__init__(gameobject.Characteristics(**{'name': 'Marauding Looter', 'text': 'Raid — At the beginning of your end step, if you attacked this turn, you may draw a card. If you do, discard a card.', 'color': ['R', 'U'], 'mana_cost': '2UR', 'power': 4, 'toughness': 3, 'subtype': ['Human', 'Pirate']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c466903(card.Card):
    "Maniacal Rage"
    def __init__(self):
        super(c466903, self).__init__(gameobject.Characteristics(**{'name': 'Maniacal Rage', 'text': "Enchant creature\nEnchanted creature gets +2/+2 and can't block.", 'color': ['R'], 'mana_cost': '1R', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c417662(card.Card):
    "Make Obsolete"
    def __init__(self):
        super(c417662, self).__init__(gameobject.Characteristics(**{'name': 'Make Obsolete', 'text': 'Creatures your opponents control get -1/-1 until end of turn.', 'color': ['B'], 'mana_cost': '2B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c571580(card.Card):
    "Magister Sphinx"
    def __init__(self):
        super(c571580, self).__init__(gameobject.Characteristics(**{'name': 'Magister Sphinx', 'text': "Flying\nWhen this creature enters, target player's life total becomes 10.", 'color': ['B', 'U', 'W'], 'mana_cost': '4WUB', 'power': 5, 'toughness': 5, 'subtype': ['Sphinx']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c452770(card.Card):
    "Loxodon Restorer"
    def __init__(self):
        super(c452770, self).__init__(gameobject.Characteristics(**{'name': 'Loxodon Restorer', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nWhen this creature enters, you gain 4 life.", 'color': ['W'], 'mana_cost': '4WW', 'power': 3, 'toughness': 4, 'subtype': ['Elephant', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Convoke]))

class c9501367949(card.Card):
    "Lotleth Giant"
    def __init__(self):
        super(c9501367949, self).__init__(gameobject.Characteristics(**{'name': 'Lotleth Giant', 'text': 'Undergrowth — When this creature enters, it deals 1 damage to target opponent for each creature card in your graveyard.', 'color': ['B'], 'mana_cost': '6B', 'power': 6, 'toughness': 5, 'subtype': ['Zombie', 'Giant']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c218053(card.Card):
    "Lost Leonin"
    def __init__(self):
        super(c218053, self).__init__(gameobject.Characteristics(**{'name': 'Lost Leonin', 'text': 'Infect (This creature deals damage to creatures in the form of -1/-1 counters and to players in the form of poison counters.)', 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 1, 'subtype': ['Phyrexian', 'Cat', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Infect]))

class c289218(card.Card):
    "Lobber Crew"
    def __init__(self):
        super(c289218, self).__init__(gameobject.Characteristics(**{'name': 'Lobber Crew', 'text': 'Defender\n{T}: This creature deals 1 damage to each opponent.\nWhenever you cast a multicolored spell, untap this creature.', 'color': ['R'], 'mana_cost': '2R', 'power': 0, 'toughness': 4, 'subtype': ['Goblin', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c446116(card.Card):
    "Liturgy of Blood"
    def __init__(self):
        super(c446116, self).__init__(gameobject.Characteristics(**{'name': 'Liturgy of Blood', 'text': 'Destroy target creature. Add {B}{B}{B}.', 'color': ['B'], 'mana_cost': '3BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c423781(card.Card):
    "Lifecrafter's Gift"
    def __init__(self):
        super(c423781, self).__init__(gameobject.Characteristics(**{'name': "Lifecrafter's Gift", 'text': 'Put a +1/+1 counter on target creature, then put a +1/+1 counter on each creature you control with a +1/+1 counter on it.', 'color': ['G'], 'mana_cost': '3G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c423779(card.Card):
    "Lifecraft Awakening"
    def __init__(self):
        super(c423779, self).__init__(gameobject.Characteristics(**{'name': 'Lifecraft Awakening', 'text': "Put X +1/+1 counters on target artifact you control. If it isn't a creature or Vehicle, it becomes a 0/0 Construct artifact creature.", 'color': ['G'], 'mana_cost': 'XG'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452937(card.Card):
    "Legion Guildmage"
    def __init__(self):
        super(c452937, self).__init__(gameobject.Characteristics(**{'name': 'Legion Guildmage', 'text': '{5}{R}, {T}: This creature deals 3 damage to each opponent.\n{2}{W}, {T}: Tap another target creature.', 'color': ['R', 'W'], 'mana_cost': 'RW', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452768(card.Card):
    "Ledev Guardian"
    def __init__(self):
        super(c452768, self).__init__(gameobject.Characteristics(**{'name': 'Ledev Guardian', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)", 'color': ['W'], 'mana_cost': '3W', 'power': 2, 'toughness': 4, 'subtype': ['Human', 'Knight']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Convoke]))

class c452936(card.Card):
    "Ledev Champion"
    def __init__(self):
        super(c452936, self).__init__(gameobject.Characteristics(**{'name': 'Ledev Champion', 'text': 'Whenever this creature attacks, you may tap any number of untapped creatures you control. This creature gets +1/+1 until end of turn for each creature tapped this way.\n{3}{G}{W}: Create a 1/1 white Soldier creature token with lifelink.', 'color': ['G', 'W'], 'mana_cost': '1GW', 'power': 2, 'toughness': 2, 'subtype': ['Elf', 'Knight']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9661457745(card.Card):
    "Leapfrog"
    def __init__(self):
        super(c9661457745, self).__init__(gameobject.Characteristics(**{'name': 'Leapfrog', 'text': "This creature has flying as long as you've cast an instant or sorcery spell this turn.", 'color': ['U'], 'mana_cost': '2U', 'power': 3, 'toughness': 1, 'subtype': ['Frog']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452935(card.Card):
    "League Guildmage"
    def __init__(self):
        super(c452935, self).__init__(gameobject.Characteristics(**{'name': 'League Guildmage', 'text': '{3}{U}, {T}: Draw a card.\n{X}{R}, {T}: Copy target instant or sorcery spell you control with mana value X. You may choose new targets for the copy.', 'color': ['R', 'U'], 'mana_cost': 'UR', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c426798(card.Card):
    "Lay Bare the Heart"
    def __init__(self):
        super(c426798, self).__init__(gameobject.Characteristics(**{'name': 'Lay Bare the Heart', 'text': 'Target opponent reveals their hand. You choose a nonlegendary, nonland card from it. That player discards that card.', 'color': ['B'], 'mana_cost': '1B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c373680(card.Card):
    "Last Breath"
    def __init__(self):
        super(c373680, self).__init__(gameobject.Characteristics(**{'name': 'Last Breath', 'text': 'Exile target creature with power 2 or less. Its controller gains 4 life.', 'color': ['W'], 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c373610(card.Card):
    "Lash of the Whip"
    def __init__(self):
        super(c373610, self).__init__(gameobject.Characteristics(**{'name': 'Lash of the Whip', 'text': 'Target creature gets -4/-4 until end of turn.', 'color': ['B'], 'mana_cost': '4B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c9050003944(card.Card):
    "Kraul Warrior"
    def __init__(self):
        super(c9050003944, self).__init__(gameobject.Characteristics(**{'name': 'Kraul Warrior', 'text': '{5}{G}: This creature gets +3/+3 until end of turn.', 'color': ['G'], 'mana_cost': '1G', 'power': 2, 'toughness': 2, 'subtype': ['Insect', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452823(card.Card):
    "Kraul Swarm"
    def __init__(self):
        super(c452823, self).__init__(gameobject.Characteristics(**{'name': 'Kraul Swarm', 'text': 'Flying\n{2}{B}, Discard a creature card: Return this card from your graveyard to your hand.', 'color': ['B'], 'mana_cost': '4B', 'power': 4, 'toughness': 1, 'subtype': ['Insect', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c9414997063(card.Card):
    "Kraul Foragers"
    def __init__(self):
        super(c9414997063, self).__init__(gameobject.Characteristics(**{'name': 'Kraul Foragers', 'text': 'Undergrowth — When this creature enters, you gain 1 life for each creature card in your graveyard.', 'color': ['G'], 'mana_cost': '4G', 'power': 4, 'toughness': 4, 'subtype': ['Insect', 'Scout']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9694157782(card.Card):
    "Kor Hookmaster"
    def __init__(self):
        super(c9694157782, self).__init__(gameobject.Characteristics(**{'name': 'Kor Hookmaster', 'text': "When this creature enters, tap target creature an opponent controls. That creature doesn't untap during its controller's next untap step.", 'color': ['W'], 'mana_cost': '2W', 'power': 2, 'toughness': 2, 'subtype': ['Kor', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c366477(card.Card):
    "Knight Watch"
    def __init__(self):
        super(c366477, self).__init__(gameobject.Characteristics(**{'name': 'Knight Watch', 'text': 'Create two 2/2 white Knight creature tokens with vigilance.', 'color': ['W'], 'mana_cost': '4W'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c366237(card.Card):
    "Knight of Obligation"
    def __init__(self):
        super(c366237, self).__init__(gameobject.Characteristics(**{'name': 'Knight of Obligation', 'text': 'Vigilance\nExtort (Whenever you cast a spell, you may pay {W/B}. If you do, each opponent loses 1 life and you gain that much life.)', 'color': ['W'], 'mana_cost': '3W', 'power': 2, 'toughness': 4, 'subtype': ['Human', 'Knight']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance]))

class c265731(card.Card):
    "Knight of Glory"
    def __init__(self):
        super(c265731, self).__init__(gameobject.Characteristics(**{'name': 'Knight of Glory', 'text': "Protection from black (This creature can't be blocked, targeted, dealt damage, or enchanted by anything black.)\nExalted (Whenever a creature you control attacks alone, that creature gets +1/+1 until end of turn.)", 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Knight']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c243233(card.Card):
    "Kessig Recluse"
    def __init__(self):
        super(c243233, self).__init__(gameobject.Characteristics(**{'name': 'Kessig Recluse', 'text': 'Reach (This creature can block creatures with flying.)\nDeathtouch (Any amount of damage this deals to a creature is enough to destroy it.)', 'color': ['G'], 'mana_cost': '2GG', 'power': 2, 'toughness': 3, 'subtype': ['Spider']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Reach, static_abilities.StaticAbilities.Deathtouch]))

class c426933(card.Card):
    "Kefnet's Monument"
    def __init__(self):
        super(c426933, self).__init__(gameobject.Characteristics(**{'name': "Kefnet's Monument", 'text': "Blue creature spells you cast cost {1} less to cast.\nWhenever you cast a creature spell, target creature an opponent controls doesn't untap during its controller's next untap step.", 'color': [], 'mana_cost': '3'}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c373538(card.Card):
    "Karametra's Acolyte"
    def __init__(self):
        super(c373538, self).__init__(gameobject.Characteristics(**{'name': "Karametra's Acolyte", 'text': '{T}: Add an amount of {G} equal to your devotion to green. (Each {G} in the mana costs of permanents you control counts toward your devotion to green.)', 'color': ['G'], 'mana_cost': '3G', 'power': 1, 'toughness': 4, 'subtype': ['Human', 'Druid']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c289221(card.Card):
    "Judge's Familiar"
    def __init__(self):
        super(c289221, self).__init__(gameobject.Characteristics(**{'name': "Judge's Familiar", 'text': 'Flying\nSacrifice this creature: Counter target instant or sorcery spell unless its controller pays {1}.', 'color': ['U', 'W'], 'mana_cost': 'W/U', 'power': 1, 'toughness': 1, 'subtype': ['Bird']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c417626(card.Card):
    "Janjeet Sentry"
    def __init__(self):
        super(c417626, self).__init__(gameobject.Characteristics(**{'name': 'Janjeet Sentry', 'text': 'When this creature enters, you get {E}{E} (two energy counters).\n{T}, Pay {E}{E}: You may tap or untap target artifact or creature.', 'color': ['U'], 'mana_cost': '2U', 'power': 2, 'toughness': 3, 'subtype': ['Vedalken', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c253514(card.Card):
    "Izzet Keyrune"
    def __init__(self):
        super(c253514, self).__init__(gameobject.Characteristics(**{'name': 'Izzet Keyrune', 'text': '{T}: Add {U} or {R}.\n{U}{R}: Until end of turn, this artifact becomes a 2/1 blue and red Elemental artifact creature.\nWhenever this artifact deals combat damage to a player, you may draw a card. If you do, discard a card.', 'color': ['R', 'U'], 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c681241(card.Card):
    "Island"
    def __init__(self):
        super(c681241, self).__init__(gameobject.Characteristics(**{'name': 'Island', 'text': '({T}: Add {U}.)', 'color': ['U'], 'mana_cost': '', 'subtype': ['Island']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c452884(card.Card):
    "Ironshell Beetle"
    def __init__(self):
        super(c452884, self).__init__(gameobject.Characteristics(**{'name': 'Ironshell Beetle', 'text': 'When this creature enters, put a +1/+1 counter on target creature.', 'color': ['G'], 'mana_cost': '1G', 'power': 1, 'toughness': 1, 'subtype': ['Insect']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c423732(card.Card):
    "Ironclad Revolutionary"
    def __init__(self):
        super(c423732, self).__init__(gameobject.Characteristics(**{'name': 'Ironclad Revolutionary', 'text': 'When this creature enters, you may sacrifice an artifact. If you do, put two +1/+1 counters on this creature and each opponent loses 2 life.', 'color': ['B'], 'mana_cost': '4BB', 'power': 4, 'toughness': 4, 'subtype': ['Aetherborn', 'Artificer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9504480812(card.Card):
    "Iona's Judgment"
    def __init__(self):
        super(c9504480812, self).__init__(gameobject.Characteristics(**{'name': "Iona's Judgment", 'text': 'Exile target creature or enchantment.', 'color': ['W'], 'mana_cost': '4W'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c684272(card.Card):
    "Invigorated Rampage"
    def __init__(self):
        super(c684272, self).__init__(gameobject.Characteristics(**{'name': 'Invigorated Rampage', 'text': 'Choose one —\n• Target creature gets +4/+0 and gains trample until end of turn.\n• Two target creatures each get +2/+0 and gain trample until end of turn.', 'color': ['R'], 'mana_cost': '1R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452978(card.Card):
    "Invert"
    def __init__(self):
        super(c452978, self).__init__(gameobject.Characteristics(**{'name': 'Invert', 'text': '', 'color': ['R', 'U'], 'mana_cost': 'U/R // 4UR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c409811(card.Card):
    "Invasive Surgery"
    def __init__(self):
        super(c409811, self).__init__(gameobject.Characteristics(**{'name': 'Invasive Surgery', 'text': "Counter target sorcery spell.\nDelirium — If there are four or more card types among cards in your graveyard, search the graveyard, hand, and library of that spell's controller for any number of cards with the same name as that spell, exile those cards, then that player shuffles.", 'color': ['U'], 'mana_cost': 'U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452977(card.Card):
    "Integrity"
    def __init__(self):
        super(c452977, self).__init__(gameobject.Characteristics(**{'name': 'Integrity', 'text': '', 'color': ['R', 'W'], 'mana_cost': 'R/W // 2RW'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452766(card.Card):
    "Inspiring Unicorn"
    def __init__(self):
        super(c452766, self).__init__(gameobject.Characteristics(**{'name': 'Inspiring Unicorn', 'text': 'Whenever this creature attacks, creatures you control get +1/+1 until end of turn.', 'color': ['W'], 'mana_cost': '2WW', 'power': 2, 'toughness': 2, 'subtype': ['Unicorn']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9714072916(card.Card):
    "Insomnia, Crown City"
    def __init__(self):
        super(c9714072916, self).__init__(gameobject.Characteristics(**{'name': 'Insomnia, Crown City', 'text': 'This land enters tapped.\n{T}: Add {W} or {B}.', 'color': ['B', 'W'], 'mana_cost': '', 'subtype': ['Town']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c452857(card.Card):
    "Inescapable Blaze"
    def __init__(self):
        super(c452857, self).__init__(gameobject.Characteristics(**{'name': 'Inescapable Blaze', 'text': "This spell can't be countered.\nInescapable Blaze deals 6 damage to any target.", 'color': ['R'], 'mana_cost': '4RR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c423703(card.Card):
    "Illusionist's Stratagem"
    def __init__(self):
        super(c423703, self).__init__(gameobject.Characteristics(**{'name': "Illusionist's Stratagem", 'text': "Exile up to two target creatures you control, then return those cards to the battlefield under their owner's control.\nDraw a card.", 'color': ['U'], 'mana_cost': '3U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c198176(card.Card):
    "Ikiral Outrider"
    def __init__(self):
        super(c198176, self).__init__(gameobject.Characteristics(**{'name': 'Ikiral Outrider', 'text': 'Level up {4} ({4}: Put a level counter on this. Level up only as a sorcery.)\nLEVEL 1-3\n2/6\nVigilance\nLEVEL 4+\n3/10\nVigilance', 'color': ['W'], 'mana_cost': '1W', 'power': 1, 'toughness': 2, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance]))

class c9466167343(card.Card):
    "Hypothesizzle"
    def __init__(self):
        super(c9466167343, self).__init__(gameobject.Characteristics(**{'name': 'Hypothesizzle', 'text': 'Draw two cards. Then you may discard a nonland card. When you do, Hypothesizzle deals 4 damage to target creature.', 'color': ['R', 'U'], 'mana_cost': '3UR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452765(card.Card):
    "Hunted Witness"
    def __init__(self):
        super(c452765, self).__init__(gameobject.Characteristics(**{'name': 'Hunted Witness', 'text': 'When this creature dies, create a 1/1 white Soldier creature token with lifelink.', 'color': ['W'], 'mana_cost': 'W', 'power': 1, 'toughness': 1, 'subtype': ['Human']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373668(card.Card):
    "Hunt the Hunter"
    def __init__(self):
        super(c373668, self).__init__(gameobject.Characteristics(**{'name': 'Hunt the Hunter', 'text': 'Target green creature you control gets +2/+2 until end of turn. It fights target green creature an opponent controls.', 'color': ['G'], 'mana_cost': 'G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c423751(card.Card):
    "Hungry Flames"
    def __init__(self):
        super(c423751, self).__init__(gameobject.Characteristics(**{'name': 'Hungry Flames', 'text': 'Hungry Flames deals 3 damage to target creature and 2 damage to target player or planeswalker.', 'color': ['R'], 'mana_cost': '2R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452927(card.Card):
    "House Guildmage"
    def __init__(self):
        super(c452927, self).__init__(gameobject.Characteristics(**{'name': 'House Guildmage', 'text': "{1}{U}, {T}: Target creature doesn't untap during its controller's next untap step.\n{2}{B}, {T}: Surveil 2. (Look at the top two cards of your library, then put any number of them into your graveyard and the rest on top of your library in any order.)", 'color': ['B', 'U'], 'mana_cost': 'UB', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c366368(card.Card):
    "Holy Mantle"
    def __init__(self):
        super(c366368, self).__init__(gameobject.Characteristics(**{'name': 'Holy Mantle', 'text': 'Enchant creature\nEnchanted creature gets +2/+2 and has protection from creatures.', 'color': ['W'], 'mana_cost': '2WW', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c262868(card.Card):
    "Hollowhenge Beast"
    def __init__(self):
        super(c262868, self).__init__(gameobject.Characteristics(**{'name': 'Hollowhenge Beast', 'text': '', 'color': ['G'], 'mana_cost': '3GG', 'power': 5, 'toughness': 5, 'subtype': ['Beast']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c366276(card.Card):
    "Hold the Gates"
    def __init__(self):
        super(c366276, self).__init__(gameobject.Characteristics(**{'name': 'Hold the Gates', 'text': 'Creatures you control get +0/+1 for each Gate you control and have vigilance.', 'color': ['W'], 'mana_cost': '2W'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c452883(card.Card):
    "Hitchclaw Recluse"
    def __init__(self):
        super(c452883, self).__init__(gameobject.Characteristics(**{'name': 'Hitchclaw Recluse', 'text': 'Reach', 'color': ['G'], 'mana_cost': '2G', 'power': 1, 'toughness': 4, 'subtype': ['Spider']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Reach]))

class c452822(card.Card):
    "Hired Poisoner"
    def __init__(self):
        super(c452822, self).__init__(gameobject.Characteristics(**{'name': 'Hired Poisoner', 'text': 'Deathtouch', 'color': ['B'], 'mana_cost': 'B', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Assassin']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Deathtouch]))

class c366459(card.Card):
    "Hindervines"
    def __init__(self):
        super(c366459, self).__init__(gameobject.Characteristics(**{'name': 'Hindervines', 'text': 'Prevent all combat damage that would be dealt this turn by creatures with no +1/+1 counters on them.', 'color': ['G'], 'mana_cost': '2G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c369021(card.Card):
    "Hidden Strings"
    def __init__(self):
        super(c369021, self).__init__(gameobject.Characteristics(**{'name': 'Hidden Strings', 'text': 'You may tap or untap target permanent, then you may tap or untap another target permanent.\nCipher (Then you may exile this spell card encoded on a creature you control. Whenever that creature deals combat damage to a player, its controller may cast a copy of the encoded card without paying its mana cost.)', 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c423777(card.Card):
    "Hidden Herbalists"
    def __init__(self):
        super(c423777, self).__init__(gameobject.Characteristics(**{'name': 'Hidden Herbalists', 'text': 'Revolt — When this creature enters, if a permanent left the battlefield under your control this turn, add {G}{G}.', 'color': ['G'], 'mana_cost': '1G', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Druid']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c23183(card.Card):
    "Heroes' Reunion"
    def __init__(self):
        super(c23183, self).__init__(gameobject.Characteristics(**{'name': "Heroes' Reunion", 'text': 'Target player gains 7 life.', 'color': ['G', 'W'], 'mana_cost': 'GW'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452856(card.Card):
    "Hellkite Whelp"
    def __init__(self):
        super(c452856, self).__init__(gameobject.Characteristics(**{'name': 'Hellkite Whelp', 'text': 'Flying\nWhenever this creature attacks, it deals 1 damage to target creature defending player controls.', 'color': ['R'], 'mana_cost': '4R', 'power': 3, 'toughness': 3, 'subtype': ['Dragon']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c289211(card.Card):
    "Hellhole Flailer"
    def __init__(self):
        super(c289211, self).__init__(gameobject.Characteristics(**{'name': 'Hellhole Flailer', 'text': "Unleash (You may have this creature enter with a +1/+1 counter on it. It can't block as long as it has a +1/+1 counter on it.)\n{2}{B}{R}, Sacrifice this creature: It deals damage equal to its power to target player or planeswalker.", 'color': ['B', 'R'], 'mana_cost': '1BR', 'power': 3, 'toughness': 2, 'subtype': ['Ogre', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c276206(card.Card):
    "Healer of the Pride"
    def __init__(self):
        super(c276206, self).__init__(gameobject.Characteristics(**{'name': 'Healer of the Pride', 'text': 'Whenever another creature you control enters, you gain 2 life.', 'color': ['W'], 'mana_cost': '3W', 'power': 2, 'toughness': 3, 'subtype': ['Cat', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c279613(card.Card):
    "Haunted Guardian"
    def __init__(self):
        super(c279613, self).__init__(gameobject.Characteristics(**{'name': 'Haunted Guardian', 'text': 'Defender, first strike', 'color': [], 'mana_cost': '2', 'power': 2, 'toughness': 1, 'subtype': ['Construct']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.First_Strike, static_abilities.StaticAbilities.Defender]))

class c417658(card.Card):
    "Harsh Scrutiny"
    def __init__(self):
        super(c417658, self).__init__(gameobject.Characteristics(**{'name': 'Harsh Scrutiny', 'text': 'Target opponent reveals their hand. You choose a creature card from it. That player discards that card. Scry 1.', 'color': ['B'], 'mana_cost': 'B'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c198165(card.Card):
    "Harmless Assault"
    def __init__(self):
        super(c198165, self).__init__(gameobject.Characteristics(**{'name': 'Harmless Assault', 'text': 'Prevent all combat damage that would be dealt this turn by attacking creatures.', 'color': ['W'], 'mana_cost': '2WW'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c369077(card.Card):
    "Haazda Snare Squad"
    def __init__(self):
        super(c369077, self).__init__(gameobject.Characteristics(**{'name': 'Haazda Snare Squad', 'text': 'Whenever this creature attacks, you may pay {W}. If you do, tap target creature an opponent controls.', 'color': ['W'], 'mana_cost': '2W', 'power': 1, 'toughness': 4, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452763(card.Card):
    "Haazda Marshal"
    def __init__(self):
        super(c452763, self).__init__(gameobject.Characteristics(**{'name': 'Haazda Marshal', 'text': 'Whenever this creature and at least two other creatures attack, create a 1/1 white Soldier creature token with lifelink.', 'color': ['W'], 'mana_cost': 'W', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c366392(card.Card):
    "Guildscorn Ward"
    def __init__(self):
        super(c366392, self).__init__(gameobject.Characteristics(**{'name': 'Guildscorn Ward', 'text': 'Enchant creature\nEnchanted creature has protection from multicolored.', 'color': ['W'], 'mana_cost': 'W', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c452791(card.Card):
    "Guild Summit"
    def __init__(self):
        super(c452791, self).__init__(gameobject.Characteristics(**{'name': 'Guild Summit', 'text': 'When this enchantment enters, you may tap any number of untapped Gates you control. Draw a card for each Gate tapped this way.\nWhenever a Gate you control enters, draw a card.', 'color': ['U'], 'mana_cost': '2U'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c279701(card.Card):
    "Guardian Lions"
    def __init__(self):
        super(c279701, self).__init__(gameobject.Characteristics(**{'name': 'Guardian Lions', 'text': "Vigilance (Attacking doesn't cause this creature to tap.)", 'color': ['W'], 'mana_cost': '4W', 'power': 1, 'toughness': 6, 'subtype': ['Cat']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance]))

class c193445(card.Card):
    "Guard Duty"
    def __init__(self):
        super(c193445, self).__init__(gameobject.Characteristics(**{'name': 'Guard Duty', 'text': 'Enchant creature\nEnchanted creature has defender.', 'color': ['W'], 'mana_cost': 'W', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c370626(card.Card):
    "Groundshaker Sliver"
    def __init__(self):
        super(c370626, self).__init__(gameobject.Characteristics(**{'name': 'Groundshaker Sliver', 'text': "Sliver creatures you control have trample. (A creature with trample can deal excess combat damage to the player or planeswalker it's attacking.)", 'color': ['G'], 'mana_cost': '6G', 'power': 5, 'toughness': 5, 'subtype': ['Sliver']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c466775(card.Card):
    "Griffin Sentinel"
    def __init__(self):
        super(c466775, self).__init__(gameobject.Characteristics(**{'name': 'Griffin Sentinel', 'text': "Flying\nVigilance (Attacking doesn't cause this creature to tap.)", 'color': ['W'], 'mana_cost': '2W', 'power': 1, 'toughness': 3, 'subtype': ['Griffin']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Vigilance]))

class c423750(card.Card):
    "Gremlin Infestation"
    def __init__(self):
        super(c423750, self).__init__(gameobject.Characteristics(**{'name': 'Gremlin Infestation', 'text': "Enchant artifact\nAt the beginning of your end step, this Aura deals 2 damage to enchanted artifact's controller.\nWhen enchanted artifact is put into a graveyard, create a 2/2 red Gremlin creature token.", 'color': ['R'], 'mana_cost': '3R', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c452855(card.Card):
    "Gravitic Punch"
    def __init__(self):
        super(c452855, self).__init__(gameobject.Characteristics(**{'name': 'Gravitic Punch', 'text': 'Target creature you control deals damage equal to its power to target player.\nJump-start (You may cast this card from your graveyard by discarding a card in addition to paying its other costs. Then exile this card.)', 'color': ['R'], 'mana_cost': '3R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c9120307405(card.Card):
    "Gravedigger"
    def __init__(self):
        super(c9120307405, self).__init__(gameobject.Characteristics(**{'name': 'Gravedigger', 'text': 'When this creature enters, you may return target creature card from your graveyard to your hand.', 'color': ['B'], 'mana_cost': '3B', 'power': 2, 'toughness': 2, 'subtype': ['Zombie']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c426946(card.Card):
    "Grasping Dunes"
    def __init__(self):
        super(c426946, self).__init__(gameobject.Characteristics(**{'name': 'Grasping Dunes', 'text': '{T}: Add {C}.\n{1}, {T}, Sacrifice this land: Put a -1/-1 counter on target creature. Activate only as a sorcery.', 'color': [], 'mana_cost': '', 'subtype': ['Desert']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c452881(card.Card):
    "Grappling Sundew"
    def __init__(self):
        super(c452881, self).__init__(gameobject.Characteristics(**{'name': 'Grappling Sundew', 'text': 'Defender, reach\n{4}{G}: This creature gains indestructible until end of turn. (Damage and effects that say "destroy" don\'t destroy this creature.)', 'color': ['G'], 'mana_cost': '1G', 'power': 0, 'toughness': 4, 'subtype': ['Plant']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Reach, static_abilities.StaticAbilities.Defender]))

class c270796(card.Card):
    "Gore-House Chainwalker"
    def __init__(self):
        super(c270796, self).__init__(gameobject.Characteristics(**{'name': 'Gore-House Chainwalker', 'text': "Unleash (You may have this creature enter with a +1/+1 counter on it. It can't block as long as it has a +1/+1 counter on it.)", 'color': ['R'], 'mana_cost': '1R', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9829223242(card.Card):
    "Gorehorn Minotaurs"
    def __init__(self):
        super(c9829223242, self).__init__(gameobject.Characteristics(**{'name': 'Gorehorn Minotaurs', 'text': 'Bloodthirst 2 (If an opponent was dealt damage this turn, this creature enters with two +1/+1 counters on it.)', 'color': ['R'], 'mana_cost': '2RR', 'power': 3, 'toughness': 3, 'subtype': ['Minotaur', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c423730(card.Card):
    "Gonti's Machinations"
    def __init__(self):
        super(c423730, self).__init__(gameobject.Characteristics(**{'name': "Gonti's Machinations", 'text': 'Whenever you lose life for the first time each turn, you get {E}. (You get an energy counter. Damage causes loss of life.)\nPay {E}{E}, Sacrifice this enchantment: Each opponent loses 3 life. You gain life equal to the life lost this way.', 'color': ['B'], 'mana_cost': 'B'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c452880(card.Card):
    "Golgari Raiders"
    def __init__(self):
        super(c452880, self).__init__(gameobject.Characteristics(**{'name': 'Golgari Raiders', 'text': 'Haste\nUndergrowth — This creature enters with a +1/+1 counter on it for each creature card in your graveyard.', 'color': ['G'], 'mana_cost': '3G', 'power': 0, 'toughness': 0, 'subtype': ['Elf', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c452925(card.Card):
    "Golgari Findbroker"
    def __init__(self):
        super(c452925, self).__init__(gameobject.Characteristics(**{'name': 'Golgari Findbroker', 'text': 'When this creature enters, return target permanent card from your graveyard to your hand.', 'color': ['B', 'G'], 'mana_cost': 'BBGG', 'power': 3, 'toughness': 4, 'subtype': ['Elf', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c253508(card.Card):
    "Golgari Decoy"
    def __init__(self):
        super(c253508, self).__init__(gameobject.Characteristics(**{'name': 'Golgari Decoy', 'text': "All creatures able to block this creature do so.\nScavenge {3}{G}{G} ({3}{G}{G}, Exile this card from your graveyard: Put a number of +1/+1 counters equal to this card's power on target creature. Scavenge only as a sorcery.)", 'color': ['G'], 'mana_cost': '3G', 'power': 2, 'toughness': 2, 'subtype': ['Elf', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c239998(card.Card):
    "Goldnight Redeemer"
    def __init__(self):
        super(c239998, self).__init__(gameobject.Characteristics(**{'name': 'Goldnight Redeemer', 'text': 'Flying\nWhen this creature enters, you gain 2 life for each other creature you control.', 'color': ['W'], 'mana_cost': '4WW', 'power': 4, 'toughness': 4, 'subtype': ['Angel']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c508317(card.Card):
    "Goldnight Commander"
    def __init__(self):
        super(c508317, self).__init__(gameobject.Characteristics(**{'name': 'Goldnight Commander', 'text': 'Whenever another creature you control enters, creatures you control get +1/+1 until end of turn.', 'color': ['W'], 'mana_cost': '3W', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Cleric', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c213926(card.Card):
    "Golden Urn"
    def __init__(self):
        super(c213926, self).__init__(gameobject.Characteristics(**{'name': 'Golden Urn', 'text': 'At the beginning of your upkeep, you may put a charge counter on this artifact.\n{T}, Sacrifice this artifact: You gain life equal to the number of charge counters on this artifact.', 'color': [], 'mana_cost': '1'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c9692854208(card.Card):
    "Goblin Locksmith"
    def __init__(self):
        super(c9692854208, self).__init__(gameobject.Characteristics(**{'name': 'Goblin Locksmith', 'text': "Whenever this creature attacks, creatures with defender can't block this turn.", 'color': ['R'], 'mana_cost': '1R', 'power': 2, 'toughness': 1, 'subtype': ['Goblin', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452924(card.Card):
    "Goblin Electromancer"
    def __init__(self):
        super(c452924, self).__init__(gameobject.Characteristics(**{'name': 'Goblin Electromancer', 'text': 'Instant and sorcery spells you cast cost {1} less to cast.', 'color': ['R', 'U'], 'mana_cost': 'UR', 'power': 2, 'toughness': 2, 'subtype': ['Goblin', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452852(card.Card):
    "Goblin Banneret"
    def __init__(self):
        super(c452852, self).__init__(gameobject.Characteristics(**{'name': 'Goblin Banneret', 'text': 'Mentor (Whenever this creature attacks, put a +1/+1 counter on target attacking creature with lesser power.)\n{1}{R}: This creature gets +2/+0 until end of turn.', 'color': ['R'], 'mana_cost': 'R', 'power': 1, 'toughness': 1, 'subtype': ['Goblin', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c253643(card.Card):
    "Gobbling Ooze"
    def __init__(self):
        super(c253643, self).__init__(gameobject.Characteristics(**{'name': 'Gobbling Ooze', 'text': '{G}, Sacrifice another creature: Put a +1/+1 counter on this creature.', 'color': ['G'], 'mana_cost': '4G', 'power': 3, 'toughness': 3, 'subtype': ['Ooze']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452923(card.Card):
    "Glowspore Shaman"
    def __init__(self):
        super(c452923, self).__init__(gameobject.Characteristics(**{'name': 'Glowspore Shaman', 'text': 'When this creature enters, mill three cards. You may put a land card from your graveyard on top of your library. (To mill a card, put the top card of your library into your graveyard.)', 'color': ['B', 'G'], 'mana_cost': 'BG', 'power': 3, 'toughness': 1, 'subtype': ['Elf', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c193557(card.Card):
    "Glory Seeker"
    def __init__(self):
        super(c193557, self).__init__(gameobject.Characteristics(**{'name': 'Glory Seeker', 'text': '', 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c213783(card.Card):
    "Glissa's Courier"
    def __init__(self):
        super(c213783, self).__init__(gameobject.Characteristics(**{'name': "Glissa's Courier", 'text': "Mountainwalk (This creature can't be blocked as long as defending player controls a Mountain.)", 'color': ['G'], 'mana_cost': '1GG', 'power': 2, 'toughness': 3, 'subtype': ['Phyrexian', 'Horror']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Mountainwalk]))

class c452986(card.Card):
    "Glaive of the Guildpact"
    def __init__(self):
        super(c452986, self).__init__(gameobject.Characteristics(**{'name': 'Glaive of the Guildpact', 'text': "Equipped creature gets +1/+0 for each Gate you control and has vigilance and menace. (A creature with menace can't be blocked except by two or more creatures.)\nEquip {3} ({3}: Attach to target creature you control. Equip only as a sorcery.)", 'color': [], 'mana_cost': '2', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c452762(card.Card):
    "Gird for Battle"
    def __init__(self):
        super(c452762, self).__init__(gameobject.Characteristics(**{'name': 'Gird for Battle', 'text': 'Put a +1/+1 counter on each of up to two target creatures.', 'color': ['W'], 'mana_cost': 'W'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c9629911349(card.Card):
    "Giott, King of the Dwarves"
    def __init__(self):
        super(c9629911349, self).__init__(gameobject.Characteristics(**{'name': 'Giott, King of the Dwarves', 'text': 'Double strike\nWhenever Giott or another Dwarf you control enters and whenever an Equipment you control enters, you may discard a card. If you do, draw a card.', 'color': ['R', 'W'], 'mana_cost': 'RW', 'power': 1, 'toughness': 1, 'subtype': ['Dwarf', 'Noble']}, supertype=[cardtype.SuperType.LEGENDARY], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Double_Strike]))

class c9860597468(card.Card):
    "Gideon's Lawkeeper"
    def __init__(self):
        super(c9860597468, self).__init__(gameobject.Characteristics(**{'name': "Gideon's Lawkeeper", 'text': '{W}, {T}: Tap target creature.', 'color': ['W'], 'mana_cost': 'W', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373373(card.Card):
    "Ghor-Clan Savage"
    def __init__(self):
        super(c373373, self).__init__(gameobject.Characteristics(**{'name': 'Ghor-Clan Savage', 'text': 'Bloodthirst 3 (If an opponent was dealt damage this turn, this creature enters with three +1/+1 counters on it.)', 'color': ['G'], 'mana_cost': '3GG', 'power': 2, 'toughness': 3, 'subtype': ['Centaur', 'Berserker']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c194124(card.Card):
    "Ghalma's Warden"
    def __init__(self):
        super(c194124, self).__init__(gameobject.Characteristics(**{'name': "Ghalma's Warden", 'text': 'Metalcraft — This creature gets +2/+2 as long as you control three or more artifacts.', 'color': ['W'], 'mana_cost': '3W', 'power': 2, 'toughness': 4, 'subtype': ['Elephant', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452879(card.Card):
    "Generous Stray"
    def __init__(self):
        super(c452879, self).__init__(gameobject.Characteristics(**{'name': 'Generous Stray', 'text': 'When this creature enters, draw a card.', 'color': ['G'], 'mana_cost': '2G', 'power': 1, 'toughness': 2, 'subtype': ['Cat']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c417589(card.Card):
    "Gearshift Ace"
    def __init__(self):
        super(c417589, self).__init__(gameobject.Characteristics(**{'name': 'Gearshift Ace', 'text': 'First strike\nWhenever this creature crews a Vehicle, that Vehicle gains first strike until end of turn.', 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 1, 'subtype': ['Dwarf', 'Pilot']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.First_Strike]))

class c262685(card.Card):
    "Gavony Ironwright"
    def __init__(self):
        super(c262685, self).__init__(gameobject.Characteristics(**{'name': 'Gavony Ironwright', 'text': 'Fateful hour — As long as you have 5 or less life, other creatures you control get +1/+4.', 'color': ['W'], 'mana_cost': '2W', 'power': 1, 'toughness': 4, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452985(card.Card):
    "Gatekeeper Gargoyle"
    def __init__(self):
        super(c452985, self).__init__(gameobject.Characteristics(**{'name': 'Gatekeeper Gargoyle', 'text': 'Flying\nThis creature enters with a +1/+1 counter on it for each Gate you control.', 'color': [], 'mana_cost': '6', 'power': 3, 'toughness': 3, 'subtype': ['Gargoyle']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c426930(card.Card):
    "Gate to the Afterlife"
    def __init__(self):
        super(c426930, self).__init__(gameobject.Characteristics(**{'name': 'Gate to the Afterlife', 'text': "Whenever a nontoken creature you control dies, you gain 1 life. Then you may draw a card. If you do, discard a card.\n{2}, {T}, Sacrifice this artifact: Search your graveyard, hand, and/or library for a card named God-Pharaoh's Gift and put it onto the battlefield. If you search your library this way, shuffle. Activate only if there are six or more creature cards in your graveyard.", 'color': [], 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c452922(card.Card):
    "Garrison Sergeant"
    def __init__(self):
        super(c452922, self).__init__(gameobject.Characteristics(**{'name': 'Garrison Sergeant', 'text': 'This creature has double strike as long as you control a Gate.', 'color': ['R', 'W'], 'mana_cost': '3RW', 'power': 3, 'toughness': 3, 'subtype': ['Lizard', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9344104347(card.Card):
    "Gaelicat"
    def __init__(self):
        super(c9344104347, self).__init__(gameobject.Characteristics(**{'name': 'Gaelicat', 'text': 'Flying, vigilance\nAs long as you control two or more artifacts, this creature gets +2/+0.', 'color': ['W'], 'mana_cost': '2W', 'power': 1, 'toughness': 3, 'subtype': ['Cat']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Vigilance]))

class c180361(card.Card):
    "Frontier Guide"
    def __init__(self):
        super(c180361, self).__init__(gameobject.Characteristics(**{'name': 'Frontier Guide', 'text': '{3}{G}, {T}: Search your library for a basic land card, put it onto the battlefield tapped, then shuffle.', 'color': ['G'], 'mana_cost': '1G', 'power': 1, 'toughness': 1, 'subtype': ['Elf', 'Scout']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9955635435(card.Card):
    "Fretwork Colony"
    def __init__(self):
        super(c9955635435, self).__init__(gameobject.Characteristics(**{'name': 'Fretwork Colony', 'text': "This creature can't block.\nAt the beginning of your upkeep, put a +1/+1 counter on this creature and you lose 1 life.", 'color': ['B'], 'mana_cost': '1B', 'power': 1, 'toughness': 1, 'subtype': ['Insect']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c107253(card.Card):
    "Freewind Equenaut"
    def __init__(self):
        super(c107253, self).__init__(gameobject.Characteristics(**{'name': 'Freewind Equenaut', 'text': 'Flying\nAs long as this creature is enchanted, it has "{T}: This creature deals 2 damage to target attacking or blocking creature."', 'color': ['W'], 'mana_cost': '2W', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Archer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c423726(card.Card):
    "Foundry Hornet"
    def __init__(self):
        super(c423726, self).__init__(gameobject.Characteristics(**{'name': 'Foundry Hornet', 'text': 'Flying\nWhen this creature enters, if you control a creature with a +1/+1 counter on it, creatures your opponents control get -1/-1 until end of turn.', 'color': ['B'], 'mana_cost': '3B', 'power': 2, 'toughness': 3, 'subtype': ['Insect']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c447387(card.Card):
    "Forsaken Sanctuary"
    def __init__(self):
        super(c447387, self).__init__(gameobject.Characteristics(**{'name': 'Forsaken Sanctuary', 'text': 'This land enters tapped.\n{T}: Add {W} or {B}.', 'color': ['B', 'W'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c681250(card.Card):
    "Forest"
    def __init__(self):
        super(c681250, self).__init__(gameobject.Characteristics(**{'name': 'Forest', 'text': '({T}: Add {G}.)', 'color': ['G'], 'mana_cost': '', 'subtype': ['Forest']}, supertype=[cardtype.SuperType.BASIC], types=[cardtype.CardType.LAND], abilities=[]))

class c9324722849(card.Card):
    "Fog Bank"
    def __init__(self):
        super(c9324722849, self).__init__(gameobject.Characteristics(**{'name': 'Fog Bank', 'text': "Defender (This creature can't attack.)\nFlying\nPrevent all combat damage that would be dealt to and dealt by this creature.", 'color': ['U'], 'mana_cost': '1U', 'power': 0, 'toughness': 2, 'subtype': ['Wall']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Defender]))

class c452976(card.Card):
    "Flower"
    def __init__(self):
        super(c452976, self).__init__(gameobject.Characteristics(**{'name': 'Flower', 'text': '', 'color': ['G', 'W'], 'mana_cost': 'G/W // 4GW'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c413708(card.Card):
    "Flinthoof Boar"
    def __init__(self):
        super(c413708, self).__init__(gameobject.Characteristics(**{'name': 'Flinthoof Boar', 'text': 'This creature gets +1/+1 as long as you control a Mountain.\n{R}: This creature gains haste until end of turn. (It can attack and {T} this turn.)', 'color': ['G', 'R'], 'mana_cost': '1G', 'power': 2, 'toughness': 2, 'subtype': ['Boar']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452761(card.Card):
    "Flight of Equenauts"
    def __init__(self):
        super(c452761, self).__init__(gameobject.Characteristics(**{'name': 'Flight of Equenauts', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nFlying", 'color': ['W'], 'mana_cost': '7W', 'power': 4, 'toughness': 5, 'subtype': ['Human', 'Knight']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Convoke]))

class c373501(card.Card):
    "Fleetfeather Sandals"
    def __init__(self):
        super(c373501, self).__init__(gameobject.Characteristics(**{'name': 'Fleetfeather Sandals', 'text': 'Equipped creature has flying and haste.\nEquip {2} ({2}: Attach to target creature you control. Equip only as a sorcery.)', 'color': [], 'mana_cost': '2', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c373705(card.Card):
    "Flamespeaker Adept"
    def __init__(self):
        super(c373705, self).__init__(gameobject.Characteristics(**{'name': 'Flamespeaker Adept', 'text': 'Whenever you scry, this creature gets +2/+0 and gains first strike until end of turn.', 'color': ['R'], 'mana_cost': '2R', 'power': 2, 'toughness': 3, 'subtype': ['Human', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373514(card.Card):
    "Flamecast Wheel"
    def __init__(self):
        super(c373514, self).__init__(gameobject.Characteristics(**{'name': 'Flamecast Wheel', 'text': '{5}, {T}, Sacrifice this artifact: It deals 3 damage to target creature.', 'color': [], 'mana_cost': '1'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c366311(card.Card):
    "Firefist Striker"
    def __init__(self):
        super(c366311, self).__init__(gameobject.Characteristics(**{'name': 'Firefist Striker', 'text': "Battalion — Whenever this creature and at least two other creatures attack, target creature can't block this turn.", 'color': ['R'], 'mana_cost': '1R', 'power': 2, 'toughness': 1, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9391221148(card.Card):
    "Fire Elemental"
    def __init__(self):
        super(c9391221148, self).__init__(gameobject.Characteristics(**{'name': 'Fire Elemental', 'text': '', 'color': ['R'], 'mana_cost': '3RR', 'power': 5, 'toughness': 4, 'subtype': ['Elemental']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c380200(card.Card):
    "Festerhide Boar"
    def __init__(self):
        super(c380200, self).__init__(gameobject.Characteristics(**{'name': 'Festerhide Boar', 'text': 'Trample\nMorbid — This creature enters with two +1/+1 counters on it if a creature died this turn.', 'color': ['G'], 'mana_cost': '3G', 'power': 3, 'toughness': 3, 'subtype': ['Boar']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample]))

class c368969(card.Card):
    "Feral Animist"
    def __init__(self):
        super(c368969, self).__init__(gameobject.Characteristics(**{'name': 'Feral Animist', 'text': '{3}: This creature gets +X/+0 until end of turn, where X is its power.', 'color': ['G', 'R'], 'mana_cost': '1RG', 'power': 2, 'toughness': 1, 'subtype': ['Goblin', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9281093626(card.Card):
    "Fencing Ace"
    def __init__(self):
        super(c9281093626, self).__init__(gameobject.Characteristics(**{'name': 'Fencing Ace', 'text': 'Double strike (This creature deals both first-strike and regular combat damage.)', 'color': ['W'], 'mana_cost': '1W', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Double_Strike]))

class c469882(card.Card):
    "Fearless Halberdier"
    def __init__(self):
        super(c469882, self).__init__(gameobject.Characteristics(**{'name': 'Fearless Halberdier', 'text': '', 'color': ['R'], 'mana_cost': '2R', 'power': 3, 'toughness': 2, 'subtype': ['Human', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c290536(card.Card):
    "Fall of the Gavel"
    def __init__(self):
        super(c290536, self).__init__(gameobject.Characteristics(**{'name': 'Fall of the Gavel', 'text': 'Counter target spell. You gain 5 life.', 'color': ['U', 'W'], 'mana_cost': '3WU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c9331567487(card.Card):
    "Fade into Antiquity"
    def __init__(self):
        super(c9331567487, self).__init__(gameobject.Characteristics(**{'name': 'Fade into Antiquity', 'text': 'Exile target artifact or enchantment.', 'color': ['G'], 'mana_cost': '2G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c194092(card.Card):
    "Ezuri's Archers"
    def __init__(self):
        super(c194092, self).__init__(gameobject.Characteristics(**{'name': "Ezuri's Archers", 'text': 'Reach (This creature can block creatures with flying.)\nWhenever this creature blocks a creature with flying, this creature gets +3/+0 until end of turn.', 'color': ['G'], 'mana_cost': 'G', 'power': 1, 'toughness': 2, 'subtype': ['Elf', 'Archer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Reach]))

class c417619(card.Card):
    "Experimental Aviator"
    def __init__(self):
        super(c417619, self).__init__(gameobject.Characteristics(**{'name': 'Experimental Aviator', 'text': 'Flying\nWhen this creature enters, create two 1/1 colorless Thopter artifact creature tokens with flying.', 'color': ['U'], 'mana_cost': '3UU', 'power': 0, 'toughness': 3, 'subtype': ['Human', 'Artificer']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c9852067439(card.Card):
    "Experiment One"
    def __init__(self):
        super(c9852067439, self).__init__(gameobject.Characteristics(**{'name': 'Experiment One', 'text': 'Evolve (Whenever a creature you control enters, if that creature has greater power or toughness than this creature, put a +1/+1 counter on this creature.)\nRemove two +1/+1 counters from this creature: Regenerate it. (The next time this creature would be destroyed this turn, instead tap it, remove it from combat, and heal all damage on it.)', 'color': ['G'], 'mana_cost': 'G', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Ooze']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c668403(card.Card):
    "Escarpment Fortress"
    def __init__(self):
        super(c668403, self).__init__(gameobject.Characteristics(**{'name': 'Escarpment Fortress', 'text': "Defender (This creature can't attack.)\nReach (This creature can block creatures with flying.)\nOther creatures you control get +1/+0.\nWhenever you attack with two or more creatures, draw a card.", 'color': ['W'], 'mana_cost': '4W', 'power': 3, 'toughness': 5, 'subtype': ['Wall']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Reach, static_abilities.StaticAbilities.Defender]))

class c417618(card.Card):
    "Era of Innovation"
    def __init__(self):
        super(c417618, self).__init__(gameobject.Characteristics(**{'name': 'Era of Innovation', 'text': 'Whenever an artifact or Artificer you control enters, you may pay {1}. If you do, you get {E}{E} (two energy counters).\nPay six {E}, Sacrifice this enchantment: Draw three cards.', 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c373724(card.Card):
    "Ephara's Warden"
    def __init__(self):
        super(c373724, self).__init__(gameobject.Characteristics(**{'name': "Ephara's Warden", 'text': '{T}: Tap target creature with power 3 or less.', 'color': ['W'], 'mana_cost': '3W', 'power': 1, 'toughness': 2, 'subtype': ['Human', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c423747(card.Card):
    "Enraged Giant"
    def __init__(self):
        super(c423747, self).__init__(gameobject.Characteristics(**{'name': 'Enraged Giant', 'text': "Improvise (Your artifacts can help cast this spell. Each artifact you tap after you're done activating mana abilities pays for {1}.)\nTrample, haste", 'color': ['R'], 'mana_cost': '5R', 'power': 4, 'toughness': 4, 'subtype': ['Giant']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Improvise, static_abilities.StaticAbilities.Haste, static_abilities.StaticAbilities.Trample]))

class c452790(card.Card):
    "Enhanced Surveillance"
    def __init__(self):
        super(c452790, self).__init__(gameobject.Characteristics(**{'name': 'Enhanced Surveillance', 'text': 'You may look at an additional two cards each time you surveil.\nExile this enchantment: Shuffle your graveyard into your library.', 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c426929(card.Card):
    "Embalmer's Tools"
    def __init__(self):
        super(c426929, self).__init__(gameobject.Characteristics(**{'name': "Embalmer's Tools", 'text': 'Activated abilities of creature cards in your graveyard cost {1} less to activate.\nTap an untapped Zombie you control: Target player mills a card.', 'color': [], 'mana_cost': '2'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c456611(card.Card):
    "Emancipation Angel"
    def __init__(self):
        super(c456611, self).__init__(gameobject.Characteristics(**{'name': 'Emancipation Angel', 'text': "Flying\nWhen this creature enters, return a permanent you control to its owner's hand.", 'color': ['W'], 'mana_cost': '1WW', 'power': 3, 'toughness': 3, 'subtype': ['Angel']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c253545(card.Card):
    "Electrickery"
    def __init__(self):
        super(c253545, self).__init__(gameobject.Characteristics(**{'name': 'Electrickery', 'text': 'Electrickery deals 1 damage to target creature you don\'t control.\nOverload {1}{R} (You may cast this spell for its overload cost. If you do, change "target" in its text to "each.")', 'color': ['R'], 'mana_cost': 'R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c426928(card.Card):
    "Edifice of Authority"
    def __init__(self):
        super(c426928, self).__init__(gameobject.Characteristics(**{'name': 'Edifice of Authority', 'text': "{1}, {T}: Target creature can't attack this turn. Put a brick counter on this artifact.\n{1}, {T}: Until your next turn, target creature can't attack or block and its activated abilities can't be activated. Activate only if there are three or more brick counters on this artifact.", 'color': [], 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c289226(card.Card):
    "Dryad Militant"
    def __init__(self):
        super(c289226, self).__init__(gameobject.Characteristics(**{'name': 'Dryad Militant', 'text': '({G/W} can be paid with either {G} or {W}.)\nIf an instant or sorcery card would be put into a graveyard from anywhere, exile it instead.', 'color': ['G', 'W'], 'mana_cost': 'G/W', 'power': 2, 'toughness': 1, 'subtype': ['Dryad', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c446141(card.Card):
    "Dragon Hatchling"
    def __init__(self):
        super(c446141, self).__init__(gameobject.Characteristics(**{'name': 'Dragon Hatchling', 'text': 'Flying\n{R}: This creature gets +1/+0 until end of turn.', 'color': ['R'], 'mana_cost': '1R', 'power': 0, 'toughness': 1, 'subtype': ['Dragon']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c452820(card.Card):
    "Douser of Lights"
    def __init__(self):
        super(c452820, self).__init__(gameobject.Characteristics(**{'name': 'Douser of Lights', 'text': '', 'color': ['B'], 'mana_cost': '4B', 'power': 4, 'toughness': 5, 'subtype': ['Horror']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c429890(card.Card):
    "Divine Verdict"
    def __init__(self):
        super(c429890, self).__init__(gameobject.Characteristics(**{'name': 'Divine Verdict', 'text': 'Destroy target attacking or blocking creature.', 'color': ['W'], 'mana_cost': '3W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c9183642423(card.Card):
    "Divine Favor"
    def __init__(self):
        super(c9183642423, self).__init__(gameobject.Characteristics(**{'name': 'Divine Favor', 'text': 'Enchant creature\nWhen this Aura enters, you gain 3 life.\nEnchanted creature gets +1/+3.', 'color': ['W'], 'mana_cost': '1W', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c452878(card.Card):
    "District Guide"
    def __init__(self):
        super(c452878, self).__init__(gameobject.Characteristics(**{'name': 'District Guide', 'text': 'When this creature enters, you may search your library for a basic land card or Gate card, reveal it, put it into your hand, then shuffle.', 'color': ['G'], 'mana_cost': '2G', 'power': 2, 'toughness': 2, 'subtype': ['Elf', 'Scout']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452917(card.Card):
    "Disinformation Campaign"
    def __init__(self):
        super(c452917, self).__init__(gameobject.Characteristics(**{'name': 'Disinformation Campaign', 'text': "When this enchantment enters, you draw a card and each opponent discards a card.\nWhenever you surveil, return this enchantment to its owner's hand.", 'color': ['B', 'U'], 'mana_cost': '1UB'}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c446776(card.Card):
    "Disdainful Stroke"
    def __init__(self):
        super(c446776, self).__init__(gameobject.Characteristics(**{'name': 'Disdainful Stroke', 'text': 'Counter target spell with mana value 4 or greater.', 'color': ['U'], 'mana_cost': '1U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c373520(card.Card):
    "Disciple of Phenax"
    def __init__(self):
        super(c373520, self).__init__(gameobject.Characteristics(**{'name': 'Disciple of Phenax', 'text': 'When this creature enters, target player reveals a number of cards from their hand equal to your devotion to black. You choose one of them. That player discards that card. (Each {B} in the mana costs of permanents you control counts toward your devotion to black.)', 'color': ['B'], 'mana_cost': '2BB', 'power': 1, 'toughness': 3, 'subtype': ['Human', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c417616(card.Card):
    "Disappearing Act"
    def __init__(self):
        super(c417616, self).__init__(gameobject.Characteristics(**{'name': 'Disappearing Act', 'text': "As an additional cost to cast this spell, return a permanent you control to its owner's hand.\nCounter target spell.", 'color': ['U'], 'mana_cost': '1UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452916(card.Card):
    "Dimir Spybug"
    def __init__(self):
        super(c452916, self).__init__(gameobject.Characteristics(**{'name': 'Dimir Spybug', 'text': "Flying\nMenace (This creature can't be blocked except by two or more creatures.)\nWhenever you surveil, put a +1/+1 counter on this creature.", 'color': ['B', 'U'], 'mana_cost': 'UB', 'power': 1, 'toughness': 1, 'subtype': ['Insect']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.Menace]))

class c496049(card.Card):
    "Dimir Locket"
    def __init__(self):
        super(c496049, self).__init__(gameobject.Characteristics(**{'name': 'Dimir Locket', 'text': '{T}: Add {U} or {B}.\n{U/B}{U/B}{U/B}{U/B}, {T}, Sacrifice this artifact: Draw two cards.', 'color': ['B', 'U'], 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c482715(card.Card):
    "Devout Chaplain"
    def __init__(self):
        super(c482715, self).__init__(gameobject.Characteristics(**{'name': 'Devout Chaplain', 'text': '{T}, Tap two untapped Humans you control: Exile target artifact or enchantment.', 'color': ['W'], 'mana_cost': '2W', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452785(card.Card):
    "Devious Cover-Up"
    def __init__(self):
        super(c452785, self).__init__(gameobject.Characteristics(**{'name': 'Devious Cover-Up', 'text': "Counter target spell. If that spell is countered this way, exile it instead of putting it into its owner's graveyard. You may shuffle up to four target cards from your graveyard into your library.", 'color': ['U'], 'mana_cost': '2UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c426919(card.Card):
    "Destined"
    def __init__(self):
        super(c426919, self).__init__(gameobject.Characteristics(**{'name': 'Destined', 'text': '', 'color': ['B', 'G'], 'mana_cost': '1B // 3G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452759(card.Card):
    "Demotion"
    def __init__(self):
        super(c452759, self).__init__(gameobject.Characteristics(**{'name': 'Demotion', 'text': "Enchant creature\nEnchanted creature can't block, and its activated abilities can't be activated.", 'color': ['W'], 'mana_cost': 'W', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c423684(card.Card):
    "Deft Dismissal"
    def __init__(self):
        super(c423684, self).__init__(gameobject.Characteristics(**{'name': 'Deft Dismissal', 'text': 'Deft Dismissal deals 3 damage divided as you choose among one, two, or three target attacking or blocking creatures.', 'color': ['W'], 'mana_cost': '3W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c426865(card.Card):
    "Defiant Greatmaw"
    def __init__(self):
        super(c426865, self).__init__(gameobject.Characteristics(**{'name': 'Defiant Greatmaw', 'text': 'When this creature enters, put two -1/-1 counters on target creature you control.\nWhenever you put one or more -1/-1 counters on this creature, remove a -1/-1 counter from another target creature you control.', 'color': ['G'], 'mana_cost': '2G', 'power': 4, 'toughness': 5, 'subtype': ['Hippo']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373623(card.Card):
    "Defend the Hearth"
    def __init__(self):
        super(c373623, self).__init__(gameobject.Characteristics(**{'name': 'Defend the Hearth', 'text': 'Prevent all combat damage that would be dealt to players this turn.', 'color': ['G'], 'mana_cost': '1G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c366268(card.Card):
    "Debtor's Pulpit"
    def __init__(self):
        super(c366268, self).__init__(gameobject.Characteristics(**{'name': "Debtor's Pulpit", 'text': 'Enchant land\nEnchanted land has "{T}: Tap target creature."', 'color': ['W'], 'mana_cost': '4W', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c366254(card.Card):
    "Deathcult Rogue"
    def __init__(self):
        super(c366254, self).__init__(gameobject.Characteristics(**{'name': 'Deathcult Rogue', 'text': "This creature can't be blocked except by Rogues.", 'color': ['B', 'U'], 'mana_cost': '1U/BU/B', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452818(card.Card):
    "Deadly Visit"
    def __init__(self):
        super(c452818, self).__init__(gameobject.Characteristics(**{'name': 'Deadly Visit', 'text': 'Destroy target creature.\nSurveil 2. (Look at the top two cards of your library, then put any number of them into your graveyard and the rest on top of your library in any order.)', 'color': ['B'], 'mana_cost': '3BB'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c423682(card.Card):
    "Deadeye Harpooner"
    def __init__(self):
        super(c423682, self).__init__(gameobject.Characteristics(**{'name': 'Deadeye Harpooner', 'text': 'Revolt — When this creature enters, if a permanent left the battlefield under your control this turn, destroy target tapped creature an opponent controls.', 'color': ['W'], 'mana_cost': '2W', 'power': 2, 'toughness': 2, 'subtype': ['Dwarf', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c409853(card.Card):
    "Dead Weight"
    def __init__(self):
        super(c409853, self).__init__(gameobject.Characteristics(**{'name': 'Dead Weight', 'text': 'Enchant creature\nEnchanted creature gets -2/-2.', 'color': ['B'], 'mana_cost': 'B', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c370721(card.Card):
    "Dawnstrike Paladin"
    def __init__(self):
        super(c370721, self).__init__(gameobject.Characteristics(**{'name': 'Dawnstrike Paladin', 'text': "Vigilance (Attacking doesn't cause this creature to tap.)\nLifelink (Damage dealt by this creature also causes you to gain that much life.)", 'color': ['W'], 'mana_cost': '3WW', 'power': 2, 'toughness': 4, 'subtype': ['Human', 'Knight']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Lifelink, static_abilities.StaticAbilities.Vigilance]))

class c452914(card.Card):
    "Darkblade Agent"
    def __init__(self):
        super(c452914, self).__init__(gameobject.Characteristics(**{'name': 'Darkblade Agent', 'text': 'As long as you\'ve surveilled this turn, this creature has deathtouch and "Whenever this creature deals combat damage to a player, you draw a card."', 'color': ['B', 'U'], 'mana_cost': '1UB', 'power': 2, 'toughness': 3, 'subtype': ['Human', 'Assassin']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c205477(card.Card):
    "Cystbearer"
    def __init__(self):
        super(c205477, self).__init__(gameobject.Characteristics(**{'name': 'Cystbearer', 'text': 'Infect (This creature deals damage to creatures in the form of -1/-1 counters and to players in the form of poison counters.)', 'color': ['G'], 'mana_cost': '2G', 'power': 2, 'toughness': 3, 'subtype': ['Phyrexian', 'Beast']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Infect]))

class c430858(card.Card):
    "Crypt of the Eternals"
    def __init__(self):
        super(c430858, self).__init__(gameobject.Characteristics(**{'name': 'Crypt of the Eternals', 'text': 'When this land enters, you gain 1 life.\n{T}: Add {C}.\n{1}, {T}: Add {U}, {B}, or {R}.', 'color': ['B', 'R', 'U'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c452757(card.Card):
    "Crush Contraband"
    def __init__(self):
        super(c452757, self).__init__(gameobject.Characteristics(**{'name': 'Crush Contraband', 'text': 'Choose one or both —\n• Exile target artifact.\n• Exile target enchantment.', 'color': ['W'], 'mana_cost': '3W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c9519340883(card.Card):
    "Crowned Ceratok"
    def __init__(self):
        super(c9519340883, self).__init__(gameobject.Characteristics(**{'name': 'Crowned Ceratok', 'text': 'Trample\nEach creature you control with a +1/+1 counter on it has trample.', 'color': ['G'], 'mana_cost': '3G', 'power': 4, 'toughness': 3, 'subtype': ['Rhino']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample]))

class c426864(card.Card):
    "Crocodile of the Crossing"
    def __init__(self):
        super(c426864, self).__init__(gameobject.Characteristics(**{'name': 'Crocodile of the Crossing', 'text': 'Haste\nWhen this creature enters, put a -1/-1 counter on target creature you control.', 'color': ['G'], 'mana_cost': '3G', 'power': 5, 'toughness': 4, 'subtype': ['Crocodile']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c366319(card.Card):
    "Crocanura"
    def __init__(self):
        super(c366319, self).__init__(gameobject.Characteristics(**{'name': 'Crocanura', 'text': 'Reach (This creature can block creatures with flying.)\nEvolve (Whenever a creature you control enters, if that creature has greater power or toughness than this creature, put a +1/+1 counter on this creature.)', 'color': ['G'], 'mana_cost': '2G', 'power': 1, 'toughness': 3, 'subtype': ['Crocodile', 'Frog']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Reach]))

class c253699(card.Card):
    "Craterize"
    def __init__(self):
        super(c253699, self).__init__(gameobject.Characteristics(**{'name': 'Craterize', 'text': 'Destroy target land.', 'color': ['R'], 'mana_cost': '3R'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c373588(card.Card):
    "Crackling Triton"
    def __init__(self):
        super(c373588, self).__init__(gameobject.Characteristics(**{'name': 'Crackling Triton', 'text': '{2}{R}, Sacrifice this creature: It deals 2 damage to any target.', 'color': ['R', 'U'], 'mana_cost': '2U', 'power': 2, 'toughness': 3, 'subtype': ['Merfolk', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9151931344(card.Card):
    "Cower in Fear"
    def __init__(self):
        super(c9151931344, self).__init__(gameobject.Characteristics(**{'name': 'Cower in Fear', 'text': 'Creatures your opponents control get -1/-1 until end of turn.', 'color': ['B'], 'mana_cost': '1BB'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c276475(card.Card):
    "Courtly Provocateur"
    def __init__(self):
        super(c276475, self).__init__(gameobject.Characteristics(**{'name': 'Courtly Provocateur', 'text': '{T}: Target creature attacks this turn if able.\n{T}: Target creature blocks this turn if able.', 'color': ['U'], 'mana_cost': '2U', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9343121793(card.Card):
    "Court Street Denizen"
    def __init__(self):
        super(c9343121793, self).__init__(gameobject.Characteristics(**{'name': 'Court Street Denizen', 'text': 'Whenever another white creature you control enters, tap target creature an opponent controls.', 'color': ['W'], 'mana_cost': '2W', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c622689(card.Card):
    "Counterspell"
    def __init__(self):
        super(c622689, self).__init__(gameobject.Characteristics(**{'name': 'Counterspell', 'text': 'Counter target spell.', 'color': ['U'], 'mana_cost': 'UU'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c662208(card.Card):
    "Corrupted Shapeshifter"
    def __init__(self):
        super(c662208, self).__init__(gameobject.Characteristics(**{'name': 'Corrupted Shapeshifter', 'text': 'Devoid (This card has no color.)\nAs this creature enters, it becomes your choice of a 3/3 creature with flying, a 2/5 creature with vigilance, or a 0/12 creature with defender.', 'color': ['U'], 'mana_cost': '3U', 'power': '*', 'toughness': '*', 'subtype': ['Eldrazi', 'Shapeshifter']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c380254(card.Card):
    "Corpse Traders"
    def __init__(self):
        super(c380254, self).__init__(gameobject.Characteristics(**{'name': 'Corpse Traders', 'text': '{2}{B}, Sacrifice a creature: Target opponent reveals their hand. You choose a card from it. That player discards that card. Activate only as a sorcery.', 'color': ['B'], 'mana_cost': '3B', 'power': 3, 'toughness': 3, 'subtype': ['Human', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9874362467(card.Card):
    "Consign"
    def __init__(self):
        super(c9874362467, self).__init__(gameobject.Characteristics(**{'name': 'Consign', 'text': '', 'color': ['B', 'U'], 'mana_cost': '1U // 4B'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452912(card.Card):
    "Conclave Guildmage"
    def __init__(self):
        super(c452912, self).__init__(gameobject.Characteristics(**{'name': 'Conclave Guildmage', 'text': '{G}, {T}: Creatures you control gain trample until end of turn.\n{5}{W}, {T}: Create a 2/2 green and white Elf Knight creature token with vigilance.', 'color': ['G', 'W'], 'mana_cost': 'GW', 'power': 2, 'toughness': 2, 'subtype': ['Elf', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452911(card.Card):
    "Conclave Cavalier"
    def __init__(self):
        super(c452911, self).__init__(gameobject.Characteristics(**{'name': 'Conclave Cavalier', 'text': 'Vigilance\nWhen this creature dies, create two 2/2 green and white Elf Knight creature tokens with vigilance.', 'color': ['G', 'W'], 'mana_cost': 'GGWW', 'power': 4, 'toughness': 4, 'subtype': ['Centaur', 'Knight']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance]))

class c9641209184(card.Card):
    "Cobblebrute"
    def __init__(self):
        super(c9641209184, self).__init__(gameobject.Characteristics(**{'name': 'Cobblebrute', 'text': '', 'color': ['R'], 'mana_cost': '3R', 'power': 5, 'toughness': 2, 'subtype': ['Elemental']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c366363(card.Card):
    "Clinging Anemones"
    def __init__(self):
        super(c366363, self).__init__(gameobject.Characteristics(**{'name': 'Clinging Anemones', 'text': 'Defender\nEvolve (Whenever a creature you control enters, if that creature has greater power or toughness than this creature, put a +1/+1 counter on this creature.)', 'color': ['U'], 'mana_cost': '3U', 'power': 1, 'toughness': 4, 'subtype': ['Jellyfish']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c9628882442(card.Card):
    "Claustrophobia"
    def __init__(self):
        super(c9628882442, self).__init__(gameobject.Characteristics(**{'name': 'Claustrophobia', 'text': "Enchant creature\nWhen this Aura enters, tap enchanted creature.\nEnchanted creature doesn't untap during its controller's untap step.", 'color': ['U'], 'mana_cost': '1UU', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c9630278408(card.Card):
    "Citywatch Sphinx"
    def __init__(self):
        super(c9630278408, self).__init__(gameobject.Characteristics(**{'name': 'Citywatch Sphinx', 'text': 'Flying\nWhen this creature dies, surveil 2. (Look at the top two cards of your library, then put any number of them into your graveyard and the rest on top of your library in any order.)', 'color': ['U'], 'mana_cost': '5U', 'power': 5, 'toughness': 4, 'subtype': ['Sphinx']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c680774(card.Card):
    "Circuitous Route"
    def __init__(self):
        super(c680774, self).__init__(gameobject.Characteristics(**{'name': 'Circuitous Route', 'text': 'Search your library for up to two basic land cards and/or Gate cards, put them onto the battlefield tapped, then shuffle.', 'color': ['G'], 'mana_cost': '3G'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c470781(card.Card):
    "Cinder Barrens"
    def __init__(self):
        super(c470781, self).__init__(gameobject.Characteristics(**{'name': 'Cinder Barrens', 'text': 'This land enters tapped.\n{T}: Add {B} or {R}.', 'color': ['B', 'R'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c438762(card.Card):
    "Chronicler of Heroes"
    def __init__(self):
        super(c438762, self).__init__(gameobject.Characteristics(**{'name': 'Chronicler of Heroes', 'text': 'When this creature enters, draw a card if you control a creature with a +1/+1 counter on it.', 'color': ['G', 'W'], 'mana_cost': '1GW', 'power': 3, 'toughness': 3, 'subtype': ['Centaur', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9650735044(card.Card):
    "Child of Night"
    def __init__(self):
        super(c9650735044, self).__init__(gameobject.Characteristics(**{'name': 'Child of Night', 'text': 'Lifelink', 'color': ['B'], 'mana_cost': '1B', 'power': 2, 'toughness': 1, 'subtype': ['Vampire']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Lifelink]))

class c370768(card.Card):
    "Charging Griffin"
    def __init__(self):
        super(c370768, self).__init__(gameobject.Characteristics(**{'name': 'Charging Griffin', 'text': "Flying (This creature can't be blocked except by creatures with flying or reach.)\nWhenever this creature attacks, it gets +1/+1 until end of turn.", 'color': ['W'], 'mana_cost': '3W', 'power': 2, 'toughness': 2, 'subtype': ['Griffin']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c265387(card.Card):
    "Centaur's Herald"
    def __init__(self):
        super(c265387, self).__init__(gameobject.Characteristics(**{'name': "Centaur's Herald", 'text': '{2}{G}, Sacrifice this creature: Create a 3/3 green Centaur creature token.', 'color': ['G'], 'mana_cost': 'G', 'power': 0, 'toughness': 1, 'subtype': ['Elf', 'Scout']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452908(card.Card):
    "Centaur Peacemaker"
    def __init__(self):
        super(c452908, self).__init__(gameobject.Characteristics(**{'name': 'Centaur Peacemaker', 'text': 'When this creature enters, each player gains 4 life.', 'color': ['G', 'W'], 'mana_cost': '1GW', 'power': 3, 'toughness': 3, 'subtype': ['Centaur', 'Cleric']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9250992014(card.Card):
    "Centaur Courser"
    def __init__(self):
        super(c9250992014, self).__init__(gameobject.Characteristics(**{'name': 'Centaur Courser', 'text': '', 'color': ['G'], 'mana_cost': '2G', 'power': 3, 'toughness': 3, 'subtype': ['Centaur', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373594(card.Card):
    "Centaur Battlemaster"
    def __init__(self):
        super(c373594, self).__init__(gameobject.Characteristics(**{'name': 'Centaur Battlemaster', 'text': 'Heroic — Whenever you cast a spell that targets this creature, put three +1/+1 counters on this creature.', 'color': ['G'], 'mana_cost': '3GG', 'power': 3, 'toughness': 3, 'subtype': ['Centaur', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c482709(card.Card):
    "Cavalry Pegasus"
    def __init__(self):
        super(c482709, self).__init__(gameobject.Characteristics(**{'name': 'Cavalry Pegasus', 'text': 'Flying\nWhenever this creature attacks, each attacking Human gains flying until end of turn.', 'color': ['W'], 'mana_cost': '1W', 'power': 1, 'toughness': 1, 'subtype': ['Pegasus']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c185697(card.Card):
    "Caravan Hurda"
    def __init__(self):
        super(c185697, self).__init__(gameobject.Characteristics(**{'name': 'Caravan Hurda', 'text': 'Lifelink (Damage dealt by this creature also causes you to gain that much life.)', 'color': ['W'], 'mana_cost': '4W', 'power': 1, 'toughness': 5, 'subtype': ['Giant']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Lifelink]))

class c456367(card.Card):
    "Call of the Conclave"
    def __init__(self):
        super(c456367, self).__init__(gameobject.Characteristics(**{'name': 'Call of the Conclave', 'text': 'Create a 3/3 green Centaur creature token.', 'color': ['G', 'W'], 'mana_cost': 'GW'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c426627(card.Card):
    "Burning-Tree Emissary"
    def __init__(self):
        super(c426627, self).__init__(gameobject.Characteristics(**{'name': 'Burning-Tree Emissary', 'text': 'When this creature enters, add {R}{G}.', 'color': ['G', 'R'], 'mana_cost': 'R/GR/G', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452814(card.Card):
    "Burglar Rat"
    def __init__(self):
        super(c452814, self).__init__(gameobject.Characteristics(**{'name': 'Burglar Rat', 'text': 'When this creature enters, each opponent discards a card.', 'color': ['B'], 'mana_cost': '1B', 'power': 1, 'toughness': 1, 'subtype': ['Rat']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c265377(card.Card):
    "Brushstrider"
    def __init__(self):
        super(c265377, self).__init__(gameobject.Characteristics(**{'name': 'Brushstrider', 'text': "Vigilance (Attacking doesn't cause this creature to tap.)", 'color': ['G'], 'mana_cost': '1G', 'power': 3, 'toughness': 1, 'subtype': ['Beast']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Vigilance]))

class c205039(card.Card):
    "Brindle Boar"
    def __init__(self):
        super(c205039, self).__init__(gameobject.Characteristics(**{'name': 'Brindle Boar', 'text': 'Sacrifice this creature: You gain 4 life.', 'color': ['G'], 'mana_cost': '2G', 'power': 2, 'toughness': 2, 'subtype': ['Boar']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c563048(card.Card):
    "Breath Weapon"
    def __init__(self):
        super(c563048, self).__init__(gameobject.Characteristics(**{'name': 'Breath Weapon', 'text': 'Breath Weapon deals 2 damage to each non-Dragon creature.', 'color': ['R'], 'mana_cost': '2R'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c369028(card.Card):
    "Boros Mastiff"
    def __init__(self):
        super(c369028, self).__init__(gameobject.Characteristics(**{'name': 'Boros Mastiff', 'text': 'Battalion — Whenever this creature and at least two other creatures attack, this creature gains lifelink until end of turn. (Damage dealt by a creature with lifelink also causes its controller to gain that much life.)', 'color': ['W'], 'mana_cost': '1W', 'power': 2, 'toughness': 2, 'subtype': ['Dog']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c366369(card.Card):
    "Boros Elite"
    def __init__(self):
        super(c366369, self).__init__(gameobject.Characteristics(**{'name': 'Boros Elite', 'text': 'Battalion — Whenever this creature and at least two other creatures attack, this creature gets +2/+2 until end of turn.', 'color': ['W'], 'mana_cost': 'W', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9640101742(card.Card):
    "Boros Challenger"
    def __init__(self):
        super(c9640101742, self).__init__(gameobject.Characteristics(**{'name': 'Boros Challenger', 'text': 'Mentor (Whenever this creature attacks, put a +1/+1 counter on target attacking creature with lesser power.)\n{2}{R}{W}: This creature gets +1/+1 until end of turn.', 'color': ['R', 'W'], 'mana_cost': 'RW', 'power': 2, 'toughness': 3, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9250480449(card.Card):
    "Borderland Ranger"
    def __init__(self):
        super(c9250480449, self).__init__(gameobject.Characteristics(**{'name': 'Borderland Ranger', 'text': 'When this creature enters, you may search your library for a basic land card, reveal it, put it into your hand, then shuffle.', 'color': ['G'], 'mana_cost': '2G', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Scout', 'Ranger']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452843(card.Card):
    "Book Devourer"
    def __init__(self):
        super(c452843, self).__init__(gameobject.Characteristics(**{'name': 'Book Devourer', 'text': 'Trample\nWhenever this creature deals combat damage to a player, you may discard all the cards in your hand. If you do, draw that many cards.', 'color': ['R'], 'mana_cost': '5R', 'power': 4, 'toughness': 5, 'subtype': ['Beast']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample]))

class c417771(card.Card):
    "Bomat Bazaar Barge"
    def __init__(self):
        super(c417771, self).__init__(gameobject.Characteristics(**{'name': 'Bomat Bazaar Barge', 'text': 'When this Vehicle enters, draw a card.\nCrew 3 (Tap any number of creatures you control with total power 3 or more: This Vehicle becomes an artifact creature until end of turn.)', 'color': [], 'mana_cost': '4', 'subtype': ['Vehicle']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c253582(card.Card):
    "Blustersquall"
    def __init__(self):
        super(c253582, self).__init__(gameobject.Characteristics(**{'name': 'Blustersquall', 'text': 'Tap target creature you don\'t control.\nOverload {3}{U} (You may cast this spell for its overload cost. If you do, change "target" in its text to "each.")', 'color': ['U'], 'mana_cost': 'U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c370593(card.Card):
    "Blur Sliver"
    def __init__(self):
        super(c370593, self).__init__(gameobject.Characteristics(**{'name': 'Blur Sliver', 'text': 'Sliver creatures you control have haste. (They can attack and {T} as soon as they come under your control.)', 'color': ['R'], 'mana_cost': '2R', 'power': 2, 'toughness': 2, 'subtype': ['Sliver']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c289222(card.Card):
    "Blistercoil Weird"
    def __init__(self):
        super(c289222, self).__init__(gameobject.Characteristics(**{'name': 'Blistercoil Weird', 'text': 'Whenever you cast an instant or sorcery spell, this creature gets +1/+1 until end of turn. Untap it.', 'color': ['R', 'U'], 'mana_cost': 'U/R', 'power': 1, 'toughness': 1, 'subtype': ['Weird']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c213820(card.Card):
    "Blightwidow"
    def __init__(self):
        super(c213820, self).__init__(gameobject.Characteristics(**{'name': 'Blightwidow', 'text': 'Reach (This creature can block creatures with flying.)\nInfect (This creature deals damage to creatures in the form of -1/-1 counters and to players in the form of poison counters.)', 'color': ['G'], 'mana_cost': '3G', 'power': 2, 'toughness': 4, 'subtype': ['Phyrexian', 'Spider']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Reach, static_abilities.StaticAbilities.Infect]))

class c567698(card.Card):
    "Blighted Woodland"
    def __init__(self):
        super(c567698, self).__init__(gameobject.Characteristics(**{'name': 'Blighted Woodland', 'text': '{T}: Add {C}.\n{3}{G}, {T}, Sacrifice this land: Search your library for up to two basic land cards, put them onto the battlefield tapped, then shuffle.', 'color': ['G'], 'mana_cost': ''}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c366299(card.Card):
    "Bioshift"
    def __init__(self):
        super(c366299, self).__init__(gameobject.Characteristics(**{'name': 'Bioshift', 'text': 'Move any number of +1/+1 counters from target creature onto another target creature with the same controller.', 'color': ['G', 'U'], 'mana_cost': 'G/U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c228117(card.Card):
    "Benalish Veteran"
    def __init__(self):
        super(c228117, self).__init__(gameobject.Characteristics(**{'name': 'Benalish Veteran', 'text': 'Whenever this creature attacks, it gets +1/+1 until end of turn.', 'color': ['W'], 'mana_cost': '2W', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9667050064(card.Card):
    "Bellows Lizard"
    def __init__(self):
        super(c9667050064, self).__init__(gameobject.Characteristics(**{'name': 'Bellows Lizard', 'text': '{1}{R}: This creature gets +1/+0 until end of turn.', 'color': ['R'], 'mana_cost': 'R', 'power': 1, 'toughness': 1, 'subtype': ['Lizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452905(card.Card):
    "Beamsplitter Mage"
    def __init__(self):
        super(c452905, self).__init__(gameobject.Characteristics(**{'name': 'Beamsplitter Mage', 'text': 'Whenever you cast an instant or sorcery spell that targets only this creature, if you control one or more other creatures that spell could target, choose one of those creatures. Copy that spell. The copy targets the chosen creature.', 'color': ['R', 'U'], 'mana_cost': 'UR', 'power': 2, 'toughness': 2, 'subtype': ['Vedalken', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452904(card.Card):
    "Beacon Bolt"
    def __init__(self):
        super(c452904, self).__init__(gameobject.Characteristics(**{'name': 'Beacon Bolt', 'text': 'Beacon Bolt deals damage to target creature equal to the total number of instant and sorcery cards you own in exile and in your graveyard.\nJump-start (You may cast this card from your graveyard by discarding a card in addition to paying its other costs. Then exile this card.)', 'color': ['R', 'U'], 'mana_cost': '1UR'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c253589(card.Card):
    "Bazaar Krovod"
    def __init__(self):
        super(c253589, self).__init__(gameobject.Characteristics(**{'name': 'Bazaar Krovod', 'text': 'Whenever this creature attacks, another target attacking creature gets +0/+2 until end of turn. Untap that creature.', 'color': ['W'], 'mana_cost': '4W', 'power': 2, 'toughness': 5, 'subtype': ['Beast']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c373627(card.Card):
    "Battlewise Valor"
    def __init__(self):
        super(c373627, self).__init__(gameobject.Characteristics(**{'name': 'Battlewise Valor', 'text': 'Target creature gets +2/+2 until end of turn. Scry 1. (Look at the top card of your library. You may put that card on the bottom.)', 'color': ['W'], 'mana_cost': '1W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c373612(card.Card):
    "Battlewise Hoplite"
    def __init__(self):
        super(c373612, self).__init__(gameobject.Characteristics(**{'name': 'Battlewise Hoplite', 'text': 'Heroic — Whenever you cast a spell that targets this creature, put a +1/+1 counter on this creature, then scry 1. (To scry 1, look at the top card of your library, then you may put that card on the bottom.)', 'color': ['U', 'W'], 'mana_cost': 'WU', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c265399(card.Card):
    "Batterhorn"
    def __init__(self):
        super(c265399, self).__init__(gameobject.Characteristics(**{'name': 'Batterhorn', 'text': 'When this creature enters, you may destroy target artifact.', 'color': ['R'], 'mana_cost': '4R', 'power': 4, 'toughness': 3, 'subtype': ['Beast']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452811(card.Card):
    "Barrier of Bones"
    def __init__(self):
        super(c452811, self).__init__(gameobject.Characteristics(**{'name': 'Barrier of Bones', 'text': 'Defender\nWhen this creature enters, surveil 1. (Look at the top card of your library. You may put that card into your graveyard.)', 'color': ['B'], 'mana_cost': 'B', 'power': 0, 'toughness': 3, 'subtype': ['Skeleton', 'Wall']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Defender]))

class c9422408747(card.Card):
    "Barging Sergeant"
    def __init__(self):
        super(c9422408747, self).__init__(gameobject.Characteristics(**{'name': 'Barging Sergeant', 'text': 'Haste\nMentor (Whenever this creature attacks, put a +1/+1 counter on target attacking creature with lesser power.)', 'color': ['R'], 'mana_cost': '4R', 'power': 4, 'toughness': 2, 'subtype': ['Minotaur', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c9478696047(card.Card):
    "Bard's Bow"
    def __init__(self):
        super(c9478696047, self).__init__(gameobject.Characteristics(**{'name': "Bard's Bow", 'text': "Job select (When this Equipment enters, create a 1/1 colorless Hero creature token, then attach this to it.)\nEquipped creature gets +2/+2, has reach, and is a Bard in addition to its other types.\nPerseus's Bow — Equip {6} ({6}: Attach to target creature you control. Equip only as a sorcery.)", 'color': ['G'], 'mana_cost': '2G', 'subtype': ['Equipment']}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c9367876386(card.Card):
    "Balamb T-Rexaur"
    def __init__(self):
        super(c9367876386, self).__init__(gameobject.Characteristics(**{'name': 'Balamb T-Rexaur', 'text': 'Trample\nWhen this creature enters, you gain 3 life.\nForestcycling {2} ({2}, Discard this card: Search your library for a Forest card, reveal it, put it into your hand, then shuffle.)', 'color': ['G'], 'mana_cost': '4GG', 'power': 6, 'toughness': 6, 'subtype': ['Dinosaur']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Trample]))

class c376256(card.Card):
    "Azorius Guildgate"
    def __init__(self):
        super(c376256, self).__init__(gameobject.Characteristics(**{'name': 'Azorius Guildgate', 'text': 'This land enters tapped.\n{T}: Add {W} or {U}.', 'color': ['U', 'W'], 'mana_cost': '', 'subtype': ['Gate']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c265383(card.Card):
    "Axebane Stag"
    def __init__(self):
        super(c265383, self).__init__(gameobject.Characteristics(**{'name': 'Axebane Stag', 'text': '', 'color': ['G'], 'mana_cost': '6G', 'power': 6, 'toughness': 7, 'subtype': ['Elk']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c265410(card.Card):
    "Avenging Arrow"
    def __init__(self):
        super(c265410, self).__init__(gameobject.Characteristics(**{'name': 'Avenging Arrow', 'text': 'Destroy target creature that dealt damage this turn.', 'color': ['W'], 'mana_cost': '2W'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c208249(card.Card):
    "Auriok Sunchaser"
    def __init__(self):
        super(c208249, self).__init__(gameobject.Characteristics(**{'name': 'Auriok Sunchaser', 'text': 'Metalcraft — As long as you control three or more artifacts, this creature gets +2/+2 and has flying.', 'color': ['W'], 'mana_cost': '1W', 'power': 1, 'toughness': 1, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c423427(card.Card):
    "Auramancer"
    def __init__(self):
        super(c423427, self).__init__(gameobject.Characteristics(**{'name': 'Auramancer', 'text': 'When this creature enters, you may return target enchantment card from your graveyard to your hand.', 'color': ['W'], 'mana_cost': '2W', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c366337(card.Card):
    "Assault Griffin"
    def __init__(self):
        super(c366337, self).__init__(gameobject.Characteristics(**{'name': 'Assault Griffin', 'text': 'Flying', 'color': ['W'], 'mana_cost': '3W', 'power': 3, 'toughness': 2, 'subtype': ['Griffin']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c373506(card.Card):
    "Artisan's Sorrow"
    def __init__(self):
        super(c373506, self).__init__(gameobject.Characteristics(**{'name': "Artisan's Sorrow", 'text': 'Destroy target artifact or enchantment. Scry 2. (Look at the top two cards of your library, then put any number of them on the bottom and the rest on top in any order.)', 'color': ['G'], 'mana_cost': '3G'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c452901(card.Card):
    "Artful Takedown"
    def __init__(self):
        super(c452901, self).__init__(gameobject.Characteristics(**{'name': 'Artful Takedown', 'text': 'Choose one or both —\n• Tap target creature.\n• Target creature gets -2/-4 until end of turn.', 'color': ['B', 'U'], 'mana_cost': '2UB'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c9817289889(card.Card):
    "Arrest"
    def __init__(self):
        super(c9817289889, self).__init__(gameobject.Characteristics(**{'name': 'Arrest', 'text': "Enchant creature\nEnchanted creature can't attack or block, and its activated abilities can't be activated.", 'color': ['W'], 'mana_cost': '2W', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c253570(card.Card):
    "Armory Guard"
    def __init__(self):
        super(c253570, self).__init__(gameobject.Characteristics(**{'name': 'Armory Guard', 'text': 'This creature has vigilance as long as you control a Gate.', 'color': ['W'], 'mana_cost': '3W', 'power': 2, 'toughness': 5, 'subtype': ['Giant', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c369082(card.Card):
    "Armored Wolf-Rider"
    def __init__(self):
        super(c369082, self).__init__(gameobject.Characteristics(**{'name': 'Armored Wolf-Rider', 'text': '', 'color': ['G', 'W'], 'mana_cost': '3GW', 'power': 4, 'toughness': 6, 'subtype': ['Elf', 'Knight']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c253601(card.Card):
    "Archweaver"
    def __init__(self):
        super(c253601, self).__init__(gameobject.Characteristics(**{'name': 'Archweaver', 'text': 'Reach, trample', 'color': ['G'], 'mana_cost': '5GG', 'power': 5, 'toughness': 5, 'subtype': ['Spider']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Reach, static_abilities.StaticAbilities.Trample]))

class c380252(card.Card):
    "Archaeomancer"
    def __init__(self):
        super(c380252, self).__init__(gameobject.Characteristics(**{'name': 'Archaeomancer', 'text': 'When this creature enters, return target instant or sorcery card from your graveyard to your hand.', 'color': ['U'], 'mana_cost': '2UU', 'power': 1, 'toughness': 2, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c452872(card.Card):
    "Arboretum Elemental"
    def __init__(self):
        super(c452872, self).__init__(gameobject.Characteristics(**{'name': 'Arboretum Elemental', 'text': "Convoke (Your creatures can help cast this spell. Each creature you tap while casting this spell pays for {1} or one mana of that creature's color.)\nHexproof (This creature can't be the target of spells or abilities your opponents control.)", 'color': ['G'], 'mana_cost': '7GG', 'power': 7, 'toughness': 5, 'subtype': ['Elemental']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Hexproof, static_abilities.StaticAbilities.Convoke]))

class c9456752875(card.Card):
    "Arbor Elf"
    def __init__(self):
        super(c9456752875, self).__init__(gameobject.Characteristics(**{'name': 'Arbor Elf', 'text': '{T}: Untap target Forest.', 'color': ['G'], 'mana_cost': 'G', 'power': 1, 'toughness': 1, 'subtype': ['Elf', 'Druid']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c270361(card.Card):
    "Aquus Steed"
    def __init__(self):
        super(c270361, self).__init__(gameobject.Characteristics(**{'name': 'Aquus Steed', 'text': '{2}{U}, {T}: Target creature gets -2/-0 until end of turn.', 'color': ['U'], 'mana_cost': '3U', 'power': 1, 'toughness': 3, 'subtype': ['Beast']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9393815020(card.Card):
    "Apostle's Blessing"
    def __init__(self):
        super(c9393815020, self).__init__(gameobject.Characteristics(**{'name': "Apostle's Blessing", 'text': '({W/P} can be paid with either {W} or 2 life.)\nTarget artifact or creature you control gains protection from artifacts or from the color of your choice until end of turn.', 'color': ['W'], 'mana_cost': '1W/P'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c466975(card.Card):
    "Anvilwrought Raptor"
    def __init__(self):
        super(c466975, self).__init__(gameobject.Characteristics(**{'name': 'Anvilwrought Raptor', 'text': 'Flying\nFirst strike (This creature deals combat damage before creatures without first strike.)', 'color': [], 'mana_cost': '4', 'power': 2, 'toughness': 1, 'subtype': ['Bird']}, supertype=[], types=[cardtype.CardType.ARTIFACT, cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying, static_abilities.StaticAbilities.First_Strike]))

class c373584(card.Card):
    "Annul"
    def __init__(self):
        super(c373584, self).__init__(gameobject.Characteristics(**{'name': 'Annul', 'text': 'Counter target artifact or enchantment spell.', 'color': ['U'], 'mana_cost': 'U'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c270801(card.Card):
    "Annihilating Fire"
    def __init__(self):
        super(c270801, self).__init__(gameobject.Characteristics(**{'name': 'Annihilating Fire', 'text': 'Annihilating Fire deals 3 damage to any target. If a creature dealt damage this way would die this turn, exile it instead.', 'color': ['R'], 'mana_cost': '1RR'}, supertype=[], types=[cardtype.CardType.INSTANT], abilities=[]))

class c240059(card.Card):
    "Angel's Tomb"
    def __init__(self):
        super(c240059, self).__init__(gameobject.Characteristics(**{'name': "Angel's Tomb", 'text': 'Whenever a creature you control enters, you may have this artifact become a 3/3 white Angel artifact creature with flying until end of turn.', 'color': [], 'mana_cost': '3'}, supertype=[], types=[cardtype.CardType.ARTIFACT], abilities=[]))

class c366400(card.Card):
    "Angelic Edict"
    def __init__(self):
        super(c366400, self).__init__(gameobject.Characteristics(**{'name': 'Angelic Edict', 'text': 'Exile target creature or enchantment.', 'color': ['W'], 'mana_cost': '4W'}, supertype=[], types=[cardtype.CardType.SORCERY], abilities=[]))

class c220644(card.Card):
    "Ambush Viper"
    def __init__(self):
        super(c220644, self).__init__(gameobject.Characteristics(**{'name': 'Ambush Viper', 'text': 'Flash\nDeathtouch', 'color': ['G'], 'mana_cost': '1G', 'power': 2, 'toughness': 1, 'subtype': ['Snake']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flash, static_abilities.StaticAbilities.Deathtouch]))

class c9155944774(card.Card):
    "Akroan Hoplite"
    def __init__(self):
        super(c9155944774, self).__init__(gameobject.Characteristics(**{'name': 'Akroan Hoplite', 'text': 'Whenever this creature attacks, it gets +X/+0 until end of turn, where X is the number of attacking creatures you control.', 'color': ['R', 'W'], 'mana_cost': 'RW', 'power': 1, 'toughness': 2, 'subtype': ['Human', 'Soldier']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c423672(card.Card):
    "Airdrop Aeronauts"
    def __init__(self):
        super(c423672, self).__init__(gameobject.Characteristics(**{'name': 'Airdrop Aeronauts', 'text': 'Flying\nRevolt — When this creature enters, if a permanent left the battlefield under your control this turn, you gain 5 life.', 'color': ['W'], 'mana_cost': '3WW', 'power': 4, 'toughness': 3, 'subtype': ['Dwarf', 'Scout']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c9539158044(card.Card):
    "Ahn-Crop Crasher"
    def __init__(self):
        super(c9539158044, self).__init__(gameobject.Characteristics(**{'name': 'Ahn-Crop Crasher', 'text': "Haste (This creature can attack and {T} as soon as it comes under your control.)\nYou may exert this creature as it attacks. When you do, target creature can't block this turn. (An exerted creature won't untap during your next untap step.)", 'color': ['R'], 'mana_cost': '2R', 'power': 3, 'toughness': 2, 'subtype': ['Minotaur', 'Warrior']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Haste]))

class c373712(card.Card):
    "Agent of Horizons"
    def __init__(self):
        super(c373712, self).__init__(gameobject.Characteristics(**{'name': 'Agent of Horizons', 'text': "{2}{U}: This creature can't be blocked this turn.", 'color': ['G', 'U'], 'mana_cost': '2G', 'power': 3, 'toughness': 2, 'subtype': ['Human', 'Rogue']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9880321148(card.Card):
    "Affectionate Indrik"
    def __init__(self):
        super(c9880321148, self).__init__(gameobject.Characteristics(**{'name': 'Affectionate Indrik', 'text': "When this creature enters, you may have it fight target creature you don't control. (Each deals damage equal to its power to the other.)", 'color': ['G'], 'mana_cost': '5G', 'power': 4, 'toughness': 4, 'subtype': ['Beast']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c417609(card.Card):
    "Aether Meltdown"
    def __init__(self):
        super(c417609, self).__init__(gameobject.Characteristics(**{'name': 'Aether Meltdown', 'text': 'Flash (You may cast this spell any time you could cast an instant.)\nEnchant creature or Vehicle\nWhen this Aura enters, you get {E}{E} (two energy counters).\nEnchanted creature gets -4/-0.', 'color': ['U'], 'mana_cost': '1U', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[static_abilities.StaticAbilities.Flash]))

class c380241(card.Card):
    "Aether Adept"
    def __init__(self):
        super(c380241, self).__init__(gameobject.Characteristics(**{'name': 'Aether Adept', 'text': "When this creature enters, return target creature to its owner's hand.", 'color': ['U'], 'mana_cost': '1UU', 'power': 2, 'toughness': 2, 'subtype': ['Human', 'Wizard']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c554162(card.Card):
    "Aeronaut Admiral"
    def __init__(self):
        super(c554162, self).__init__(gameobject.Characteristics(**{'name': 'Aeronaut Admiral', 'text': 'Flying\nVehicles you control have flying.', 'color': ['W'], 'mana_cost': '3W', 'power': 3, 'toughness': 1, 'subtype': ['Human', 'Pilot']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Flying]))

class c423668(card.Card):
    "Aerial Modification"
    def __init__(self):
        super(c423668, self).__init__(gameobject.Characteristics(**{'name': 'Aerial Modification', 'text': "Enchant creature or Vehicle\nAs long as enchanted permanent is a Vehicle, it's a creature in addition to its other types.\nEnchanted creature gets +2/+2 and has flying.", 'color': ['W'], 'mana_cost': '4W', 'subtype': ['Aura']}, supertype=[], types=[cardtype.CardType.ENCHANTMENT], abilities=[]))

class c370738(card.Card):
    "Advocate of the Beast"
    def __init__(self):
        super(c370738, self).__init__(gameobject.Characteristics(**{'name': 'Advocate of the Beast', 'text': 'At the beginning of your end step, put a +1/+1 counter on target Beast creature you control.', 'color': ['G'], 'mana_cost': '2G', 'power': 2, 'toughness': 3, 'subtype': ['Elf', 'Shaman']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[]))

class c9232884334(card.Card):
    "Adventurer's Inn"
    def __init__(self):
        super(c9232884334, self).__init__(gameobject.Characteristics(**{'name': "Adventurer's Inn", 'text': 'When this land enters, you gain 2 life.\n{T}: Add {C}.', 'color': [], 'mana_cost': '', 'subtype': ['Town']}, supertype=[], types=[cardtype.CardType.LAND], abilities=[]))

class c9214504354(card.Card):
    "Acidic Slime"
    def __init__(self):
        super(c9214504354, self).__init__(gameobject.Characteristics(**{'name': 'Acidic Slime', 'text': 'Deathtouch (Any amount of damage this deals to a creature is enough to destroy it.)\nWhen this creature enters, destroy target artifact, enchantment, or land.', 'color': ['G'], 'mana_cost': '3GG', 'power': 2, 'toughness': 2, 'subtype': ['Ooze']}, supertype=[], types=[cardtype.CardType.CREATURE], abilities=[static_abilities.StaticAbilities.Deathtouch]))

