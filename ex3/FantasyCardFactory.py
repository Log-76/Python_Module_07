from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory
import random


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self._registry = {
            'creatures': {'dragon': {'name': 'Fire Dragon', 'cost': 5,
                                     'rarity': 'Legendary', 'attack': 6,
                                     'health': 8},
                          'goblin': {'name': 'Goblin Warrior', 'cost': 2,
                                     'rarity': 'Common', 'attack': 3,
                                     'health': 2}},
            'spells': {'fireball': {'name': 'Fireball', 'cost': 3,
                                    'rarity': 'Rare', 'effect_type': 'damage'},
                       'lightning_bolt': {'name': 'Lightning Bolt', 'cost': 2,
                                          'rarity': 'Common',
                                          'effect_type': 'damage'}},
            'artifacts': {'mana_ring': {'name': 'Mana Ring', 'cost': 1,
                                        'rarity': 'Common', 'durability': 5,
                                        'effect': '+1 mana per turn'},
                          'staff': {'name': 'Magic Staff', 'cost': 3,
                                    'rarity': 'Rare', 'durability': 3,
                                    'effect': '+2 spell power'},
                          'crystal': {'name': 'Power Crystal', 'cost': 2,
                                      'rarity': 'Uncommon', 'durability': 4,
                                      'effect': '+1 to all stats'}}
        }

    def create_creature(self, name_or_power: str | int | None = None
                        ) -> CreatureCard:
        creatures = self._registry['creatures']
        key = name_or_power if name_or_power in creatures else 'dragon'
        data = creatures[key]
        return CreatureCard(data['name'], data['cost'], data['rarity'],
                            data['attack'], data['health'])

    def create_spell(self, name_or_power: str | int | None = None
                     ) -> SpellCard:
        spells = self._registry['spells']
        key = name_or_power if name_or_power in spells else 'fireball'
        data = spells[key]
        return SpellCard(data['name'], data['cost'], data['rarity'],
                         data['effect_type'])

    def create_artifact(self, name_or_power: str | int | None = None
                        ) -> ArtifactCard:
        artifacts = self._registry['artifacts']
        key = name_or_power if name_or_power in artifacts else 'mana_ring'
        data = artifacts[key]
        return ArtifactCard(data['name'], data['cost'], data['rarity'],
                            data['durability'], data['effect'])

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        categories = list(self._registry.keys())

        for _ in range(size):
            category = random.choice(categories)
            card_key = random.choice(list(self._registry[category].keys()))
            if category == 'creatures':
                deck.append(self.create_creature(card_key))
            elif category == 'spells':
                deck.append(self.create_spell(card_key))
            else:
                deck.append(self.create_artifact(card_key))

        return {"deck": deck, "size": len(deck)}

    def get_supported_types(self) -> dict:
        return {category: list(card_types.keys())
                for category, card_types in self._registry.items()}
