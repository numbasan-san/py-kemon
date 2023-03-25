
from engine import *

print('Py-kemon.')
print()
eng = engine()

while True:
    if eng.end_all == True:
        break
    eng.print_pokemones()
