
from Pokemon import pokemon

class hipocampo:
    
    def start_hipocampo(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        return pokemon('hipocampo', 'agua', 60, 30, 50, 100, 'H',  [self.ataque_1(), self.ataque_2(), self.ataque_3(), self.ataque_4()])
    
    # nombre, tipo, usos, damage, precision, descripcion
    def ataque_1(self):
        return pokemon.ataque('Chorro Aguja', 'agua', 10, 80, 75, 'Lanza un chorro de agua a super preción.')

    def ataque_2(self):
        return pokemon.ataque('Culatazo', 'normal', 20, 50, 75, 'Lanza cozes y patadas que pueden aturdir al contrincante.')

    def ataque_3(self):
        return pokemon.ataque('Naufrajio', 'agua', 20, 30, 75, 'Hunde al contrincante bajando su defensa.', self.naufrajio, True)

    def ataque_4(self):
        return pokemon.ataque('Natatoria', 'agua', 8, 00, 100, 'Aumenta su velocidad al nadar.', self.natatoria)

    def naufrajio(self, criatura):
        criatura.defensa -= 5
        print('Defensa enemiga mermada.')

    def natatoria(self, own):
        own.velocidad += int(own.velocidad * 0.05)
        print('Velocidad propia aumentada.')
