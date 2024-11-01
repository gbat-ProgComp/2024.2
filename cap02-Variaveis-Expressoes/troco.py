# Esse codigo foi desenvolvido por 
#    Jullyana Pessoa em Nov/2024 no IFRN

conta = (int(input("qual o valor da conta?")))
valorpago =(int(input("qual o valor pago?")))
troco = valorpago - conta
print("seu troco é:", troco)

notas200 = troco // 200
print("notas de 200", notas200)
troco = troco - notas200 * 200

notas100 = troco // 100
print("notas de 100", notas100)
troco = troco - notas100 * 100

notas50 = troco // 50
print("notas de 50", notas50)
troco = troco - notas50 * 50

notas20 = troco // 20
print("notas de 20", notas20)
troco = troco - notas20 * 20

notas10 = troco // 10
print("notas de 10", notas10)
troco = troco - notas10 * 10

notas5 = troco // 5
print("notas de 5", notas5)
troco = troco - notas5 * 5

notas2 = troco // 2
print("notas de 2", notas2)
troco = troco - notas2 * 2

moeda1 = troco // 1
print("moedas de 1", moeda1)
troco = troco - moeda1 * 1
 



