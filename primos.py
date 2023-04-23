import doctest

def esPrimo(numero):

    """
    Devuelve True si numero es primo y false si no lo es
    >>> [ numero for numero in range(2,50) if esPrimo(numero)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """

    if numero < 2:
        return False
    else:
        for i in range(2,numero):
            if numero % i == 0:
                return False
        return True

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que n.
    >>> [primos(50)]
    [(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)]
    """
    primes = [i for i in range(2, numero) if all(i % j != 0 for j in range(2, i))]
    return tuple(primes)

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de numero.
    >>> [descompon(36 * 175 * 143)]
    [(2, 2, 3, 3, 5, 5, 7, 11, 13)]
    """
    factors = []
    for factor in range(2, numero+1):
        while numero % factor == 0:
            factors.append(factor)
            numero //= factor
        if numero < 2:
            break
    return tuple(factors)


def dicFact(numero1,numero2):
    """
    Devuelve el factor primo de un número con su correspondiente exponente. 
    La función tiene como argumento dos números.
    >>> dicFact(90,14)
    ({2: 1, 3: 2, 5: 1, 7: 0}, {2: 1, 3: 0, 5: 0, 7: 1})
    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)

    factores = set(factores1 + factores2)  
    dicfact1 ={factor : 0 for factor in factores } 
    dicfact2 ={factor : 0 for factor in factores} 
    for factor in factores1 : dicfact1[factor] += 1 #añade 1 a la clave cada vez que encuentra un factor en el xonjunto
    for factor in factores2 : dicfact2[factor] += 1 
  
    return dicfact1,dicfact2
    
def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de los dos argumentos.
    >>> mcm(90, 14)
    630
    """
    mcm = 1
    dicFact1, dicFact2 = dicFact(numero1, numero2)
    for factor in  dicFact1 | dicFact2:
        mcm *= factor ** max(dicFact1[factor],dicFact2[factor]) # vas multiplican els factors comuns elevats am maxim exponent
    return mcm

def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de los dos argumentos.
    >>> mcd(924, 780)
    12
    """
    mcd = 1
    dicFact1, dicFact2 = dicFact(numero1, numero2)
    for factor in  dicFact1 | dicFact2:
        mcd *= factor ** min(dicFact1[factor],dicFact2[factor]) #exactament el mateix pero multiplicant perls factorscomuns amb el menor exponent
    return mcd

def dicFactN(*numeros):
    """
    Devuelve un diccionario con los factores primos de varios números con sus correspondientes exponentes.
    La función tiene como argumento una cantidad variable de números.
    """
    factores = set()
    for numero in numeros:
        factores |= set(descompon(numero))
    dicfacts = [{factor : 0 for factor in factores } for _ in numeros]
    for i, numero in enumerate(numeros):
        for factor in descompon(numero):
            dicfacts[i][factor] += 1
    return dicfacts

def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de varios números.
    La función tiene como argumento una cantidad variable de números.
    >>> mcm(42, 60, 70, 63)
    1260
    """
    mcm = 1
    dicfacts = dicFactN(*numeros)
    for factor in set().union(*dicfacts):
        mcm *= factor ** max([dicfact[factor] for dicfact in dicfacts])
    return mcm

def mcdN(*numeros):
    """
    Devuelve el máximo común divisor de varios números.
    La función tiene como argumento una cantidad variable de números.
    >>> mcd(820, 630, 1050, 1470)
    210
    """
    mcd = 1
    dicfacts = dicFactN(*numeros)
    for factor in set().union(*dicfacts):
        mcd *= factor ** min([dicfact[factor] for dicfact in dicfacts])
    return mcd


doctest.testmod()
