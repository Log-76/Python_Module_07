from .CreatureCard import CreatureCard

print("=== DataDeck Card Foundation ===\n")
print("Testing Abstract Base Class Design:\n")
dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
print("CreatureCard Info:")
print({"name": dragon.name, "cost": dragon.cost, "rarity": dragon.rarity,
       "attack": dragon.attack, "health": dragon.health})
print("\nPlaying Fire Dragon with 6 mana available:")
print("playable:", dragon.is_playable(6))
if dragon.is_playable(6) is True:
    print(dragon.play({}))

gobling = CreatureCard("goblin", 5, "Legendary", 7, 5)
print("\nFire Dragon attacks Goblin Warrior:")
print("attack result", dragon.attack_target(gobling))
print("\nTesting insufficient mana (3 available):")
print("playable:", dragon.is_playable(3))
print("Abstract pattern successfully demonstrated!")
