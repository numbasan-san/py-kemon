
from Pokemon import pokemon
from Ataque import ataque

class fenix:

    def start_fenix(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        return pokemon('fenix', 'fuego', 70, 35, 65, 75, 'F', [self.ataque_1(), self.ataque_2(), self.ataque_3(), self.ataque_4()])
    
    # nombre, tipo, usos, damage, precision, descripcion
    def ataque_1(self):
        return pokemon.ataque('Punzocorte', 'normal', 20, 70, 100, 'Ataca con sus garras y pico.')

    def ataque_2(self):
        return pokemon.ataque('Lluvia de Brazas', 'fuego', 10, 20, 75, 'Bate las alas rociando con brazas al oponente haciendo que las respire, reduciendo su defensa.', self.lluvia_de_brazas, True)

    def ataque_3(self):
        return pokemon.ataque('Incendio', 'fuego', 3, 20, 100, 'Quema el campo de combate para reducir la movilidad del otro y lo quema un poco.', self.incendio, True)

    def ataque_4(self):
        return pokemon.ataque('Renacimiento', 'fuego', 5, 00, 100, 'Cura sus heridas al renacer pero reduce bastante su propio daño.', self.renacimiento)
    
    def lluvia_de_brazas(self, criatura):
        criatura.defensa -= 3
        print('Defensa enemiga mermada.')

    def incendio(self, criatura):
        criatura.velocidad -= 15
        print('Velocidad enemiga mermada.')
    
    def renacimiento(self, own):
        own.vida = 70
        own.damage -= int(own.damage * 0.3)
        print('Salud propia restaurada. Defensa daño mermada.')
