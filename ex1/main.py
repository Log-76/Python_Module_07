from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck

print("=== DataDeck Deck Builder ===")
print("Building deck with different card types...")

# Créer le deck
deck = Deck()

# Créer les cartes
lightning_bolt = SpellCard("Lightning Bolt", 3, "common", "damage")
mana_crystal = ArtifactCard("Mana Crystal", 4, "uncommon", 5,
                            "+1 mana per turn")
fire_dragon = CreatureCard("Fire Dragon", 5, "rare", 6, 4)

# Ajouter au deck
deck.add_card(lightning_bolt)
deck.add_card(mana_crystal)
deck.add_card(fire_dragon)

print("Deck stats:", deck.get_deck_stats())
print("Drawing and playing cards:")

game_state = {"mana": 10}

card = deck.draw_card()
print(f"Drew: {card.name} (Spell)")
print("Play result:", card.play(game_state))

card = deck.draw_card()
print(f"Drew: {card.name} (Artifact)")
print("Play result:", card.play(game_state))

card = deck.draw_card()
print(f"Drew: {card.name} (Creature)")
print("Play result:", card.play(game_state))

print("Polymorphism in action: Same interface, different card behaviors!")
