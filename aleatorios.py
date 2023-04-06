"""
    FICHERO ALEATORIOS.PY
 
    Gisela León
    
    PRUEBAS UNITARIAS:
     
    Clase Aleat:
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
    
    Función generadora aleat():
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


class Aleat:
    """
   
    Clase que implementa el generador de números aleatorios en el rango 0 <= xn < m
    usando el método LGC
    
    """
    
    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m      #Por defecto, los valores de m, a y c serán los usados por el estándar POSIX
        self.a = a
        self.c = c
        self.x = x0
    
    # Los valores de m, a, c y x0 son configurables al crear el objeto, 
    # y la semilla puede reiniciarse en cualquier momento usando la llamada a la función sobrecargada __call__().
    
    def __iter__(self):
        return self
    
    def __next__(self): #Efectua la generación en sí misma y devuelve el número aleatorio siguiete
        self.x = (self.a * self.x + self.c) % self.m
        return self.x
    
    def __call__(self, seed): #Reinicia la secuencia con la semilla indicada en su único argumento
        self.x = seed  
    
    def send(self, seed):
        self.x = seed
        return next(self)
        
        
def aleat(m=2**48, a=25214903917, c=11, x0=1212121):
    """
    La función aleat() es una función generadora que implementa la misma lógica que la clase Aleat, 
    pero sin necesidad de crear un objeto iterable. 
    
    """
    # Usa los mismos parámetros que la clase Aleat, con valores por defecto iguales.
    x = x0      # La semilla inicial es x0 y se mantiene en la variable x
    while True:                 #En cada iteración, la función calcula el siguiente valor de la secuencia      
        x = (a * x + c) % m     #pseudoaleatoria usando la fórmula del LGC y lo devuelve con yield 
        seed = yield x 
        if seed is not None:
            x = seed
    #Si se envía un valor al generador con send(), se reinicia la secuencia con ese valor como nueva semilla.
    #En ambos casos, la semilla se puede reiniciar utilizando el método __call__() o send().

import doctest
doctest.testmod()
