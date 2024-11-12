# Esse codigo determina se um número de 3
# dígitos é palíndromo e foi desenvolvido por 
#    GALILEU Batista em Nov/2024 no IFRN

try:
    num = int(input("Digite um número: "))

    msg = ""
    if num // 100 != num % 10:
        msg = "não"
    print (num, msg, "é um palíndromo!")
          
except ValueError as e:
    print ("Erro na leitura do número!")