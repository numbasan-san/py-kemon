
from Pokemon import pokemon
import random

class kirin(pokemon):
    
    def __init__(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        super().__init__('kirin', 'rayo', 125, 60, 70, 80, 'K', [self.ataque_1(), self.ataque_2(), self.ataque_3(), self.ataque_4()])
    
    # nombre, tipo, usos, damage, precision, descripcion, funcion = None, efecto = False
    def ataque_1(self):
        return pokemon.ataque('Electro Lanza', 'rayo', 20, 60, 70, 'Carga un rayo que lanza al contrario que quizás lo paralice.')

    def ataque_2(self):
        return pokemon.ataque('Sobrecarga', 'rayo', 3, 00, 100, 'Acumula electricidad para potenciar de sobremanera su velocidad.', funcion = self.sobrecarga)

    def ataque_3(self):
        return pokemon.ataque('Foco Eléctrico', 'rayo', 3, 0, 100, 'Inbulle su cuerpo en electricidad para aumentar su ataque.', funcion = self.foco_electrico)

    def ataque_4(self):
        return pokemon.ataque('Latigo', 'normal', 20, 50, 85, 'Lanza un coletazo que lo puede aturdir, bajando su velocidad.', funcion = self.latigo, efecto = True)

    def sobrecarga(self):
        self.velocidad += int(self.velocidad * 0.25)
    
    def foco_electrico(self):
        self.damage += int(self.damage * 0.15)
    
    def latigo(self, criatura):
        ran = random.randint(1, 10)
        print(f'Dado: {ran}')
        if ran <= 2:
            criatura.velocidad -= int(criatura.velocidad * 0.05)

