from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, defense: int,
                 base_rating: int = 1200) -> None:
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.rating = base_rating
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        if game_state.get("mana", 0) < self.cost:
            return {"error": "not enough mana"}
        game_state["mana"] -= self.cost
        return {"card_played": self.name, "mana_used": self.cost,
                "effect": "Tournament card enters the battlefield"}

    def get_card_info(self) -> dict:
        return {"name": self.name, "cost": self.cost,
                "rarity": self.rarity, "type": "Tournament"}

    def attack(self, target) -> dict:
        target_name = target.name if hasattr(target, "name") else target
        return {"attacker": self.name, "target": target_name,
                "damage": self.attack_power, "combat_type": "tournament"}

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.defense, incoming_damage)
        taken = max(0, incoming_damage - self.defense)
        return {"defender": self.name, "damage_taken": taken,
                "damage_blocked": blocked, "still_alive": True}

    def get_combat_stats(self) -> dict:
        return {"name": self.name, "attack": self.attack_power,
                "defense": self.defense}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += wins * 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= losses * 16

    def get_rank_info(self) -> dict:
        return {"name": self.name, "rating": self.rating,
                "wins": self.wins, "losses": self.losses}

    def get_tournament_stats(self) -> dict:
        return {"name": self.name, "rating": self.rating,
                "record": f"{self.wins}-{self.losses}",
                "attack": self.attack_power, "defense": self.defense}
