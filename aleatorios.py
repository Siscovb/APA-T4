"""
APA-T4 
Oriol Garcia Vila

Para esta entrega he usado el fichero de primos de una practica anterior que hicimos.
"""
import doctest
import primos as pr

###########################################################
class Aleat:
    """
    La clase Aleat genera un numero aleatorio usando el algoritmo LGC,
    Tiene los siguientes atributos que por defecto estan inicializados a un valor:
    m =2**48, a = 25214903917, c = 11, x0 = 1212121
    m --> módulo
    a --> multiplicador
    c --> incremento
    x0 --> semilla
    
    Genera un numero aleatorio usando el algoritmo LGC.
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
    def __init__(self, *, m =2**48, a = 25214903917, c = 11, x0 = 1212121):
        """
        Método mágico:
        Constructor de la clase Aleat, el cual tiene como parametros: m, a, c, x0
        Argumentos se tienen que indicar obligatoriamente por clave.
        Por defecto valen: m =2**48, a = 25214903917, c = 11, x0 = 1212121
        """
        
        self.m, self.a, self.c, self.x = m, a, c, x0
        
        #CONDICIONES:
        #m y c no deben tener factores primos en común
        #Si m es divisible por 4, a - 1 también debe serlo, pero no por 8
        if pr.mcd(m,c) != 1 : 
            if m%4 == 0: 
                if (a-1)%4 != 0:           
                    print('NO cumple alguna de las condiciones ')
                elif  (a-1)%8 == 0: 
                    print('NO cumple alguna de las condiciones ')
       
        #a−1 debe ser divisible por todos los factores primos de mm (aunque no mucho).
        if not all( (a-1) % primo == 0 for primo in pr.descompon(m)):
            print('NO Condicion optima ')
        
    
    def __next__(self):
        """
        Método mágico:
        Efectua la generación en si misma y devuelve el siguiente numero aleatorio generado
        """
        self.x = ((self.a * self.x) + self.c) % self.m
       
        #condición que el valor aleatorio tiene que ser menor que 'm'
        if self.x > self.m : 
            self.x = self.m -1
        return self.x
    
    def __call__(self, x, /):
        """
        Método mágico:
        Sobrecarga la llamada a función, 
        Se usará para reiniciar la secuencia con la semilla indicada en su único argumento, que será forzosamente posicional
        """
        self.x = x

###########################################################

def aleat(*,m =2**48, a = 25214903917, c = 11, x0 = 1212121):
    """
    La función aleat() genera un numero aleatorio usando el algoritmo LGC,
    Tiene los siguientes atributos que por defecto estan inicializados a un valor:
    m =2**48, a = 25214903917, c = 11, x0 = 1212121
    m --> módulo
    a --> multiplicador
    c --> incremento
    x0 --> semilla
    Comprobación del funcionamiento de aleat():
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    Comprobación del reinicio de aleat()
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
    #CONDICIONES:
    #m y c no deben tener factores primos en común
    #Si m es divisible por 4, a - 1 también debe serlo, pero no por 8
    if pr.mcd(m,c) != 1 : 
        if m%4 == 0: 
            if (a-1)%4 != 0:           
                print('NO cumple alguna de las condiciones ')
            elif  (a-1)%8 == 0: 
                print('NO cumple alguna de las condiciones ')
    
    #a−1 debe ser divisible por todos los factores primos de mm (aunque no mucho).
    if not all( (a-1) % primo == 0 for primo in pr.descompon(m)):
        print('NO Condicion optima ')


    while True :
        x0= (a * x0 + c) % m
        default = (yield x0)
        if default : x0 = default
    

doctest.testmod()
