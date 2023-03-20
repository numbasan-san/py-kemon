
from Pokemon import pokemon

class hipocampo(pokemon):
    
    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('hipocampo', 'agua', 60, 30, 50, 85, 'H', [self.ataque_1(), self.ataque_2(), 
                                                                    self.ataque_3(), self.ataque_4()])
    
    def ataque_1(self):
        return 'Lanza un chorro de agua a super preción.'
    
    def ataque_2(self):
        return 'Lanza cozes y patadas que pueden aturdir al contrincante.'

    def ataque_3(self):
        return 'Hunde al contrincante bajando su defensa.'
    
    def ataque_4(self):
        return 'Aumenta su velocidad al nadar.'
