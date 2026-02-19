class SpellCard:
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.effect_type = effect_type
        self.use = False

    def play(self, game_state: dict) -> dict:
        if self.use is True:
            return {"error": "Spell already used"}
        if game_state["mana"] < self.cost:
            return {"error": "not enough mana"}
        game_state["mana"] -= self.cost
        result = self.resolve_effect([])
        self.use = True
        return {"card_played": self.name, "mana_used": self.cost,
                "effect": result["effect"]}

    def resolve_effect(self, targets: list) -> dict:
        results = []
        if self.effect_type == "damage":
            damage_amount = 3
            for target in targets:
                target["hp"] -= damage_amount
                results.append({"target": target["name"],
                                "damage": damage_amount,
                                "hp_remaining": target["hp"]})
            return {"effect": f"Deal {self.cost} damage to target"}
        if self.effect_type == "heal":
            heal = 3
            for target in targets:
                target["hp"] += heal
                results.append({"target": target["name"],
                                "heal": heal,
                                "hp_remaining": target["hp"]})
            return {"effect": "heal", "affected": results}
        if self.effect_type == "buff":
            buff = 1
            for target in targets:
                target["mana"] += buff
                results.append({"target": target["name"],
                                "buff": buff,
                                "mana_remaining": target["mana"]})
            return {"effect": "buff", "affected": results}
        if self.effect_type == "debuff":
            debuff = 1
            for target in targets:
                target["mana"] += debuff
                results.append({"target": target["name"],
                                "mana": debuff,
                                "mana_remaining": target["mana"]})
            return {"effect": "mana", "affected": results}
