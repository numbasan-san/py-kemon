
from start_pokemon import *
from utilities import *
from hud import *
from combat import *
import os

class engine:

    def __init__(self):
        self.start_pokemon = start_pokemon()
        self.hud = hud()
        self.combat = combat()
        self.end_all = False

    def print_pokemones(self):
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
        self.game_over()
    '''
    def print_combat(self, elegidos):
        self.hud.combat_hud(elegidos[0], elegidos[1])
    '''

    def select_pokemon(self):
        selected = []

        for i in range(len(self.start_pokemon.loaded_pokemon())):
            print(f'#{i + 1}\n{self.hud.info_hud(self.start_pokemon.loaded_pokemon()[i])}')

        for i in range(2):
            opt = utilities.pregunta('Elija uno de los disponibles. ', 1, len(self.start_pokemon.loaded_pokemon()), -1) - 1
            print(f'elejido: {self.start_pokemon.loaded_pokemon()[opt].nombre}')
            selected.append(self.start_pokemon.loaded_pokemon()[opt])

        os.system('cls')
        print(self.combat.start_combat(selected))

    def game_over(self):
        option = utilities.opciones('Terminar? Y, N ', ['Y', 'N'])
        if option == 'Y':
            self.end_all = True
