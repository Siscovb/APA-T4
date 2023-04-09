"""
Ada Salvador Avalos


"""


class Aleat :
    """
    En esta clase se aplica el algoritmo de generación lineal congruente LGC que permite generar secuencias pseudoaleatorias 
    de características controladas.
    Como atributos uso self.m , self.a, self.c, self.xn que son los proporcionados por el constructor, gracias a 
    el que hace una instáncia de la clase Ej : x = Aleat(m = 1, a =2 ,c = 3, x0 = 4) respectivamente.
    self.xn0 es la semilla o valor inicial. Que uso en el iterador (__iter__).


    >>> rand = Aleat(m = 32, a=9, c = 13, x0 = 11)
    Si m es divisible por 4, a - 1 también debe serlo, pero no por 8.
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
    def __init__(self,m = 2**48, a = 25214903917, c= 11, x0 = 1212121) :
        """
        Método mágico __init__(), es el constructor de una clase que devuelve un objeto de la misma al invocarla como si
        fuera una función. En este caso, los valores de m, a y c y la semilla x0 son configurables al crear el objeto.
        A la vez que comprueba si los valores son óptimos para la generación de números aleatorios 
        usando el algoritmo LGC.

        """
        self.m = m
        self.a = a
        self.c = c
        self.xn = x0
        self.xn0 = x0
        # compruebo si las condiciones son óptimas 
        mcd_mc = self.mcd(self.m , self.c)
        if mcd_mc != 1 :
            print('m y c no deben tener factores primos en común.')

        descomm = self.descompon(self.m)
        if not all((self.a -1)% divm == 0 for divm in descomm) :
            print('a−1 debe ser divisible por todos los factores primos de m (aunque no mucho).')

        if self.m%4 == 0:
            if not((self.a -1)%4==0 and (self.a -1)%8 != 0) :   
                print('Si m es divisible por 4, a - 1 también debe serlo, pero no por 8.')
    

    def __iter__(self) :
        """
         Método mágico __iter__(), se utiliza para permitir que los objetos de la clase sean iterables.
        """
        self.xn = self.xn0
        return self

    def __next__(self) :
        """
        Método mágico __next__(),  efectua la generación en sí misma y devuelve el número aleatorio siguiente.
        
        """
        self.xn = (self.a * self.xn + self.c) % self.m
        return self.xn



    def __call__(self, semilla) :
         """
         El método mágico __call__() que sobrecarga la llamada a función, es decir, el uso del objeto como si fuera una función con sus argumentos entre paréntesis,
         se usa para reiniciar la secuencia con la semilla.
         """
         self.xn = semilla



# funciones cogidas de primos.py para poder hacer las comprobaciones en la clase Aleat()
# ---------------------------------------------------------------------
    def descompon(self, numero):
        """
        Devuelve una **tupla** con la descomposición en factores primos de su argumento.
        La función tiene como argumento un número.

        """
        i= 2
        factor = []
        while range(2,numero):

            if numero%i==0:
                numero= numero//i
                factor.append(i)
            else : 
                i=i+1
        return tuple(factor)


    def dicFact(self,numero1, *numero2):
        """
        Devuelve el factor primo de un número con su correspondiente exponente.
        La función tiene como argumento uno o varios números.

        """
        factores1 = self.descompon(numero1)
        factores2 = []   #lista vacía
        for numero in numero2:
            factores2.extend(self.descompon(numero)) # descompone el numero2 en factores primos  
        #y si se suma la lista creada a la lista factores2
    
        factores = set(list(factores1) + list(factores2)) #se suman factores1 y factores2
    #transformándolos en listas.
        dicfact1 = {factor: 0 for factor in factores}
        dicfact2 = {factor: 0 for factor in factores}
        for factor in factores1: dicfact1[factor] += 1
        for factor in factores2: dicfact2[factor] += 1
        return dicfact1, dicfact2


    def mcd(self,numero1, numero2):
        """
        Devuelve el máximo común divisor de sus argumentos.
        La función tiene como argumento dos números.

        """
        mcd = 1
        dicFact1, dicFact2 = self.dicFact(numero1, numero2)
        for factor in  dicFact1 | dicFact2:
            mcd *= factor ** min(dicFact1[factor],dicFact2[factor])
        return mcd

#------------------------------------------------------------------------------

def  aleat(m = 2**48, a = 25214903917, c= 11, x0 = 1212121)  :
    """
    En esta función se aplica el algoritmo de generación lineal congruente LGC que permite generar secuencias pseudoaleatorias 
    de características controladas.
    Se comprueba si los números son óptimos y implementa el generador de números aleatorios LGC.
    Como argumentos tiene por clave m = 2**48, a = 25214903917, c= 11 y x0 = 1212121, respectivamente.
    Proporciona como salida un número/s aleatorio/s y permite el reinicio de send() usando yield.
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...    print(next(rand))
    m y c no deben tener factores primos en común.
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
        # compruebo si las condiciones son óptimas 
    mcd_mc = mcd(m , c)
    if mcd_mc != 1 :
        print('m y c no deben tener factores primos en común.')

    descomm = descompon(m)
    if not all((a -1)% divm == 0 for divm in descomm) :
        print('a−1 debe ser divisible por todos los factores primos de m (aunque no mucho).')

    if m%4 == 0:
        if not((a -1)%4==0 and (a -1)%8 != 0) :   
                print('Si m es divisible por 4, a - 1 también debe serlo, pero no por 8.')
    

    xn = x0
    while True :
        xn= (a * xn + c) % m
        reset = (yield xn)
        if reset : xn = reset



# funciones cogidas de primos.py para poder hacer las comprobaciones en la función generadora aleat()
# ---------------------------------------------------------------------
def descompon(numero):
    """
    Devuelve una **tupla** con la descomposición en factores primos de su argumento.
    La función tiene como argumento un número.

    """
    i= 2
    factor = []
    while range(2,numero):

        if numero%i==0:
            numero= numero//i
            factor.append(i)
        else : 
            i=i+1
    return tuple(factor)


def dicFact(numero1, *numero2):
    """
    Devuelve el factor primo de un número con su correspondiente exponente.
    La función tiene como argumento uno o varios números.
    """
    factores1 = descompon(numero1)
    factores2 = []   #lista vacía
    for numero in numero2:
        factores2.extend(descompon(numero)) # descompone el numero2 en factores primos  
    #y si se suma la lista creada a la lista factores2

    factores = set(list(factores1) + list(factores2)) #se suman factores1 y factores2
#transformándolos en listas.
    dicfact1 = {factor: 0 for factor in factores}
    dicfact2 = {factor: 0 for factor in factores}
    for factor in factores1: dicfact1[factor] += 1
    for factor in factores2: dicfact2[factor] += 1
    return dicfact1, dicfact2


def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    La función tiene como argumento dos números.
    """
    mcd = 1
    dicFact1, dicFact2 = dicFact(numero1, numero2)
    for factor in  dicFact1 | dicFact2:
        mcd *= factor ** min(dicFact1[factor],dicFact2[factor])
    return mcd

#-----------------------------------------------------------------------


import doctest
doctest.testmod()

