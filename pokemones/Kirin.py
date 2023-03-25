
from Pokemon import pokemon

class kirin(pokemon):
    
    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('kirin', 'rayo', 125, 60, 70, 80, 'K', [self.ataque_1, self.ataque_2, self.ataque_3, self.ataque_4])
    
    # nombre, tipo, usos, damage, precision, descripcion
    ataque_1 = pokemon.ataque('Electro Lanza', 'rayo', 20, 60, 70, 'Carga un rayo que lanza al contrario que quizás lo paralice.')
    ataque_2 = pokemon.ataque('Sobrecarga', 'rayo', 10, 00, 100, 'Acumula electricidad para potenciar de sobremanera su velocidad.')
    ataque_3 = pokemon.ataque('Foco Eléctrico', 'rayo', 10, 0, 100, 'Inbulle su cuerpo en electricidad para aumentar su ataque.')
    ataque_4 = pokemon.ataque('Latigo', 'normal', 20, 50, 85, 'Lanza un coletazo que lo puede aturdir bajando su velocidad.')
