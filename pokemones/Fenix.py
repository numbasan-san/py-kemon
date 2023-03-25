
from Pokemon import pokemon
from Ataque import ataque

class fenix(pokemon):
    
    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('fenix', 'fuego', 70, 35, 65, 75, 'F', [self.ataque_1, self.ataque_2, self.ataque_3, self.ataque_4])
    
    # nombre, tipo, usos, damage, precision, descripcion
    ataque_1 = pokemon.ataque('Llamaradas', 'fuego', 20, 50, 100, 'Con sus llamaradas quema al otro.')
    ataque_2 = pokemon.ataque('Lluvia de Brazas', 'fuego', 20, 20, 75, 'Bate las alas rociando con brazas al oponente haciendo que las respire, reduciendo su defensa.')
    ataque_3 = pokemon.ataque('Incendio', 'fuego', 20, 20, 100, 'Quema el campo de combate para reducir la movilidad del otro.')
    ataque_4 = pokemon.ataque('Renacimiento', 'fuego', 5, 00, 100, 'Cura parte de sus heridas al renacer.')
