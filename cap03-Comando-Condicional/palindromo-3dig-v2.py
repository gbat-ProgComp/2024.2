# Esse codigo determina se um número de 3
# dígitos é palíndromo e foi desenvolvido por 
#    GALILEU Batista em Nov/2024 no IFRN

try:
    num = int(input("Digite um número: "))

    direto = num
    inverso = 0

    d = num % 10
    inverso = inverso * 10 + d
    num //= 10

    d = num % 10
    inverso = inverso * 10 + d
    num //= 10

    d = num % 10
    inverso = inverso * 10 + d
    num //= 10
    
    msg = ""
    if direto != inverso:
        msg = "não"
    print (direto, msg, "é um palíndromo!")
          
except ValueError as e:
    print ("Erro na leitura do número!")