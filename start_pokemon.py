
from pokemones.Wendigo import *
from pokemones.Sirena import *
from pokemones.Hipocampo import *
from pokemones.Golem import *
from pokemones.Fenix import *
from pokemones.Kirin import *

from Pokemon import *

# Para inicializarlo todo y tener todo en el mismo lugar.
class start_pokemon:
    
    def __init__(self):
        self.wendigo = wendigo()
        self.sirena = sirena()
        self.hipocampo = hipocampo()
        self.golem = golem()
        self.fenix = fenix()
        self.kirin = kirin()

    def loaded_pokemon(self):
        return [self.wendigo.start_wendigo(), self.sirena.start_sirena(), 
                self.hipocampo.start_hipocampo(), self.golem.start_golem(), 
                self.fenix.start_fenix(), self.kirin.start_kirin()]
