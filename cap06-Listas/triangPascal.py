'''
    Programa para gerar o triângulo de Pascal
    por Galileu Batista - IFRN Dez 2024
'''

limite = int (input("Quantas linha do triângulo de Pascal: "))

l = [1]
print (l)
n = 1

while n < limite:
    l = [1] + [l[pos] + l[pos+1] for pos in range(len(l)-1)] + [1]
    print (l)
    n += 1
    
num = int (input("Qual o número a procurar: "))
ultPos = -1
for pos in range(len(l)):
    if l[pos] == num:
        ultPos = pos

print (f"A última ocorrência de {num} é na posição {ultPos}")