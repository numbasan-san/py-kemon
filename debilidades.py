
class debilidades:

    def __init__(self):
        self.fuego = {
            'hielo': 2, 
            'volador': 1.25,
            'metal': 1,
            'fuego': 1,
            'rayo': 1, 
            'agua': 0.5 
        }
        self.hielo = {
            'volador': 2, 
            'metal': 1.25, 
            'agua': 1, 
            'hielo': 1, 
            'rayo': 1, 
            'fuego': 0.5
        }
        self.volador = {
            'rayo': 2, 
            'agua': 1.25, 
            'metal': 1, 
            'volador': 1, 
            'fuego': 0.75, 
            'hielo': 0.5
        }
        self.rayo = {
            'metal': 2, 
            'agua': 1.25, 
            'rayo': 1, 
            'volador': 1, 
            'fuego': 1, 
            'volador': 0.5
        }
        self.metal = {
            'agua': 2, 
            'metal': 1, 
            'volador': 1, 
            'fuego': 1, 
            'hielo': 0.75, 
            'rayo': 0.5
        }
        self.agua = {
            'fuego': 2, 
            'hielo': 1.25, 
            'volador': 1, 
            'agua': 1, 
            'rayo': 0.75, 
            'metal': 0.5
        }

    def search_efects(self, tipo_ataque, tipo_pokemon_enemigo):
        elements = {
            'fuego': self.fuego, 
            'hielo': self.hielo, 
            'volador': self.volador, 
            'rayo': self.rayo, 
            'metal': self.metal, 
            'agua': self.agua
        }
        if tipo_ataque == 'normal' or tipo_pokemon_enemigo == 'normal':
            print(f'El tipo del ataque es {tipo_ataque}. Tipo de pokemon enemigo: {tipo_pokemon_enemigo}. Efecto del ataque x{1}')
            return 1
        else:
            listado = elements[tipo_ataque]
            print(f'El tipo del ataque es {tipo_ataque}. Tipo de pokemon enemigo: {tipo_pokemon_enemigo}. Efecto del ataque x{listado[tipo_pokemon_enemigo]}')
            return listado[tipo_pokemon_enemigo]

    # same type attack bonus, efecto, variacion, nivel, ataque, potencia, defensa
    @staticmethod
    def calculate_damage(stab, eft, var, atk, ptnc, defe):
        final_dmg = 0.01 * stab * eft * var * ( ( ( ( 0.2 + 1 ) * atk * ptnc ) / ( 25 * defe ) ) + 2 )
        return int(final_dmg * 100) if ptnc > 0 else 0
