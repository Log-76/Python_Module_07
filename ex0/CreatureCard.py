from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'}

    def attack_target(self, target: object) -> dict:
        if self.attack < 1 or target.health < 1:
            return {"attacker": self.name, "target": target.name,
                    "damage_dealt": 0, "combat_resolved": False}
        else:
            target.health = target.health - self.attack
            final = False
            if target.health < 1:
                final = True
            return {"attacker": self.name, "target": target.name,
                    "damage_dealt": self.attack, "combat_resolved": final}
