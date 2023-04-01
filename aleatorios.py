"""
    Cuarta tarea de APA - Generación de números aleatorios

    Nombre y apellidos:
    Albert Giménez

Exemples:


    
    
"""

class Aleat:
    "Clase generadora de números aleatorios"
    def __init__(self, m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
        """
        Costructor de la clase Aleat. 
        """
        i=0
        self.alea = list()
        self.alea.append(x0)
        while self.alea(i) <= m:
            self.alea.append((self.alea(i) * a) + c)
            i += 1
        return None
    