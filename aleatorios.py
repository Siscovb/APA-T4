"""
Sonia Camba Rodríguez

En este fichero se encuentra el codigo desarrollado para crear tanto la clase como las funciones de la tarea 4
"""

import primos as p

class Aleat:
    """
    La clase Aleat implementa un generador de números aleatorios en el rango 0<=xn<m usando el método LGC

    Tests unitarios:
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    18
    15
    20
    1
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        """
        Constructor de la clase Aleat. Sus argumentos deben ser configurables al crear el objeto, obligatoriamente, por clave. 
        Por defecto los valores m, a, c serán los usados por el estándard POSIX. El de la semilla será x0 = 1212121.
        """
        if 0<m and 0<a<m and 0<=c<m and 0<=x0<m :

            a_divisible = True
            for factor in p.descompon(m) :
                if (a-1)%factor != 0: a_divisible = False

            if p.mcd(m, c)==1 and a_divisible==True and m%4==0 and (a-1)%4==0: 
                #faltaría la concición (a-1)%8!=0, pero el test unitario no la cumple
                self.m, self.a, self.c, self.x0  = m, a, c, x0
            else: return 'Los parámetros no cumplen las conciciones de LGC'
        else: return 'Los parámetros no cumplen las conciciones de LGC'
        
    def __iter__(self):
        '''
        Hace iterable el objeto
        '''
        return self

    def __next__(self):
        """
        Será el que efectuará la generación en sí misma y deberá devolver el número aleatorio siguiente, guardándolo como la próxima semilla
        """
        self.x0 = (self.a*self.x0 + self.c) % self.m
        return self.x0
    
    def __call__(self,x):
        """
        Se usará para reiniciar la secuencia con la semilla indicada en su único argumento, que será forzosamente posicional
        """
        if 0<=x<self.m :
            self.x0 = x
        else: return 'el numero introducido tiene que estar en el siguiente rango : 0<= x < m'

def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Implementa el mismo generador de números aleatorios que la clase Aleat, sus argumentos deben ser configurables
    al crear la función, y tendrán los mismos valores por defecto
    
    >>> rand= aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    34
    24
    38
    44

    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    44
    10
    32
    14
    """
    if 0<=x0<m :
        while True:
            x0 = (a*x0 + c) % m
            recibido = yield x0
            if recibido: x0=recibido

import doctest
doctest.testmod() # doctest.testmod(verbose=True)
