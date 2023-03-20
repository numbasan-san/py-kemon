
from pokemones.Wendigo import *
from pokemones.Sirena import *
from pokemones.Hipocampo import *
from pokemones.Golem import *
from pokemones.Fenix import *
from pokemones.Kirin import *

class start_pokemon:
    
    def __init__(self):
        self.wendigo = wendigo()
        self.sirena = sirena()
        self.hipocampo = hipocampo()
        self.golem = golem()
        self.fenix = fenix()
        self.kirin = kirin()

    def loaded_pokemon(self):
        return [self.wendigo, self.sirena, 
                self.hipocampo, self.golem, 
                self.fenix, self.kirin]
