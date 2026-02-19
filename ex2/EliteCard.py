from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str, attack_power: int,
                 defense: int, mana: int):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.attack_power = attack_power
        self.defense = defense
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        if game_state["mana"] < self.cost:
            return {"error": "not enough mana"}
        game_state["mana"] -= self.cost
        return {"card_played": self.name, "mana_used": self.cost,
                "effect": "Elite card played"}

    def attack(self, target: object) -> dict:
        return {"attacker": self.name, "target": target,
                "damage": self.attack_power, "combat_type": "melee"}

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = min(self.defense, incoming_damage)
        damage_taken = max(0, incoming_damage - self.defense)
        return {"defender": self.name, "damage_taken": damage_taken,
                "damage_blocked": damage_blocked,
                "still_alive": damage_taken < self.mana}

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_power, "defense": self.defense}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_used = 4
        self.mana -= mana_used
        return {"caster": self.name, "spell": spell_name,
                "targets": targets, "mana_used": mana_used}

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> dict:
        return {"mana": self.mana}
