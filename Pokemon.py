
from Ataque import ataque

class pokemon:

    def __init__(self, nombre, tipo, vida, defensa, damage, velocidad, sprite, ataques):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.defensa = defensa
        self.damage = damage
        self.velocidad = velocidad
        self.sprite = sprite
        self.ataques = ataques

    def ataque(nombre, tipo, usos, damage, precision, descripcion, funcion = None, efecto = False):
        atq = ataque(nombre, tipo, usos, damage, precision, descripcion, funcion, efecto)
        return atq
