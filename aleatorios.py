
def aleat(m=2**48, a=25214903917, c=11, x0=1212121):
    """
        La función se mantiene en un bucle infinito para mantener la iterabilidad.
        "yeild" es una palabra clave que sirve para devolver el siguiente aleatorio 
        y para asignar el valor dentro del metodo "send()" a la x0 actual siempre y cuando
        sea diferente de None  
        >>> rand = aleat(m=64, a=5, c=46, x0=36)
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
    while True: 
        x0 = (a * x0 + c) % m
        
        nuevax0 = yield x0
        if(nuevax0 is not None):
            x0 = nuevax0
        else:
            x0 = x0

class Aleat:
    """
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
        Constructor de clase que define todos los valores iniciales de la clase Aleat.
        En el caso de que el usuario cree el objeto sin valores estos tendran unos por defecto.
        """
        self.m, self.a, self.c, self.x0= m, a, c, x0

    def __iter__(self):
        """
        Metodo que hace que la clase sea iterable.
        """
        return self
    
    def __next__(self):
        """
        Método que genera el siguiente numero de la secuencia. 
        En este se actualiza el valor x0 cada vez que se usa.
        """
        self.x0 = (self.a * self.x0 + self.c) % self.m
        return self.x0
    
    def __call__(self, x0):
        """
        Método de la clase que permite que la clase sea llamada como una funcion.
        Aquí se reinicia la secuencia de numeros actualizando el valor x0 al valor deseado.
        """
        self.x0 = x0

import doctest
doctest.testmod()