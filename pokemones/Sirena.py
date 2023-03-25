
from Pokemon import pokemon

class sirena(pokemon):
    
    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('sirena', 'volador', 50, 20, 40, 83, 'S', [self.ataque_1, self.ataque_2, self.ataque_3, self.ataque_4])
    
    # nombre, tipo, usos, damage, precision, descripcion
    ataque_1 = pokemon.ataque('Encanto', 'volador', 5, 00, 65, 'Hipnotiza al contrincante.')
    ataque_2 = pokemon.ataque('Onda de Choque', 'volador', 20, 60, 80, 'Canta a frecuencias que causan dolor de cabeza.')
    ataque_3 = pokemon.ataque('Vuelo', 'volador', 10, 00, 100, 'Vuela para mejorar su evasión.')
    ataque_4 = pokemon.ataque('Zarpazos', 'normal', 20, 50, 90, 'Zarpazos.')
