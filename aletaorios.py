"""
    Cuarta tarea de APA - Generación de números aleatorios

    Nombre y apellidos: Marina Fresneda Manzano
"""

import doctest
import primos 

class Aleat:
    '''
    Clase que implementa un generador de números aleatorios en el rango 0<=xn<m usando el método LGC
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
    '''

    def __init__(self, m=2**48, a=25214903917, c=11, x0 = 1212121):
        '''
        Costructor de la clase Aleat. Sus argumentos son los estándares POSIX
        '''
        self.m = m
        self.a = a
        self.c = c
        self.xn = x0


    def __iter__(self):
        '''
        Método que permite que el objeto sea iterable 
        '''
        return self


    def __next__(self):
        '''
        Método que permite obtener el siguiente elemento de una secuencia de objetos
        '''
        self.x = (self.a * self.x + self.c) % self.m
        return self.x
    

    def __call__(self, semilla):
        '''
        Método que sobrecarga la llamada a función
        '''
        self.xn = semilla
    

    def aleat(m=2**48, a=25214903917, c=11, x0 = 1212121):
        '''
        Función que implementa el generador de números aleatorios
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

        '''

        xn = x0
        while True:
            xn = (a * xn + c) % m
            yield xn / m            #normaliza el número aleatorio generado en el rango [0, 1)
            n_sem = yield
            if n_sem is not None:
                xn = n_sem