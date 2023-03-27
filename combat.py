
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
            # same type attack bonus, efecto, variacion, nivel, ataque, potencia, defensa
            damage = debilidad.calculate_damage(
                1.5, 
                debilidad.search_efects((criatura_0.ataques[opt]).tipo, criatura_1.tipo), 
                1, 
                criatura_0.damage, 
                (criatura_0.ataques[opt]).damage, 
                criatura_1.defensa
                )
            self.make_damage(criatura_1, damage)
            if (criatura_0.ataques[opt]).usos > 0:
                self.reduce_uses((criatura_0.ataques[opt]))
                if (criatura_0.ataques[opt]).funcion != None:
                    (criatura_0.ataques[opt]).funcion()
                print(f'{criatura_0.nombre} ha usado {(criatura_0.ataques[opt]).nombre}.')
            else:
                print(f'El ataque {(criatura_0.ataques[opt]).nombre} no se puede usar más.')
            input('pulse enter para continuar')
            os.system('cls')

    def reduce_uses(self, ataque):
        ataque.usos -= 1

    def make_damage(self, criatura, damage):
        criatura.vida -= damage
