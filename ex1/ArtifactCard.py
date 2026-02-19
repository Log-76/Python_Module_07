class ArtifactCard:
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.durability = durability
        self.effect = effect
        self.in_play = False
        self.destroyed = False

    def play(self, game_state: dict) -> dict:
        if game_state["mana"] < self.cost:
            return {"error": "not enough mana"}
        game_state["mana"] -= self.cost
        return {"card_played": self.name, "mana_used": self.cost,
                "effect": f"Permanent: {self.effect}"}

    def activate_ability(self) -> dict:
        if self.destroyed is True:
            return {"Artifact": "is detroye"}
        self.durability -= 1
        if self.durability < 1:
            self.destroyed = True
        return {"ability": self.effect,
                "durability_remaining": self.durability,
                "destroyed": self.destroyed}
