"""
Alexandr Ramos

Aixo es un lleu codi que utilitza la Classe i la Funció descrita en Aleat.py
"""

import aleatorios as al

print('Creem un objecte de classe Aleat sense inicialitzadors')

rand = al.Aleat()
for _ in range(4): print(next(rand))

print('\nActualitzem la llavor')

rand(29)
for _ in range(4): print(next(rand))

print('\nInicialitzem un altre objecte amb arguments definits')

rand = al.Aleat(m=32, a=9, c=13, x0=11)
for _ in range(4): print(next(rand))

print('\nActualitzem la llavor')

rand(29)
for _ in range(4): print(next(rand))

print('\nUtilitzem la funció sense arguments definits')

rand = al.aleat()
for _ in range(4): print(next(rand))

print('\nUtilitzem la funció definint arguments')

rand = al.aleat(m=64, a=5, c=46, x0=36)
for _ in range(4): print(next(rand))

print('\nActualitzem la llavor')

rand.send(24)
for _ in range(4): print(next(rand))