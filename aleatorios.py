"""
APA TAREA 4

Milene Granda

Pruebas unitarias:
Clase Aleat:
    
     Prueba unitaria para la comprobación del funcionamiento de Aleat:
     >>> rand = Aleat (m=32, a=9, c=13, x0=11)
     >>> for _ in range(4):
     ...      print(next(rand))
     16
     29
     18
     15

     Prueba unitaria para la comprobación del reinicio de Aleat:
     >>> rand(29)
     >>> for _ in range(4):
     ...     print(next(rand))
     ...
     18
     15
     20
     1

         

Función aleat():
     >>> rand = aleat(m=64, a=5, c=46, x0=36)
     >>> for _ in range(4):
     ...     print(next(rand))
     34
     24
     38
     44

     Prueba unitaria del comprobamiento del renicio de aleat():
     >>> rand.send(24)
     38
     >>> for _ in range(4):
     ...     print(next(rand))
     44
     10
     32
     14
         
"""


class Aleat:
     """
    Clase usada para implementar un generador de números aleatorios
    en el rango 0 <= xn < usando LGC 
    """
     # Método que toma 4 argumentos indicados por clave los cuáles se utilizan para generar num aleatorios a través del método LGC
     def __init__(self,*,m = 2**48, a =252149093917,c=11,x0=1212121 ):
          self.m = m
          self.a = a
          self.c = c
          self.xn = x0

     # Método que devuelve la instancia actual

     def __iter__(self):
          return self
     
    #Método que calcula el siguiente número aleatorio de acuerdo a la fórmula indicada en e método
     def __next__(self):
          self.xn = (self.a * self.xn +self.c) % self.m
          return self.xn
     
     #Método que actualiza la 'semilla' de la secuencia de los núeros aleatorios con un valor diferente al anterior
     def __call__(self,seed):
          self.xn = seed

     def send(self,seed):
          self.xn = seed
          return next(self)

     # Función generadora aleat() que implementa el mismo generador de num aleatorios en el rango 0<xn<m usando LGC
def aleat(m = 2**48, a =252149093917, c=11, x0=1212121):
     #La semilla inicial es x0 y se mantiene en xn
     xn =x0 
     while True:
          xn =(a*xn+c) % m
          seed = yield xn
          if seed is not None:
               xn=seed

          

import doctest
doctest.testmod()