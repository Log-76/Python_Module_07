from ex2.EliteCard import EliteCard

print("=== DataDeck Ability System ===")
print("EliteCard capabilities:")
print("- Card: ['play', 'get_card_info', 'is_playable']")
print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")
print()

# Créer la carte
arcane_warrior = EliteCard("Arcane Warrior", 5, "legendary", 5, 3, 8)

game_state = {"mana": 10}

print("Playing Arcane Warrior (Elite Card):")
print()
print("Combat phase:")

attack_result = arcane_warrior.attack("Enemy")
print("Attack result:", attack_result)

defend_result = arcane_warrior.defend(5)
print("Defense result:", defend_result)

print()
print("Magic phase:")

spell_result = arcane_warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"])
print("Spell cast:", spell_result)

mana_result = arcane_warrior.channel_mana(3)
print("Mana channel:", mana_result)

print()
print("Multiple interface implementation successful!")
