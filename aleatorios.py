import time

"""
    Cuarta tarea de APA - manejo de vectores
    Nombre y apellidos: Victor Ceballos Fouces
"""

class Aleat:
    """
    Clase Aleat que genera numeros aleatorios en el rango 0 ≤ xn ≤ m usando el metodo LGC.
    
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
        Inicializa los valores de m, a, c y x0
        """

        self.m, self.a, self.c, self.x0= m, a, c, x0
    
    def __next__(self):
        """
        Método mágico _next_() que será el encargado de la generación aletoria
        y deberá devolver el número aleatorio siguiente.
        """
        self.x0 = (self.a * self.x0 + self.c) % self.m
        return self.x0
    
    def __call__(self, x0):
        """
        Establece el valor de x0
        """
        self.x0 = x0
    
    def __iter__(self):
        """
        Devuelve un objeto iterable para la clase
        """
        return self
    

def aleat(m=2**48, a=25214903917, c=11, x0=1212121):
    """
    La función aleat genera números aleatorios en el rango 0 ≤ xn ≤ m utilizando el método LGC.
    Los argumentos m, a, c y x0 son los valores necesarios para generar números aleatorios.

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
        """
        El bucle while en el cuerpo de la función genera números aleatorios indefinidamente.
        El valor generado se devuelve mediante el uso de la declaración yield.
        Si un valor seed se proporciona, se utiliza para establecer el valor de x en lugar del valor generado.
        """
        x = (a * x + c) % m
        seed = yield x
        if seed is not None:
            x = seed
        else:
            x = x



import doctest
doctest.testmod(verbose = True)