
from Pokemon import pokemon

class sirena(pokemon):
    
    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('sirena', 'volador', 50, 20, 40, 83, 'S', 
                         [self.ataque_1(), self.ataque_2(), self.ataque_3(), self.ataque_4()])
    
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
        criatura.velocidad -= int(criatura.velocidad * 0.05)
    
    def encanto(self, criatura):
        criatura.defensa -= int(criatura.defensa * 0.15)
    
    def vuelo(self):
        self.velocidad += int(self.velocidad * 0.2)
