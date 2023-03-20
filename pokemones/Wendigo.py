
from Pokemon import pokemon

class wendigo(pokemon):
    
    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('wendigo', 'hielo', 100, 40, 65, 60, 'W', [self.ataque_1(), self.ataque_2(), 
                                                                    self.ataque_3(), self.ataque_4()])
    
    def ataque_1(self):
        return 'Corta al otro con las garras.'
    
    def ataque_2(self):
        return 'Aumenta la velocidad.'

    def ataque_3(self):
        return 'Salta hacia al enemigo.'
    
    def ataque_4(self):
        return 'Muerde al enemigo.'
