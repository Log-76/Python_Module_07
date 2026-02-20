from .GameStrategy import GameStrategy


class AggressiveStrategy (GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        # 1. On joue des cartes de la main (ton code précédent)
        cards_to_play = sorted(hand, key=lambda x: x.cost)[:2]

        # 2. On fait attaquer les créatures déjà sur le terrain (battlefield)
        # On additionne la puissance (power) de chaque créature sur le plateau
        damage_from_battlefield = sum(card.power for card in battlefield)

        # 3. On calcule les dégâts des nouveaux sorts joués
        # (ex: 3 dégâts par sort)
        damage_from_spells = sum(3 for card in cards_to_play if "Spell"
                                 in str(type(card)))

        return {
            "cards_played": [c.name for c in cards_to_play],
            "mana_used": sum(c.cost for c in cards_to_play),
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_from_battlefield + damage_from_spells}

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        player_target = [t for t in available_targets if t == "Enemy Player"]
        other_target = [t for t in available_targets if t != "Enemy Player"]

        return player_target + other_target
