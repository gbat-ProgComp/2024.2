# Esse codigo foi desenvolvido por 
#    Julio Cesar em Nov/2024 no IFRN

Captal = float(input("Digite o valor da divida: "))
Tempo = int(input("Digite o tempo da divida: "))
Taxa = float(input("Digite valor da taxa: "))

Montante = round(Captal * (1 + Taxa/100)**Tempo, 2)
print("Sua divida é: ", Montante)