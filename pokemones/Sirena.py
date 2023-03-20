
from Pokemon import pokemon

class sirena(pokemon):
    
    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('sirena', 'volador', 50, 20, 40, 83, 'S', [self.ataque_1(), self.ataque_2(), 
                                                                    self.ataque_3(), self.ataque_4()])
    
    def ataque_1(self):
        return 'Hipnotiza al contrincante.'
    
    def ataque_2(self):
        return 'Canta a frecuencias que causan dolor de cabeza.'

    def ataque_3(self):
        return 'Vuela para mejorar su evasión.'
    
    def ataque_4(self):
        return 'Zarpazos.'
