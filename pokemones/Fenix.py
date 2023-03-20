
from Pokemon import pokemon

class fenix(pokemon):
    
    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('fenix', 'fuego', 70, 35, 65, 75, 'F', [self.ataque_1(), self.ataque_2(), 
                                                                 self.ataque_3(), self.ataque_4()])
    
    def ataque_1(self):
        return 'Con sus llamaradas quema al otro.'
    
    def ataque_2(self):
        return 'Bate las alas rociando con brazas al oponente haciendo que las respire, reduciendo su defensa.'

    def ataque_3(self):
        return 'Quema el campo de combate para reducir la movilidad del otro.'
    
    def ataque_4(self):
        return 'Cura parte de sus heridas al renacer.'
