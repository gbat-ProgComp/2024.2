import timeit

def somaDivProp(n):
    somaDiv = 0
    for div in range(1, n//2+1):
        if n%div == 0:
            somaDiv += div
    return somaDiv

def genSomaAmigos(limite):
    somaAllAmigos = 0
    for a in range (1, limite+1):
        for b in range (a+1, limite+1):
            if somaDivProp(a) == b and somaDivProp(b) == a:
                somaAllAmigos += a+b
    return somaAllAmigos

LIMITE = 1000
print(timeit.timeit(lambda: print(genSomaAmigos(LIMITE)), number=1))
