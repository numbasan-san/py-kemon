
from Pokemon import pokemon

class hipocampo(pokemon):
    
    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('hipocampo', 'agua', 60, 30, 50, 85, 'H',  [self.ataque_1, self.ataque_2, self.ataque_3, self.ataque_4])
    
    # nombre, tipo, usos, damage, precision, descripcion
    ataque_1 = pokemon.ataque('Chorro Aguja', 'agua', 10, 80, 75, 'Lanza un chorro de agua a super preción.')
    ataque_2 = pokemon.ataque('Culatazo', 'normal', 20, 50, 75, 'Lanza cozes y patadas que pueden aturdir al contrincante.')
    ataque_3 = pokemon.ataque('Naufrajio', 'agua', 20, 30, 75, 'Hunde al contrincante bajando su defensa.')
    ataque_4 = pokemon.ataque('Natatoria', 'agua', 20, 00, 100, 'Aumenta su velocidad al nadar.')
