
from Pokemon import pokemon

class sirena:

    def start_sirena(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        return pokemon('sirena', 'volador', 50, 20, 55, 83, 'S', [self.ataque_1(), self.ataque_2(), self.ataque_3(), self.ataque_4()])

    # nombre, tipo, usos, damage, precision, descripcion, funcion = None, efecto = False
    def ataque_1(self):
        return pokemon.ataque('Encanto', 'volador', 5, 00, 65, 'Hipnotiza al contrincante y reduce su defensa un poco.', self.encanto, True)

    def ataque_2(self):
        return pokemon.ataque('Onda de Choque', 'volador', 20, 60, 80, 'Canta a frecuencias que causan dolor de cabeza y que reduce la velocidad del oponente.', self.onda_de_choque, True)

    def ataque_3(self):
        return pokemon.ataque('Vuelo', 'volador', 5, 00, 100, 'Vuela para mejorar su evasión.', self.vuelo)

    def ataque_4(self):
        return pokemon.ataque('Zarpazos', 'normal', 20, 50, 90, 'Zarpazos.')

    def onda_de_choque(self, criatura):
        criatura.velocidad -= int(criatura.velocidad * 0.15)
        print('Velocidad enemiga mermada.')

    def encanto(self, criatura):
        criatura.defensa -= int(criatura.defensa * 0.15)
        print('Defensa enemiga mermada.')

    def vuelo(self, own):
        own.velocidad += int(own.velocidad * 0.2)
        print('Velocidad propia aumentada.')
