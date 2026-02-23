from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


try:
    print("=== DataDeck Tournament Platform ===")
    print("Registering Tournament Cards...")

    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 3, 1200)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 5, 4, 1150)

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    for card_id, card in [(dragon_id, dragon), (wizard_id, wizard)]:
        print(f"\n{card.name} (ID: {card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.calculate_rating()}")
        print(f"- Record: {card.wins}-{card.losses}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    for line in platform.get_leaderboard():
        print(line)

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
except Exception as e:
    print(e)
