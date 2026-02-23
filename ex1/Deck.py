from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
import random


class Deck:
    def __init__(self):
        self.deck = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i in self.deck:
            if i.name == card_name:
                self.deck.remove(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        if not self.deck:
            raise IndexError("Cannot draw from an empty deck")
        return self.deck.pop(0)

    def get_deck_stats(self) -> dict:
        total_card = len(self.deck)
        creatures = sum(1 for card in self.deck
                        if isinstance(card, CreatureCard))
        spells = sum(1 for card in self.deck if isinstance(card, SpellCard))
        artifacts = sum(1 for card in self.deck
                        if isinstance(card, ArtifactCard))
        avg_cost = 0
        if total_card > 0:
            avg_cost = sum(c.cost for c in self.deck) / total_card
        return {"total_cards": total_card, "creatures": creatures,
                "spells": spells, "artifacts": artifacts, "avg_cost": avg_cost}
