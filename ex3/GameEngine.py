from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def __init__(self):
        self._factory = None
        self._strategy = None
        self._stats = {"turns_simulated": 0, "total_damage": 0,
                       "cards_created": 0}

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Configure le moteur avec une usine et une stratégie spécifique."""
        self._factory = factory
        self._strategy = strategy
        print("Configuring Fantasy Card Game...")
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.get_strategy_name()}")

    def simulate_turn(self) -> dict:
        """Simule un tour complet de jeu."""
        if not self._factory or not self._strategy:
            raise ValueError("Engine must be configured before simulation.")
        # 1. Génération d'une main via la factory
        deck_data = self._factory.create_themed_deck(size=3)
        hand = deck_data['deck']
        # 2. Mise à jour des stats de création
        self._stats["cards_created"] += len(hand)
        self._stats["turns_simulated"] += 1
        # 3. Exécution du tour via la stratégie
        # On passe une liste vide pour le battlefield car c'est le début
        turn_results = self._strategy.execute_turn(hand, [])
        # 4. Mise à jour des dégâts globaux
        self._stats["total_damage"] += turn_results.get("damage_dealt", 0)
        return turn_results

    def get_engine_status(self) -> dict:
        """Retourne le rapport final de la partie."""
        status = self._stats.copy()
        status["strategy_used"] = self._strategy.get_strategy_name()
        return status
