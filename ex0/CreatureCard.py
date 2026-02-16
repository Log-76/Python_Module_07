from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int,
                 health: int) -> None:
        super.__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    # a faire
    def play(self, game_state: dict) -> dict:
        pass

    def attack_target(self, target: object) -> dict:
        if self.attack < 1 or target.health < 1:
            return {"name": target.name, "cost": target.cost,
                    "rarity": target.rarity, "attack": target.attack,
                    "health": target.healf}
        else:
            target.health = target.health - self.attack
            return {"name": target.name, "cost": target.cost,
                    "rarity": target.rarity, "attack": target.attack,
                    "health": target.healf}
