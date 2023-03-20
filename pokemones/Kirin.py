
from Pokemon import pokemon

class kirin(pokemon):
    
    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('kirin', 'rayo', 125, 60, 70, 80, 'K', [self.ataque_1(), self.ataque_2(), 
                                                                 self.ataque_3(), self.ataque_4()])
    
    def ataque_1(self):
        return 'Carga un rayo que lanza al contrario que quizás lo paralice.'
    
    def ataque_2(self):
        return 'Acumula electricidad para potenciar de sobremanera su velocidad.'

    def ataque_3(self):
        return 'Inbulle su cuerpo en electricidad para aumentar su ataque.'

    def ataque_4(self):
        return 'Lanza un coletazo que lo puede aturdir bajando su velocidad.'
