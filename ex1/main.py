from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck


try:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()

    lightning_bolt = SpellCard("Lightning Bolt", 3, "Common", "damage")
    mana_crystal = ArtifactCard("Mana Crystal", 2, "Uncommon", 5,
                                "+1 mana per turn")
    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    deck.add_card(lightning_bolt)
    deck.add_card(mana_crystal)
    deck.add_card(fire_dragon)

    print("Deck stats:", deck.get_deck_stats())
    print("\nDrawing and playing cards:")

    game_state = {"mana": 10}

    while deck.deck:
        card = deck.draw_card()
        print(f"\nDrew: {card.name} ({card.get_card_info().get('type')})")
        print(f"Play result: {card.play(game_state)}")

    print("\nPolymorphism in action: Same interface,"
          "different card behaviors!")

except IndexError as e:
    print(e)
except ValueError as e:
    print(e)
