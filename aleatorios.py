class Aleat():
    """
    Esta clase es el algoritmo de generacion lineal congruente LGC que permite generar secuencias pseudoaleatorias.
    
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)

    >>> for _ in range(4):
            print(next(rand))
     16
     29
     18
     15

    >>> rand(29)

    >>> for _ in range(4):
            print(next(rand))
    18
    15
    20
    1
    
    
    """

    def __init__(self, m=2E+48, a=25214903917, c = 11, x0 = 1212121 ):
        """
        Método magico que es el constructor de la clase.
        """
        self.m = m
        self.a = a
        self.c = c
        self.x0 = x0
        self.xn = x0
    
    def __iter__(self):
        """
        Método magico iterador que permiten a los objectos ser iterables.
        """

        self.xn = self.x0
        return self


    def __next__(self):
        """
        Método magico que genera y devuelve el valor aleatorio.
        """
        xn1 = ((self.a * self.xn) + self.c) % self.m
        return xn1
        
    def __call__(self,semilla):
        """
        Método magico que reinicia la secuencia con un nuevo valor de semilla.

        """
        self.xn = semilla

def aleat(m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
    """
    Función que genera el algoritmo LGC.

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

    while True:
     x0 = ((a * x0) + c) % m
     val = yield x0
     if val : x0 = val


import doctest
doctest.testmod()