from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===")

    # 1. Initialisation de la plateforme
    platform = TournamentPlatform()

    print("Registering Tournament Cards...")

    # 2. Création et enregistrement des cartes de tournoi
    # Hérite de Card, Combatable, et Rankable
    dragon = TournamentCard("Fire Dragon", power=50, health=100,
                            initial_rating=1200)
    wizard = TournamentCard("Ice Wizard", power=40, health=80,
                            initial_rating=1150)

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    # Affichage des détails de l'enregistrement
    for card_id, card in [(dragon_id, dragon), (wizard_id, wizard)]:
        print(f"{card.name} (ID: {card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.calculate_rating()}")
        print(f"- Record: {card.wins}-{card.losses}")

    # 3. Simulation d'un match de tournoi
    print("\nCreating tournament match...")
    match_result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {match_result}")

    # 4. Affichage du Leaderboard
    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for i, entry in enumerate(leaderboard, 1):
        print(f"{i}. {entry}")

    # 5. Rapport final de la plateforme
    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
