from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine


print("=== DataDeck Game Engine ===\n")

# 1. Initialisation
engine = GameEngine()
factory = FantasyCardFactory()
strategy = AggressiveStrategy()

# 2. Configuration (Affiche les messages de config)
engine.configure_engine(factory, strategy)

# 3. Affichage des types supportés
supported = factory.get_supported_types()
print(f"Available types: {supported}")

# 4. Simulation du tour
print("\nSimulating aggressive turn...")
turn_execution = engine.simulate_turn()

# Affichage du détail du tour
print("Turn execution:")
print(f"Strategy: {strategy.get_strategy_name()}")
print(f"Actions: {turn_execution}")

# 5. Rapport final
print("\nGame Report:")
report = engine.get_engine_status()
print(report)

print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
