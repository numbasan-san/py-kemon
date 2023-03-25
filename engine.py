
from start_pokemon import *
from utilities import *
from hud import *
import os

class engine:

    def __init__(self):
        self.start_pokemon = start_pokemon()
        self.hud = hud()
        self.end_all = False

    def print_pokemones(self):
        """
        criaturas = [self.start_pokemon.wendigo, self.start_pokemon.sirena, 
                     self.start_pokemon.hipocampo, self.start_pokemon.golem, 
                     self.start_pokemon.fenix, self.start_pokemon.kirin]
        """
        print(f'Tenemos estos "pokemones":')
        for criatura in self.start_pokemon.loaded_pokemon():
            print(f'{self.hud.info_hud(criatura)}')
        self.print_info_pokemon()
    
    def print_info_pokemon(self):
        opt = utilities.opciones('¿Quiere ver la información de algún pokemon? Y, N ', ['Y', 'N'])
        if opt == 'Y':
            os.system('cls')
            for i in range(len(self.start_pokemon.loaded_pokemon())):
                print(f'#{i + 1}\n{ self.hud.info_hud(self.start_pokemon.loaded_pokemon()[i]) }')
            opt = utilities.pregunta('Elija uno de los disponibles. ', 1, len(self.start_pokemon.loaded_pokemon()), -1) - 1
            os.system('cls')
            print(self.hud.info_hud(self.start_pokemon.loaded_pokemon()[opt], all = True))
            input('Pulse enter para salir.')
        else:
            os.system('cls')
            self.select_pokemon()
        
        os.system('cls')

    def print_combat(self, elegidos):
        self.hud.combat_hud(elegidos[0], elegidos[1])
        self.game_over()

    def select_pokemon(self):
        selected = []

        for i in range(len(self.start_pokemon.loaded_pokemon())):
            print(f'#{i + 1}\n{self.hud.info_hud(self.start_pokemon.loaded_pokemon()[i])}')

        for i in range(2):
            opt = utilities.pregunta('Elija uno de los disponibles. ', 1, len(self.start_pokemon.loaded_pokemon()), -1) - 1
            print(f'elejido: {self.start_pokemon.loaded_pokemon()[opt].nombre}')
            selected.append(self.start_pokemon.loaded_pokemon()[opt])

        os.system('cls')
        print(self.hud.combat_hud(selected))

        self.game_over()
    
    # same type attack bonus, efecto, variacion, nivel, ataque, potencia, defensa
    def calculate_damage(stab, eft, var, lvl, atk, ptnc, defe):
        return ( 0.01 * stab * eft * var ( ( ( (0.2 * lvl + 1) * atk * ptnc ) / 25 * defe) + 2 ) )

    def game_over(self):
        option = utilities.opciones('Terminar? Y, N ', ['Y', 'N'])
        if option == 'Y':
            self.end_all = True
