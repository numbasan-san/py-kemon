
from Pokemon import pokemon

class golem(pokemon):
    
    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('golem', 'metal', 200, 80, 60, 40, 'G', [self.ataque_1(), self.ataque_2(), 
                                                                  self.ataque_3(), self.ataque_4()])
    
    def ataque_1(self):
        return 'Aumenta su defensa aumentando su dureza.'
    
    def ataque_2(self):
        return 'Levanta una roca gigante y la lanza al enemigo.'

    def ataque_3(self):
        return 'Provoca un terremoto que reduce la velocidad del enemigo.'
    
    def ataque_4(self):
        return 'Da un puñetazo al contrincante.'
