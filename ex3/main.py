from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine

print("=== DataDeck Game Engine ===")
print("Configuring Fantasy Card Game...")

engine = GameEngine()
factory = FantasyCardFactory()
strategy = AggressiveStrategy()

engine.configure_engine(factory, strategy)

print(f"Factory: {factory.__class__.__name__}")
print(f"Strategy: {strategy.get_strategy_name()}")
print(f"Available types: {factory.get_supported_types()}")

print("\nSimulating aggressive turn...")
turn = engine.simulate_turn()

print(f"Hand: {turn['hand']}")
print("\nTurn execution:")
print(f"Strategy: {turn['strategy']}")
print(f"Actions: {turn['actions']}")

print("\nGame Report:")
print(engine.get_engine_status())

print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
print("How do Abstract Factory and Strategy patterns work together? What")
print("makes this combination powerful for game engine systems?")
