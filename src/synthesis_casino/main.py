from models import Casino, Player, Roulette, RouletteType, RouletteColor, RouletteEvenOdd

def main():
    default_chips = (
        ("blanca", 1),
        ("roja", 5),
        ("azul", 10),
        ("verde", 25),
        ("negra", 100),
        ("morada", 500),
        ("naranja", 1000),
        ("gris", 5000),
        ("amarilla", 10000)
    )
    
    casino = Casino("La plata", "123 Main St", "352", default_chips)
    player = Player("Juan", 25, "30000000", casino)
    roulette = Roulette("Ruleta 1", "1234567890", casino, [player])

    player.set_chips({
        "roja": 2,
        "negra": 1,
        "azul": 1,
        "verde": 1,
    })
    
    print(f"El jugador {player.name} tiene {player.calculate_chips()} dólares en fichas")
    print(player.chips)

    win = roulette.play([
        {
            "player_id": player.id, 
            "type": RouletteType.EVEN_ODD, 
            "value": RouletteEvenOdd.EVEN, 
            "chips": {
                "roja": 2,
                "negra": 1
            }
        }
    ])

    print(f"{player.name} ha {'ganado' if win else 'perdido'}")
    print(f"Ahora {player.name} tiene {player.calculate_chips()} dólares en fichas")
    print(player.chips)

if __name__ == "__main__":
    main()