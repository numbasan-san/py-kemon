
from Pokemon import pokemon

class golem(pokemon):

    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('golem', 'metal', 200, 80, 60, 40, 'G', [self.ataque_1, self.ataque_2, self.ataque_3, self.ataque_4])

    # nombre, tipo, usos, damage, precision, descripcion
    ataque_1 = pokemon.ataque('Coraza', 'metal', 20, 00, 100, 'Aumenta su defensa aumentando su dureza.')
    ataque_2 = pokemon.ataque('Diluvio Lítico', 'metal', 15, 70, 75, 'Levanta una roca gigante y la lanza al enemigo.')
    ataque_3 = pokemon.ataque('Sismo', 'metal', 10, 20, 100, 'Provoca un terremoto que reduce la velocidad del enemigo.')
    ataque_4 = pokemon.ataque('Impacto', 'normal', 20, 50, 90, 'Da un puñetazo al contrincante.')
