
from engine import *
from start_pokemon import *

print('Py-kemon.\n')
eng = engine()

while True:
    if eng.end_all == True: # Si termina el juego, se cierra todo.
        break
    eng.print_pokemones()