"""
PAU PERÁLVAREZ CASASAMPERE

Tarea 4 de APA - Generación de números aleatorios usando el algoritmo LGC
"""

class Aleat:
    """
    Clase iterable que genera números aleatorios utilizando
    el método LGC.

    Los argumentos de la función son:
    - módulo: m > 0
    - multiplicador: 0 < a < m
    - incremento: 0 <= c < m
    - valor inicial o semila: 0 <= x0 < m
    
    Los métodos de la clase son:
    - __init__(): Se inicializan los cuatro argumentos
    - __next__(): efectúa la generacion en sí mismo y 
    devuelve el número aleatorio siguiente 
    - __call__(): sobrecarga la llamada a función. 
    Necesita un argumento (valor de x0)


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
    def __init__(self, m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x0 = x0
        self.x = x0
    
    def __next__(self):
        self.x = ((self.x * self.a) + self.c) % self.m 
        return self.x
    
    def __call__(self, x0):
        self.x = x0


def aleat(m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
    """
    Generador de números aleatorios en el rango 0 <= xn < m

    Los argumentos de la función son:
    - módulo: m > 0
    - multiplicador: 0 < a < m
    - incremento: 0 <= c < m
    - valor inicial o semila: 0 <= x0 < m


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
    x = x0
    while True:
        x = ((x * a) + c) % m 
        i = (yield x)
        if i: x = i



import doctest
doctest.testmod()