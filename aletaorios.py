"""
    Cuarta Tarea : Generación numeros aleatorios

    Nombre y apellidos: Kirian Rodríguez Alonso
"""

class Aleat:
    def __init__(self, m=2**48, a=25214903917, c=11, x0=1212121):
        """
        Definimos los valores iniciales (m,a,c,x0).
        """
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def  __next__(self):
        """
        Generamos el valor y devuelve el siguiente valor.
        """
        self.x = (self.a * self.x + self.c) % self.m
        return self.x