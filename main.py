
from engine import *
from start_pokemon import *

print('Py-kemon.')
print()
eng = engine()


'''
str_pok = start_pokemon()
print(f'velo: {str_pok.wendigo.velocidad}')
str_pok.wendigo.ataques[1].funcion()
print(f'velo: {str_pok.wendigo.velocidad}')

'''
while True:
    if eng.end_all == True:
        break
    eng.print_pokemones()