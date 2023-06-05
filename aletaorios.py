''''
    T4 - Generación de números aleatorios
    Gerard Piqueras Codina
'''

import doctest

class Aleat:
    """
    Classe iterable Aleat : Generador de números aleatorios en el rango 0 <= xn < usando el método LGC

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """

    def __init__(self, m=2**48, a = 25214903917, c = 11, x0 = 1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x0 = x0
        self.xn = x0
    
    def __iter__(self) :
        return self
    
    def __next__(self):
        self.xn = ((self.a * self.xn) + self.c) % self.m
        return self.xn
    
    def __call__(self,x):
        self.xn = x


def aleat (m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
    """
    Implementa el mismo generador de números aleatorios en el rango 
    que en el ejercicio anterior.

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    
    xn = x0
    while True:
        xn = ((a * xn) + c) % m
        send = (yield xn)
        if send: xn = send

doctest.testmod()