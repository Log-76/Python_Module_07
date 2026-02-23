from .CreatureCard import CreatureCard

try:
    print("=== DataDeck Card Foundation ===")
    print("Testing Abstract Base Class Design:")

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    goblin = CreatureCard("Goblin Warrior", 2, "Common", 2, 1)

    print("\nCreatureCard Info:")
    print(dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {dragon.is_playable(6)}")
    print(f"Play result: {dragon.play({})}")

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {dragon.attack_target(goblin)}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")
    print("Abstract pattern successfully demonstrated")
except ValueError as e:
    print(e)
