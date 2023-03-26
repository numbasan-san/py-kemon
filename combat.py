
from hud import *
from utilities import *
import os

class combat:

    def __init__(self):
        self.hud = hud()
    
    def start_combat(self, criatura_0, criatura_1):
        while(criatura_1.vida > 0 or criatura_0.vida > 0):
            print(hud.combat_hud([criatura_0, criatura_1]))
            opt = utilities.pregunta('Elija uno de los ataques disponibles. ', 1, 4, -1) - 1
            damage = debilidad.calculate_damage(
                1.5, 
                debilidad.search_efects((criatura_0.ataques[opt]).tipo, criatura_1.tipo), 
                1, 
                criatura_0.damage, 
                (criatura_0.ataques[opt]).damage, 
                criatura_1.defensa
                )
            self.make_damage(criatura_1, damage)
            
            input('pulse neter para continuar')
            os.system('cls')

    def make_damage(self, criatura, damage):
        criatura.vida -= damage

'''
debilidad.calculate_damage(1.5, 
debilidad.search_efects((criatura[0].ataques[0]).tipo, criatura[1].tipo), 
1, 
criatura[0].damage, 
(criatura[0].ataques[0]).damage, 
criatura[1].defensa)}
'''
