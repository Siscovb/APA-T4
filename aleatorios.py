class Aleat:
    '''
    Clase que implementa un generador de números del rango 0<=Xn<=m usando el método LGC.
    
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

    def __init__(self, m=2**31 - 1, a=1103515245, c=12345, x0=1212121):
        '''
        Creamos el método __init__ para obtener un conjunto de variables que sean configurables, y que
        tengan por defecto un valor.
        '''
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __next__(self):
        '''
        Con este método realizamos la generación y devuelve el número aleatorio siguiente.
        '''
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, num):
        '''
        Reinicia la secuencia con el argumento indicado entre paréntesis.
        '''
        self.x = num

def aleat(m=2**31 - 1, a=1103515245, c=12345, x0=1212121):
    '''
    Esta función realiza la misma operación que la clase previa.
    Primero asignamos valores. Luego creamos un bucle en el cual actualizamos el valor de x en cada iteración y lo devolvemos utilizando el método yield.
    Cada vez que num tenga un nuevo valor, se realizará el retorno y se mostrarán los números.

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
    x = x0
    while True:
        x = (a * x + c) % m
        num = yield x
        if num is not None:
            x = num

if __name__ == "__main__":
    import doctest
    doctest.testmod()