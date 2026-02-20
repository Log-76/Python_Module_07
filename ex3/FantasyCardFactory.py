from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self._registry = {'creatures': {
            'dragon': {'name': 'Fire Dragon', 'cost': 5, 'rarity': 'legendary',
                       'attack': 6, 'health': 8},
            'goblin': {'name': 'Goblin Warrior', 'cost': 2, 'rarity': 'common',
                       'attack': 3, 'health': 2}},
            'spells': {
            'fireball': {'name': 'Fireball', 'cost': 3, 'rarity': 'rare',
                         'power': 5},
            'lightning_bolt': {'name': 'Lightning Bolt', 'cost': 2,
                               'rarity': 'common', 'power': 3}},
            'artifacts': {
            'mana_ring': {'name': 'Mana Ring', 'cost': 1, 'rarity': 'common',
                          'effect': '+1 mana'},
            'staff': {'name': 'Magic Staff', 'cost': 3, 'rarity': 'rare',
                      'effect': '+2 power'},
            'crystal': {'name': 'Crystal', 'cost': 2, 'rarity': 'uncommon',
                        'effect': '+1 all stats'}}}

    def create_creature(self, name_or_power: str | int
                        | None = None) -> CreatureCard:
        key = name_or_power if name_or_power in self._registry else "dragon"
        dq
    def create_spell(self, name_or_power: str | int
                     | None = None) -> SpellCard:
        pass

    def create_artifact(self, name_or_power: str | int
                        | None = None) -> ArtifactCard:
        pass

    def create_themed_deck(self, size: int) -> dict:
        pass

    def get_supported_types(self) -> dict:
        pass
