"""
    APA T4

    Nombre y apellidos: Àlex Mata Barrero

    Generación de nombres aleatorios con el algoritmo LGC.

""" 

from primos import descompon
import doctest

class Aleat:
    def __init__(self, m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
        """
        Classe Aleat que genera un nombre aleatori seguint l'algoritme LGC.

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

        ## COMENTAT, JA QUE NO CAL QUE COMPROVEM L'ADEQUACIÓ ##
        # primos_m = descompon(m)
        # primos_c = descompon(c)

        # for factor in primos_m:
        #     if factor in primos_c: raise
        
        # for factor in primos_m:
        #     if (a-1)%factor != 0: raise
        
        # if (m % 4 == 0):
        #     if (a - 1) % 4 == 0:
        #         if (m & (m - 1)) == 0: # comprovem que m sigui potència de 2:
        #             # quan un número és ^2, en binari, per exemple: 10000. Si li restem 1, 01111. Si fem and de 10000 i 01111 == 0.
        #             if (a - 1) % 8 == 0: raise
        #     else: raise
    
        self.m = m
        self.a = a
        self.c = c
        self.x_n = x0


    def __iter__(self):
        return self


    def __next__(self):
        self.x_n = (self.a * self.x_n + self.c) % self.m
        return self.x_n 


    def __call__(self,x):
        if x != None: self.x_n = x


def aleat(m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
    """
    Funció aleat que genera un nombre aleatori seguint l'algoritme LGC. 
    Es fa ús de la interrupció yield, per tal de poder enviar valors externs a la funció durant l'execució d'aquesta.

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
    ## COMENTAT, JA QUE NO CAL QUE COMPROVEM L'ADEQUACIÓ ##
    # primos_m = descompon(m)
    # primos_c = descompon(c)
    # for factor in primos_m:
    #     if factor in primos_c: raise
    
    # for factor in primos_m:
    #     if (a-1)%factor != 0: raise

    # if (m % 4 == 0):
    #     if (a - 1) % 4 == 0:
    #         if (m & (m - 1)) == 0: # comprovem que m sigui potència de 2:
    #             # quan un número és ^2, en binari, per exemple: 10000. Si li restem 1, 01111. Si fem and de 10000 i 01111 == 0.
    #             if (a - 1) % 8 == 0: raise
    #     else: raise
    x_n = x0

    while True:
        x_n = (a * x_n + c) % m
        envio = yield x_n
        if envio != None: x_n = envio

doctest.testmod()