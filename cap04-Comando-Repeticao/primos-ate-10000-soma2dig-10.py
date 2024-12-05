numero = 2

while True: 
    primo = True
    for x in range(2, int(numero ** 0.5) + 1):
        if numero % x == 0:
            primo = False
            break  
         
    if primo == True:
        print (numero)
        doisDigitos = numero
        while doisDigitos > 100:
            doisDigitos //= 10

        soma_digitos = doisDigitos // 10 + doisDigitos % 10       
        if soma_digitos == 9:
            print("O tal primo é:", numero)
            break
    
    numero += 1