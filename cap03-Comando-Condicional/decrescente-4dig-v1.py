# Calculando se um número é decrescente

try: 
    numero = int(input("Digite um numero de 04 dígitos: "))
    
    numInicial = numero
    ehDescrecente = True
    base = 0
    
    last = numero % 10
    if last < base:
        ehDescrecente = False
    base = last
    numero = numero // 10

    last = numero % 10
    if last < base:
        ehDescrecente = False
    base = last
    numero = numero // 10

    last = numero % 10
    if last < base:
        ehDescrecente = False
    base = last
    numero = numero // 10

    last = numero % 10
    if last < base:
        ehDescrecente = False
    base = last
    numero = numero // 10

    msg = "é decrescente!"
    if not ehDescrecente:
        print(numInicial, 'não', msg)
    else:
        print(numInicial, msg)
except ValueError as e:
    print('Insira um número válido! ')