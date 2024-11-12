salario = int(input("Digite oo valor do salario: "))

if salario <= 2250.20:
     print("está isento do imposto d renda")
     irpf = 0

elif 2259.21 <= salario <= 2826.65: 
     print ("o valor da aliquota é 7.5%,o valor da parcela a pagar é R$ 169.44")
     irpf = 7.5/100 * salario - 169.44

elif 2826.66 <= salario <= 3751.05: 
     print ("o valor da aliquota é 15%,o valor da parcela a pagar é R$ 381.44")
     irpf = 15/100 * salario - 381.44

elif 3751.06 <= salario <= 4664.68:
     print ("o valor da aliquota é 22.5%,o valor da parcela a pagar é R$662.77")
     irpf = 22.5/100 * salario - 662.77

elif salario > 4664.69:
     print ("o valor da aliquota é 27.5%,o valor da parcela a pagar é R$ 896")
     irpf = 27.5/100 * salario - 896

print ("o valor do imposto de renda é: ", irpf)