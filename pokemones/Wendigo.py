
from Pokemon import pokemon

class wendigo(pokemon):

    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('wendigo', 'hielo', 100, 40, 65, 60, 'W', [self.ataque_1, self.ataque_2, self.ataque_3, self.ataque_4])

    # nombre, tipo, usos, damage, precision, descripcion
    ataque_1 = pokemon.ataque('Desgarre', 'normal', 20, 65, 75, 'Corta al otro con las garras.')
    ataque_2 = pokemon.ataque('Cacería', 'normal', 10, 0, 100, 'Aumenta la velocidad.')
    ataque_3 = pokemon.ataque('Asalto', 'normal', 20, 50, 70, 'Salta hacia al enemigo.')
    ataque_4 = pokemon.ataque('Fauces', 'normal', 20, 50, 75, 'Muerde al enemigo.')


# 6600 AMD