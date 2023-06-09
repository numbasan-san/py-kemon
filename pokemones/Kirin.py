
from Pokemon import pokemon
import random

class kirin:

    def start_kirin(self):
        # nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques
        return pokemon('kirin', 'rayo', 125, 60, 70, 80, 'K', [self.ataque_1(), self.ataque_2(), self.ataque_3(), self.ataque_4()])
    
    # nombre, tipo, usos, damage, precision, descripcion, funcion = None, efecto = False
    def ataque_1(self):
        return pokemon.ataque('Electro Lanza', 'rayo', 20, 60, 70, 'Carga un rayo que lanza al contrario que quizás lo paralice.')

    def ataque_2(self):
        return pokemon.ataque('Sobrecarga', 'rayo', 3, 00, 100, 'Acumula electricidad para potenciar de sobremanera su velocidad.', funcion = self.sobrecarga)

    def ataque_3(self):
        return pokemon.ataque('Foco Eléctrico', 'rayo', 3, 0, 100, 'Inbulle su cuerpo en electricidad para aumentar su ataque.', funcion = self.foco_electrico)

    def ataque_4(self):
        return pokemon.ataque('Latigo', 'normal', 20, 50, 85, 'Lanza un coletazo que lo puede aturdir, bajando su velocidad.', funcion = self.latigo, efecto = True)

    def sobrecarga(self, own):
        own.velocidad += int(own.velocidad * 0.25)
        print('Velocidad propia aumentada.')
    
    def foco_electrico(self, own):
        own.damage += int(own.damage * 0.15)
        print('Fuerza propia aumentada.')
    
    def latigo(self, criatura):
        ran = random.randint(1, 10)
        if ran <= 2:
            criatura.velocidad -= int(criatura.velocidad * 0.05)
            print('Velocidad enemiga mermada.')

