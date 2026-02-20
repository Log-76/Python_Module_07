from .TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self):
        # Stocke les cartes enregistrées
        self.registry = {}
        # Compteur pour les statistiques du rapport
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        # Génération d'ID spécifique pour correspondre
        #  à la trace (ex: dragon_001)
        name_part = (card.name.split()[1].lower() if " " in
                     card.name else card.name.lower())
        card_id = f"{name_part}_001"
        self.registry[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        c1 = self.registry[card1_id]
        c2 = self.registry[card2_id]
        # Logique de match basée sur la puissance héritée de Combatable
        if c1.power >= c2.power:
            c1.update_wins(1)
            c2.update_losses(1)
            winner_id, loser_id = card1_id, card2_id
            winner_card, loser_card = c1, c2
        else:
            c2.update_wins(1)
            c1.update_losses(1)
            winner_id, loser_id = card2_id, card1_id
            winner_card, loser_card = c2, c1
        self.matches_played += 1
        # Retourne le dictionnaire complet avec
        # les ratings mis à jour pour la trace
        return {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner_card.calculate_rating(),
            'loser_rating': loser_card.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        # Trie par rating décroissant
        cards_items = list(self.registry.items())
        sorted_items = sorted(cards_items, key=lambda
                              x: x[1].calculate_rating(), reverse=True)
        # Formatage textuel pour le leaderboard de la trace
        leaderboard = []
        for i, (cid, card) in enumerate(sorted_items, 1):
            info = card.get_rank_info()
            leaderboard.append(f"{card.name} - Rating: {info['rating']}"
                               f"({info['record']})")
        return leaderboard

    def generate_tournament_report(self) -> dict:
        # Calcul de la moyenne des ratings pour le rapport
        all_ratings = [c.calculate_rating() for c in self.registry.values()]
        avg_rating = sum(all_ratings) // len(all_ratings) if all_ratings else 0
        # Structure exacte du rapport de la trace
        return {
            'total_cards': len(self.registry),
            'matches_played': self.matches_played,
            'avg_rating': avg_rating,
            'platform_status': 'active'
        }
