
from start_pokemon import *
from utilities import *
from hud import *

class engine:

    def __init__(self):
        self.start_pokemon = start_pokemon()
        self.hud = hud()
        self.end_all = False

    def print_pokemones(self):
        criaturas = [self.start_pokemon.wendigo, self.start_pokemon.sirena, 
                     self.start_pokemon.hipocampo, self.start_pokemon.golem, 
                     self.start_pokemon.fenix, self.start_pokemon.kirin]
        for criatura in self.start_pokemon.loaded_pokemon():
            # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
            # ━ ┃ ┏ ┓ ┗ ┛ ┣ ┫ ┳ ┻ ╋
            self.hud.info_hud(criatura)
        
        option = utilities.opciones('Terminar? Y, N ', ['Y', 'N'])

        if option == 'Y':
            self.end_all = True
    
    def print_combat(self):
        self.hud.combat_hud([self.start_pokemon.wendigo, self.start_pokemon.sirena])
        
        option = utilities.opciones('Terminar? Y, N ', ['Y', 'N'])

        if option == 'Y':
            self.end_all = True
