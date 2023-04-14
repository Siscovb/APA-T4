"""
Cuarta tarea de APA 2023: Generación de números aleatorios
Nom i cognoms: Oriol Garcia Moreiras
"""

import primos as pr

class Aleat:
    """
    En esta clase se aplica el algoritmo de generación lineal congruente LGC que permite generar secuencias pseudoaleatorias de características controladas,
    explicado de forma más simple esta clase implementa un generador de números aleatorios en el rango 0<=xn<m usando el método LGC.

    Los atributos utilizados son los proporcionados por el constructor: self.m , self.a, self.c, self.x.
    Donde:
    m --> módulo
    a --> multiplicador
    c --> incremento
    x0 --> semilla

    Comprobación del funcionamiento de 'Aleat':
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))    
    16
    29
    18
    15

    Comprobación del reinicio de 'Aleat':
    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    18
    15
    20
    1
    
    """
    def __init__(self, *, m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
        """
        Método que tiene como parámetros (m, a, c, x0).
        Estos parámetros tiene que indicarse por clave.
        Por defecto: m =2**48, a = 25214903917, c = 11, x0 = 1212121
        En resumen definimos los valores iniciales (m,a,c,x0).
        """
        self.m, self.a, self.c, self.x = m, a, c, x0

        # Debe cumplir:
        if pr.mcd(m,c) != 1 :  # m y c no deben tener factores primos en común
            if not all((a - 1)% primoss == 0 for primoss in pr.descompon(m)):  #a−1 debe ser divisible por todos los factores primos de mm (aunque no mucho).
                if m%4 == 0: #Si m es divisible por 4
                    if (a - 1) % 4 != 0:  # a - 1 también debe serlo        
                        print('NO cumple alguna de las condiciones ')
                    elif  (a - 1) % 8 == 0:  # Pero no por 8
                        print('NO cumple alguna de las condiciones ')
    
    def __iter__(self):
        '''
        Hace iterable el objeto
        '''
        return self

    def  __next__(self):
        """
        Método utilizado para generar el valor (numero aleatorio generado)
        y devolver el siguiente valor (siguiente numero aleatorio generado).
        """
        self.x = ((self.a * self.x) + self.c) % self.m
        return self.x

    def __call__(self,x): 
        """
        Metodo que sobrecarga la llamada a función, es decir reinicia la secuencia
        con la semilla indicada en su único argumento.
        """
        self.x = x

def aleat(m = 2**48, a = 25214903917, c = 11,x0 = 1212121):
    """
    Esta función que implementa el mismo generador de números aleatorios en el rango
    0 <= x < m  que en el ejercicio anterior pero sin crear un objecto iterable. Tendrá los mismos atributos (m, a, c, x0). Donde:
    m --> módulo
    a --> multiplicador
    c --> incremento
    x0 --> semilla
    Los cuales tienen los siguientes valores por defecto:
    m =2**48, a = 25214903917, c = 11, x0 = 1212121

    Comprobación del funcionamiento de aleat():
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    Comprobación del reinicio de aleat():
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
    # Debe cumplir:
    if pr.mcd(m,c) != 1 :  # m y c no deben tener factores primos en común
        if not all((a -1)% primoss == 0 for primoss in pr.descompon(m)):  # a − 1 debe ser divisible por todos los factores primos de mm (aunque no mucho).
            if m % 4 == 0: #Si m es divisible por 4
                if (a-1) % 4 != 0:  # a - 1 también debe serlo        
                    print('NO cumple alguna de las condiciones ')
                elif  (a-1) % 8 == 0:  # Pero no por 8
                    print('NO cumple alguna de las condiciones ')

    while True:
        x0 = (a * x0 + c) % m #pseudoaleatoria usando LGC y lo devuelve con yield 
        readjust = (yield x0)
        if readjust : x0 = readjust
 
import doctest
doctest.testmod()