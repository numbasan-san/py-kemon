
import random
import sys
import time
from hud import *
from utilities import *
import os

# Para llevar cuenta y a cabo todo la lógica de combate.
class combat:

    def __init__(self):
        self.hud = hud()
        self.turno_0 = True

    # EL núcleo del sistema de combate.
    def start_combat(self, criaturas):

        while(True):
            criatura_0, criatura_1 = (criaturas[0], criaturas[1]) if self.turno_0 else (criaturas[1], criaturas[0])
            print(f'Turno de: {criaturas[0].nombre if self.turno_0 else criaturas[1].nombre}')
            
            # Se carga la interfáz.
            print(hud.combat_hud([criaturas[0], criaturas[1]]))

            # Se manda a elejir un ataque.
            if self.turno_0:
                opt = utilities.pregunta('Elija uno de los ataques disponibles. ', 4) - 1
            else:
                opt = self.random_ia()

            '''
                Fórmula de evasión:
                    ((criatura_0.ataques[opt]).precision) * (criatura_0.precision / criattura_1.velocidad)

                No existe el atributo "precision" en los "pokemon", solo en los ataques, por lo que no sé qué atributo ya existente usar. Y la fórmula original dicta que el denominador debe ser la evasión, pero no tengo eso por lo que velocidad y ya.

                Nmms, que hueva implementar el sistema de evasión.
            '''

            # Se calcula el daño y se efectua, junto al efecto que este tenga. También se reduce el uso del ataque.
            # same type attack bonus, efecto, variacion, nivel, ataque, potencia, defensa
            stab = 1.5 if (criatura_0.ataques[opt]).tipo == criatura_0.tipo else 1
            var = (random.randint(85, 100)) / 100
            efecto = debilidad.search_efects((criatura_0.ataques[opt]).tipo, criatura_1.tipo)
            damage = debilidad.calculate_damage(
                stab, 
                efecto, 
                var, 
                criatura_0.damage, 
                (criatura_0.ataques[opt]).damage, 
                criatura_1.defensa
            )

            self.print_effect(f'\n{criatura_0.nombre} ha usado {(criatura_0.ataques[opt]).nombre}.\n')

            if (criatura_0.ataques[opt]).usos > 0:
                self.reduce_uses((criatura_0.ataques[opt]))
                var = random.randint(1, 100)
                if var < (criatura_0.ataques[opt]).precision:
                    self.make_damage(criatura_1, damage)
                    # En verdad que esto podría ser más bonito, pero ñeh.
                    if damage > 0:
                        if efecto == 0.5:
                            self.print_effect('Es muy poco efectivo.\n')
                        elif efecto == 0.75:
                            self.print_effect('Es poco efectivo.\n')
                        elif efecto == 1.25:
                            self.print_effect('Es muy efectivo.\n')
                        elif efecto == 2:
                            self.print_effect('Es super efectivo.\n')
                    if (criatura_0.ataques[opt]).funcion != None:
                        if (criatura_0.ataques[opt]).efecto == True:
                            (criatura_0.ataques[opt]).funcion(criatura_1)
                        else:
                            (criatura_0.ataques[opt]).funcion(criatura_0)
                else:
                    self.print_effect(f'\n{criatura_0.nombre} ha fallado {(criatura_0.ataques[opt]).nombre}.')

                self.turno_0 = not(self.turno_0)

            else:
                self.print_effect(f'\nEl ataque {(criatura_0.ataques[opt]).nombre} no se puede usar más.')

            if (criatura_1.vida <= 0 or criatura_0.vida <= 0):
                os.system('cls')
                print(hud.combat_hud([criaturas[0], criaturas[1]]))
                perdedor = criaturas[0].nombre if criaturas[0].vida <= 0 else criaturas[1].nombre 
                ganador = criaturas[0].nombre if criaturas[1].vida <= 0 else criaturas[1].nombre 
                self.print_effect(f'{perdedor} no puede continuar.')
                self.print_effect(f'{ganador} ha ganado.')
                break
            else:
                input('\nPULSE ENTER PARA CONTINUAR')
                os.system('cls')

    # Para reducir los usos de un ataque.
    def reduce_uses(self, ataque):
        ataque.usos -= 1

    # Para efectuar el ataque.
    def make_damage(self, criatura, damage):
        criatura.vida -= damage

    def random_ia(self):
        return random.randint(0, 3)
    
    def print_effect(self, s):
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)
