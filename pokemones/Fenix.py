
from Pokemon import pokemon
from Ataque import ataque

class fenix(pokemon):
    
    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('fenix', 'fuego', 70, 35, 65, 75, 'F', [self.ataque_1(), self.ataque_2(), self.ataque_3(), self.ataque_4()])
    
    # nombre, tipo, usos, damage, precision, descripcion
    def ataque_1(self):
        return pokemon.ataque('Llamaradas', 'normal', 20, 70, 100, 'Ataca con sus garras y pico.')

    def ataque_2(self):
        return pokemon.ataque('Lluvia de Brazas', 'fuego', 10, 20, 75, 'Bate las alas rociando con brazas al oponente haciendo que las respire, reduciendo su defensa.', self.lluvia_de_brazas, True)

    def ataque_3(self):
        return pokemon.ataque('Incendio', 'fuego', 3, 20, 100, 'Quema el campo de combate para reducir la movilidad del otro y lo quema un poco.', self.incendio, True)

    def ataque_4(self):
        return pokemon.ataque('Renacimiento', 'fuego', 5, 00, 100, 'Cura sus heridas al renacer pero reduce bastante su propio daño.', self.renacimiento)
    
    def lluvia_de_brazas(self, criatura):
        criatura.defensa -= 3

    def incendio(self, criatura):
        criatura.velocidad -= 15
    
    def renacimiento(self):
        self.vida = 70
        self.damage -= int(self.damage * 0.3)
