"""
Gerard Escardó Cabrerizo

P4 - Generación de números aleatorios usando el algoritmo LGC
"""

class Aleat:
    """
    Descripción del cometido de la clase:
    Genera números aleatorios usando el método LGC.

    Descripción de los atributos y métodos de la clase:
    - __init__(): Se inicializa el objecto con los argumentos.
    - __next__(): Efectúa la generacion en sí mismo y devuelve el número aleatorio siguiente.
    - __call__(): Sobrecarga la llamada a función.
    
    Las pruebas unitarias correspondientes:
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
    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        """
        Parametros de la función (por defecto): m=2**48, a=25214903917, c=11, x0=1212121
        Argumentos por clave
        """
        self.m = m
        self.a = a
        self.c = c
        self.x = x0
    
    def __next__(self):
        self.x = ((self.a * self.x) + self.c) % self.m 
        return self.x
    
    def __call__(self, x0, /):
        """
        Argumento posicional
        """
        self.x = x0


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Descripción del cometido de la función:
    Generador de números aleatorios en el rango (0 <= xn < m).
    
    Argumentos de la función:
    - módulo: m > 0
    - multiplicador: 0 < a < m
    - incremento: 0 <= c < m
    - valor inicial o semila: 0 <= x0 < m

    Salida proporcionada:
    Número aleatorio.

    Pruebas unitarias correspondientes:   
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
        i = (yield x)
        if i : x = i



import doctest
doctest.testmod()