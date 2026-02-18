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
            return {"error": "not enougth mana for this spell"}
        game_state["mana"] -= game_state["cost"]
        target = [game_state["targets"]]
        result = self.resolve_effect(target)
        self.use = True
        return game_state.update(result)

    def resolve_effect(self, targets: list) -> dict:

        # TODO: Branch logic based on self.effect_type:
        #   - "damage"  → TODO: Calculate and apply damage to each target
        #   - "heal"    → TODO: Calculate and restore HP to each target
        #   - "buff"    → TODO: Apply a positive stat modifier to each target
        #   - "debuff"  → TODO: Apply a negative stat modifier to each target
        # TODO: Build and return a result dict summarizing what happened (affected targets, amounts, etc.)
        pass