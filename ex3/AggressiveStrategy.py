from .GameStrategy import GameStrategy


class AggressiveStrategy (GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cheap_cards = sorted(hand, key=lambda card: card.cost)[:2]

        field_damage = sum(getattr(card, 'attack', 0) for card in battlefield)
        spell_damage = sum(3 for card in cheap_cards
                           if "Spell" in str(type(card)))
        total_damage = field_damage + spell_damage

        mana_spent = sum(card.cost for card in cheap_cards)
        cards_played = [card.name for card in cheap_cards]
        targets = self.prioritize_targets(["Enemy Player"])
        return {"cards_played": cards_played,
                "mana_used": mana_spent,
                "targets_attacked": targets,
                "damage_dealt": total_damage}

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        enemy_targets = [t for t in available_targets if t == "Enemy Player"]
        other_targets = [t for t in available_targets if t != "Enemy Player"]
        return enemy_targets + other_targets
