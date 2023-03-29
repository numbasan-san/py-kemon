
from Pokemon import pokemon

class wendigo:

    def start_wendigo(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        return pokemon('wendigo', 'hielo', 100, 40, 65, 60, 'W', [self.ataque_1(), self.ataque_2(), self.ataque_3(), self.ataque_4()])

    # nombre, tipo, usos, damage, precision, descripcion
    def ataque_1(self):
        return pokemon.ataque('Desgarre', 'normal', 20, 65, 75, 'Corta al otro con las garras.')

    def ataque_2(self):
        return pokemon.ataque('Cacería', 'normal', 5, 0, 100, 'Aumenta la velocidad.', self.caceria)

    def ataque_3(self):
        return pokemon.ataque('Asalto', 'normal', 20, 50, 70, 'Salta hacia al enemigo.')

    def ataque_4(self):
        return pokemon.ataque('Fauces', 'normal', 20, 50, 75, 'Muerde al enemigo.')

    def caceria(self, own):
        own.velocidad += int(own.velocidad * 0.1)
        print('Velocidad incrementada.')

# 6600 AMD