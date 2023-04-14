"""
Oriol Garcia Moreiras

Modulo de gestión de numeros primos

Exemples: 

>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcmN(42, 60, 70, 63)
1260

>>> mcdN(840, 630, 1050, 1470)
210
"""

def esPrimo(numero):
    """
    Devuelve True si su argumento es primo y False si no lo es. 
    """

    for proba in range(2, int (numero**0.5 + 1)):
        if numero % proba == 0:
            return False
    return True


def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.
    """

    return tuple ([proba for proba in range(2, numero) if esPrimo(proba)])


def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    """

    factores = tuple()
    for factor in primos(numero + 1):
        while numero%factor == 0:
            numero = numero/factor
            factores = factores + (factor,)

    return factores

    
def fact2dic(numero1, numero2):
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores = set(factores1) | set(factores2)
    dic1 =  {factor : 0 for factor in factores}
    dic2 =  {factor : 0 for factor in factores}
    for factor in factores1: 
        dic1[factor] += 1

    for factor in factores2: 
        dic2[factor] += 1
    
    return dic1, dic2

    
def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    """
    dic1, dic2 = fact2dic(numero1, numero2)
    mcm = 1
    for factor in dic1:
        mcm *= factor**max(dic1[factor], dic2[factor])
    return mcm

def mcd(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    """
    dic1, dic2 = fact2dic(numero1, numero2)
    mcd = 1
    for factor in dic1:
        mcd *= factor**min(dic1[factor], dic2[factor])
    return mcd

def mcmN(*numeros):
    '''
    Devuelve el mínimo común múltiplo de sus argumentos.
    '''
    desc, lista = (), []
    total = 1
    for i in range(len(numeros)):
        desc += (descompon(numeros[i]), )
        for j in descompon(numeros[i]):
            lista.append(j)
    tots = set(lista)
    dic_total = {item:0 for item in tots}
    for i in range(len(numeros)):
        dic = {item:0 for item in tots}
        for num in desc[i]:
            dic[num] += 1
        for num in tots:
            if(dic_total[num] < dic[num]):
                dic_total[num] = dic[num]  
    for num in tots:
        total *= num**dic_total[num]
    return total

def mcdN(*numeros):
    '''
    Devuelve el mínimo común divisor de sus argumentos.
    '''
    desc, lista = (), []
    total = 1    
    for i in range(len(numeros)):
        desc += (descompon(numeros[i]), )
        for j in descompon(numeros[i]):
            lista.append(j)
    tots = set(lista)
    dic_total = {item:0 for item in tots}
    for i in desc[0]:
        dic_total[i] += 1
    for i in range(len(numeros)):
        dic = {item:0 for item in tots}
        for num in desc[i]:
            dic[num] += 1
        for num in tots:
            if(dic_total[num] > dic[num]):
                dic_total[num] = dic[num]  
    for num in tots:
        total *= num**dic_total[num]
    return total

import doctest
doctest.testmod()