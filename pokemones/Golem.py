
from Pokemon import pokemon

class golem(pokemon):

    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('golem', 'metal', 200, 80, 60, 40, 'G', [self.ataque_1(), self.ataque_2(), self.ataque_3(), self.ataque_4()])

    # nombre, tipo, usos, damage, precision, descripcion
    def ataque_1(self):
        return pokemon.ataque('Coraza', 'metal', 5, 00, 100, 'Aumenta su defensa aumentando su dureza.', funcion = self.coraza)

    def ataque_2(self):
        return pokemon.ataque('Diluvio Lítico', 'metal', 15, 70, 75, 'Levanta una roca gigante y la lanza al enemigo.')

    def ataque_3(self):
        return pokemon.ataque('Sismo', 'metal', 10, 40, 100, 'Provoca un terremoto que reduce la velocidad del enemigo.', self.sismo, True)

    def ataque_4(self):
        return pokemon.ataque('Impacto', 'normal', 20, 50, 90, 'Da un puñetazo al contrincante.')

    def coraza(self):
        self.defensa += int(self.defensa * 0.1)
    
    def sismo(self, criatura):
        criatura.velocidad -= 4
