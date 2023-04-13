"""
    Cuarta tarea de APA - Generación de números aleatorios

    Nombre y apellidos:
    Albert Giménez

"""

class Aleat:
    """
    Clase generadora de números aleatorios


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

    def __init__(self, m = 2 ** 48, a = 25214903917, c = 11, x0 = 1212121):
        """
        Costructor de la clase Aleat. 
        """

        self.m = m
        self.a = a
        self.c = c
        self.x0 = x0
        self.x = x0
        return None
    
    def __next__(self):
        """
        Método que genera el siguiente número aleatorio, y hace iterable la clase Aleat
        """

        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, semilla):
        """
        Método que sobrecarga la llamada a función, es decir, el uso del objeto como si fuera una función
        """

        self.x = semilla
        return None
    

def aleat(m = 2**48, a = 25214903917, c= 11, x0 = 1212121):
    """
    Esta función genera números aleatorios con el mismo protocolo que la clase definida previamente

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
        x = (a * x + c) % m
        siguiente = yield x
        if siguiente:
            x = siguiente
    return None

import doctest
doctest.testmod()   


