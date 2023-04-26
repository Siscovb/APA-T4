"""
Paula Puigdevall Tornero

Classe i funció generadores de seqüencies de nombres aleatoris partint de l'algoritme LGC
"""
class Aleat:
    """
    Classe generadora de nombres aleatoris.
    Mètodes utilitzats:
    __init__ per inicialitzar els valors dels atributs
    __next__ per tal d'obtenir el següent nombre aleatori
    __call__ per reiniciar la seqüencia de nombres aleatoris

    Pel que fa als atributs m, a, c, se'ls hi atribueix el valor predeterminat per el generador 
    aleatori de l'estandar POSIX. 
    La x0 sera la que es dona a l'enunciat.

    Exemples:

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
        # Els valors d'inici de cada atribut son els que venen predeterminats per el generador aleatori del estandar POSIX
        # El valor de X0 es el que ve donat a l'enunciat.
        self.m = m
        self.a = a
        self.c = c
        self.x0 = x0

    def __next__(self):
        self.x0 = (self.a * self.x0 + self.c) % self.m  # Per tal de generar el següent nombre aleatori utilitzem l'algoritme LGC.
        return self.x0      # Retorna el següent valor aleatori
    
    def __call__(self, nou):
        self.x0 = nou       # Reinicia la seqüencia amb la nova x0 indicada a l'argument nou.
    

def aleat(m = 2 ** 48, a = 25214903917, c = 11, x0 = 1212121):
    """
    Funció de generació de nombres aleatoris. Acabarà fent el mateix que la classe però sense utilitzar mètodes.

    Exemples:
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
    x = x0                       # Inicialitzem x                       
    while True:                  # Bucle per generar el següent nombre aleatori
        x = (x * a + c) % m      # Tornem a utilitzar l'algoritme LGC
        nou = yield x            # Utilitzem la funció yield per tal de reinicialitzar la seqüencia amb una nova x
        if nou is not None:
            x = nou


import doctest
doctest.testmod()
