from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory
import random


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
        creatures = self._registry['creatures']
        key = name_or_power if name_or_power in creatures else "dragon"
        data = creatures[key]
        return CreatureCard(data["name"], data["cost"], data["rarity"],
                            data["attack"], data["health"])

    def create_spell(self, name_or_power: str | int
                     | None = None) -> SpellCard:
        spells = self._registry['spells']
        key = name_or_power if name_or_power in spells else "fireball"
        data = spells[key]
        return SpellCard(data["name"], data["cost"], data["rarity"],
                         data["power"])

    def create_artifact(self, name_or_power: str | int
                        | None = None) -> ArtifactCard:
        artif = self._registry['artifacts']
        key = name_or_power if name_or_power in artif else "mana_ring"
        data = artif[key]
        return SpellCard(data["name"], data["cost"], data["rarity"],
                         data["effect"])

    def create_themed_deck(self, size: int) -> dict:
        """Crée un deck aléatoire de la taille spécifiée."""
        deck = []
        categories = list(self._registry.keys())
        for _ in range(size):
            cat = random.choice(categories)
            card_key = random.choice(list(self._registry[cat].keys()))
            if cat == 'creatures':
                deck.append(self.create_creature(card_key))
            elif cat == 'spells':
                deck.append(self.create_spell(card_key))
            else:
                deck.append(self.create_artifact(card_key))
        return {"deck": deck, "size": len(deck)}

    def get_supported_types(self) -> dict:
        """Retourne les types supportés comme demandé dans l'output exemple."""
        return {cat: list(cards.keys()) for cat, cards
                in self._registry.items()}
