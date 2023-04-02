"""
Àlex Mata Barrero

Mòdul de gestió de nombres primers

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

>>> mcdN(820, 630, 1050, 1470)
10

"""

def esPrimo(numero):
    """
    Devuelve True si su argumento es primo, y False si no lo es.
    """
    
    for num_div in range(2, int(numero**0.5 + 1)):
        if numero % num_div == 0: return False
    else: return True

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.
    """

    return tuple([num_div for num_div in range(2,numero) if esPrimo(num_div)])

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    """

    factores = tuple()
    for factor in primos(numero + 1):
        while numero%factor == 0:
            numero = numero//factor
            factores = factores + (factor,) 
    return factores

def fact2dic(numero1, numero2):
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores =  set(factores1) | set(factores2)
    dic1 = {factor : 0 for factor in factores}
    dic2 = {factor : 0 for factor in factores}
    for factor in factores1:
        dic1[factor] += 1
    
    for factor in factores2:
        dic2[factor] += 1

    return dic1, dic2

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    """
    dic1, dic2 = fact2dic(numero1,numero2)
    mcm = 1
    for factor in dic1:
        mcm *= factor**max(dic1[factor],dic2[factor])
    return mcm

def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    """
    dic1, dic2 = fact2dic(numero1,numero2)
    mcd = 1
    for factor in dic1:
        mcd *= factor**min(dic1[factor],dic2[factor])
    return mcd

def fact2dicN(*numeros):
    factores_all = set()
    for numero in numeros:
        factores_num = set(descompon(numero))
        factores_all |= factores_num
    dic = [{factor : 0 for factor in factores_all} for _ in numeros]
    for i, numero in enumerate(numeros):
        for factor in descompon(numero):
            dic[i][factor] += 1
    return dic

def mcmN(*numeros):
    dic = fact2dicN(*numeros)
    mcm = 1
    max = 0
    for factor in dic[0]:
        for i, _ in enumerate(numeros):
            if dic[i][factor] > max: max= dic[i][factor]
        mcm *= factor**max
        max = 0
    return mcm

def mcdN(*numeros):
    dic = fact2dicN(*numeros)
    mcd = 1
    for factor in dic[0]:
        mcd *= factor**min([dic_[factor] for dic_ in dic])
    return mcd


import doctest
doctest.testmod()