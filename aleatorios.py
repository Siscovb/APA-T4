'''
Alexandr Ramos

Clase / Funcion : Aleat / aleat()
'''

class Aleat:
    """
    Classe Aleat
    """

    def __init__(self, *, m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
        """
        Inicialitzador amb parametres opcionals m, a, c, x0.
        Per defecte, tots tindran un valor inicial.
        S'han d'introduir per clau, no posicionalement.
        """
        if m == 2**48 and a == 25214903917 and c == 11 and x0 == 1212121:
            ...
        elif 0 < m and 0 < a and a < m and 0 <= c and c < m and 0 < x0 and x0 < m:
            ...
        else: print("Aquests inicialitzadors NO son adequants pel correcte funcionament de l'algoritme")

        self.m, self.a, self.c, self.x0 = m, a, c, x0

    def __next__(self):
        """
        Actualitza una iteració i retorna el resultat
        >>> rand = Aleat(m=32, a=9, c=13, x0=11)
        >>> for _ in range(4): print(next(rand))
        16
        29
        18
        15
        """
        self.x0 = ((self.a * self.x0) + self.c) % self.m
        return self.x0
    
    def __call__(self, x0, /):
        """
        Actualitza la llavor
        Nomes per invocació posicional
        >>> rand = Aleat(m=32, a=9, c=13, x0=11)
        >>> rand(29)
        >>> for _ in range(4): print(next(rand))
        18
        15
        20
        1
        """
        self.x0 = x0


"""
funció aleat()
"""
def aleat(m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
    """
    Funció que genera valor aleatori.
    Iterable amb next() i actualitzable amb send()
    Arguments invocables tant posicionalement com per clau.
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4): print(next(rand))
    34
    24
    38
    44

    >>> rand.send(24)
    38
    >>> for _ in range(4): print(next(rand))
    44
    10
    32
    14
    """
    if m == 2**48 and a == 25214903917 and c == 11 and x0 == 1212121:
        ...
    elif 0 < m and 0 < a and a < m and 0 <= c and c < m and 0 < x0 and x0 < m:
        ...
    else: print("Aquests inicialitzadors NO son adequants pel correcte funcionament de l'algoritme")
    
    while True:
        x0 = ((a * x0) + c) % m
        ret = yield x0
        if ret: x0 = ret


import doctest
doctest.testmod()