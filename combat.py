
from hud import *
from utilities import *
import os

class combat:

    def __init__(self):
        self.hud = hud()
        self.turno_0 = True

    def start_combat(self, criaturas):
        while(True):
            jugadores = criaturas if self.turno_0 == True else criaturas[::-1]
            criatura_0, criatura_1 = jugadores[0], jugadores[1]
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
                    if (criatura_0.ataques[opt]).efecto == True:
                        (criatura_0.ataques[opt]).funcion(criatura_1)
                    else:
                        (criatura_0.ataques[opt]).funcion()
                        
                print(f'{criatura_0.nombre} ha usado {(criatura_0.ataques[opt]).nombre}.')
            else:
                print(f'El ataque {(criatura_0.ataques[opt]).nombre} no se puede usar más.')
            
            if (criatura_1.vida < 1 or criatura_0.vida < 1):
                ganador = criatura_0.nombre if criatura_1.vida < 1 else criatura_1 
                input(f'{ganador} ha ganado.')

            input('pulse enter para continuar')
            os.system('cls')
        
            if (criatura_1.vida < 1 or criatura_0.vida < 1):
                break
            self.turno_0 = not(self.turno_0)
        '''
        '''
            

    def reduce_uses(self, ataque):
        ataque.usos -= 1

    def make_damage(self, criatura, damage):
        criatura.vida -= damage
