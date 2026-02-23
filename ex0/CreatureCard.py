from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        if not isinstance(attack, int) or attack < 0:
            raise ValueError("attack negatif impossible")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health negatif impossible ou equivalent a 0")
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        return {'card_played': self.name, 'mana_used': self.cost,
                'effect': 'Creature summoned to battlefield'}

    def attack_target(self, target: object) -> dict:
        target.health = target.health - self.attack
        final = False
        if target.health < 1:
            final = True
        return {"attacker": self.name, "target": target.name,
                "damage_dealt": self.attack, "combat_resolved": final}

    def get_card_info(self):
        return {"name": self.name, "cost": self.cost, "rarity": self.rarity,
                "attack": self.attack, "health": self.health}
