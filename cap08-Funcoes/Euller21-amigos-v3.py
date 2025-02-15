import timeit

def somaDivProp(n):
    somaDiv = 0
    for div in range(1, int(n**0.5)+1):
        if n%div == 0:
            otherDiv = n // div
            if div == otherDiv or otherDiv == n:
                somaDiv += div
            else:
                somaDiv += div + otherDiv
    return somaDiv

def genSomaAmigos(limite):
    somaAllAmigos = 0
    for a in range (1, limite+1):
        b = somaDivProp(a)
        if a < b:
            newa = somaDivProp(b)
            if a == newa:
                somaAllAmigos += a+b
    return somaAllAmigos

LIMITE = 10000
print(timeit.timeit(lambda: print(genSomaAmigos(LIMITE)), number=1))
