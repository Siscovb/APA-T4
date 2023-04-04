"""
    APA-T4
    
    Rafal A. Echevarria Silva

    Cuarta tarea de APA 2023: Generación de números aleatorios
"""
import doctest

class Aleat:
    """
    Generador de números aleatorios en el rango 0 < x_n < m usando el método LGC.

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

    def __init__(self, *, m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x_n = x0
        return None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.x_n = (self.a * self.x_n + self.c) % self.m
        return self.x_n
    
    def __call__(self, seed):
        if seed != None: self.x_n = seed
    

def aleat(*, m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
    """
    Función que implementa el mismo generador de números aleatorios.

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

    x_n = x0
    while True:
        x_n = (a * x_n + c) % m
        seed = yield x_n
        if seed is not None:
            x_n = seed


doctest.testmod()