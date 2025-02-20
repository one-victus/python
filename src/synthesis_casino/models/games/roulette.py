from .game import Game
from models.enums import SettingChipsType, RouletteType, RouletteColor, RouletteEvenOdd

import random

class Roulette(Game):
    def __init__(self, name: str, id: str, casino: object, players: list[object]):
        super().__init__(name, id, casino)
        self.players = players

    def play(self, bets: list[dict[str, str | int | dict[str, int]]]) -> None:
        spin_result = self._spin()
        
        for bet in bets:
            player = next(player for player in self.players if player.id == bet["player_id"])

            if spin_result[bet["type"]] == bet["value"]:
                player.set_chips(bet["chips"], SettingChipsType.SUB)

                player.set_chips(player.calculate_chips(bet["chips"]) * 2, SettingChipsType.SUM)

                return True
            else:
                player.set_chips(bet["chips"], SettingChipsType.SUB)

                return False

    def _spin(self) -> dict[str, str | int]:
        number = random.randint(0, 36)

        if number == 0:
            color = RouletteColor.GREEN
        elif number % 2 == 0:
            color = RouletteColor.BLACK
        else:
            color = RouletteColor.RED

        if number % 2 == 0:
            even_odd = RouletteEvenOdd.EVEN
        else:
            even_odd = RouletteEvenOdd.ODD

        return {
            RouletteType.EVEN_ODD: even_odd,
            RouletteType.COLOR: color
        }