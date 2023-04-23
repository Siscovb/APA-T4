"""
Pol Sedó i Mota
APA-T4 

"""
import doctest
import primos as pr # importamos el fitxero python que contiene las funciones mcd() i descompon()

##################################################################################################################################
class Aleat:
    """
    Esta clase usa el algoritmo de generacion linial (LGC) para generar numeros aleatorios con
    algunos parametros controlables. Estos parametros se inicializan por defecto como:
    m =2**48, a = 25214903917, c = 11, x0 = 1212121
    m es el módulo, a es el multiplicador, c es el incremento i x0 la semilla
    
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
        Metodo inicializador de la clase Aleat (constructor) inicializa los valores por defecto como:
        m =2**48, a = 25214903917, c = 11, x0 = 1212121
        """
        
        self.m, self.a, self.c, self.x = m, a, c, x0 #self.a refiere a la variable del objecto que se esta creando
                                                    # mientras que a es la variable que introduce uno por parametros
        
        # comprovando las siguientes condiciones:
        if pr.mcd(m,c) != 1 : #m y c no tienen factores primos comunes
            if m%4 == 0: 
                if (a-1)%4 != 0:                #Si m es divisible por 4, a - 1 también, pero no por 8
                    print('Las condiciones no se cumplen')
                else:
                    if(a-1)%8 == 0: 
                        print('Las condiciones no se cumplen ')
       
        #a−1 es divisible por todos los factores primos de m
        if not all( (a-1) % primo == 0 for primo in pr.descompon(m)):
            print('Las condiciones no se cumplen')
        
    
    def __next__(self):
        """
        Devuelve el siguiente numero aleatoria de la sequencia que se esta generando
        con el algoritmo LGC
        """
        self.x = ((self.a * self.x) + self.c) % self.m
        
        if self.x > self.m :            # compruba que x no sea nunca mayor a m 
            self.x = self.m -1
        return self.x
       

    
    def __call__(self, x, /): #se usa el caracter / para que solo se puedan pasar posicionalmente 
        """
        Este metodo reinicializa la sequencia LGC con una semilla concreta pasa por parametros
        """
        self.x = x

##################################################################################################################################

def aleat(*,m =2**48, a = 25214903917, c = 11, x0 = 1212121):
    """
    La función aleat() genera un numero aleatorio usando el algoritmo LGC,
    Se comprueban las conficiones y usa el generador de números aleatorios LGC.
    Como argumentos tiene por clave m = 2**48, a = 25214903917, c= 11 y x0 = 1212121
    Retorna una sequencia de numeros aleatorios i mediante diferentes metodos se puede iteral
    o volver a reinicializar con una semilla
    Valores por defecto:
    m =2**48, a = 25214903917, c = 11, x0 = 1212121
    Test aleat():
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44

    Test reinicializacion aleat()
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




    if pr.mcd(m,c) != 1 : #m y c no tienen factores primos comunes
        if m%4 == 0: 
            if (a-1)%4 != 0:           
                print('Las condiciones no se cumplen ')   #Si m es divisible por 4, a - 1 también
            elif  (a-1)%8 == 0: 
                print('Las condiciones no se cumplen')   #pero no por 8
    
    if not all( (a-1) % primo == 0 for primo in pr.descompon(m)):
        print('Las condiciones no se cumplen')

    #bucle para comprovar si es necesario reiniciar.
    while True :
        x0= (a * x0 + c) % m
        default = (yield x0)
        if default : x0 = default
    
##################################################################################################################################

doctest.testmod()