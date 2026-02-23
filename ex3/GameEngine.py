from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:

    def __init__(self):
        self._factory = None
        self._strategy = None
        self._stats = {
            "turns_simulated": 0,
            "total_damage": 0,
            "cards_created": 0
        }

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        self._factory = factory
        self._strategy = strategy

    def simulate_turn(self) -> dict:
        if not self._factory or not self._strategy:
            raise ValueError("Engine must be configured before simulation.")

        deck_data = self._factory.create_themed_deck(size=3)
        hand = deck_data['deck']

        self._stats["cards_created"] += len(hand)
        self._stats["turns_simulated"] += 1

        turn_result = self._strategy.execute_turn(hand, [])
        self._stats["total_damage"] += turn_result.get("damage_dealt", 0)

        hand_display = [f"{card.name} ({card.cost})" for card in hand]

        return {
            "hand": hand_display,
            "strategy": self._strategy.get_strategy_name(),
            "actions": turn_result
        }

    def get_engine_status(self) -> dict:
        report = self._stats.copy()
        report["strategy_used"] = self._strategy.get_strategy_name()
        return report
