# Calculando se um número é decrescente

try: 
    numero = int(input("Digite um numero de 04 dígitos: "))
    num_inicial = numero

    #Capturando o número mais significativo
    a = numero // 1000 
    numero %= 1000

    b = numero // 100
    numero %= 100

    c = numero // 10
    numero %= 10

    d = numero // 1

    msg = "é decrescente!"
    if a >= b:
        if b >= c:
            if c >= d:
                print(num_inicial, msg)
    else:
        print(num_inicial, 'não', msg)
except ValueError as e:
    print('Insira um número válido! ')