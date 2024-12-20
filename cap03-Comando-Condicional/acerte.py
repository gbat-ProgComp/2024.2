import random

print('Tente acertar o número aleatório entre 1 e 100, você possui 4 tentativas restantes.')
x = int(input("Digite um número de 1 a 100: "))
y = (random.randint(1, 100))

tentativa1 = 1
tentativa2 = 2
tentativa3 = 3
tentativa4 = 4

    # teste de verificação
    #print(y)

if x == 0:
    exit

        #tentativa n1
        # Caso o usuário acerte de primeira
elif x == y:
        print('Parabéns, você acertou o número aleatório na primeira tentativa, você é algum tipo de médium ou algo assim?')

        #tentativa n2
        # Caso o número sorteado seja menor ou igual a 50

else:
    if y <= 25 and y >= 1:
        x = int(input('O valor está entre 1 e 25, tente de novo (Tentativas restantes: 3): '))
        if x == y:
            print('Parabéns, você acertou na tentativa número', tentativa2)
    elif y <= 50 and y > 25:
            x = int(input('O valor está entre 26 e 50, tente de novo (Tentativas restantes: 3): '))
            if x == y:
                print('Parabéns, você acertou na tentativa número', tentativa2)
    elif y <= 75 and y > 50:
            x = int(input('O valor está entre 51 e 75, tente de novo (Tentativas restantes: 3): '))
            if x == y:
                print('Parabéns, você acertou na tentativa número', tentativa2)
    elif y <= 100 and y > 75:
            x = int(input('O valor está entre 76 e 100, tente de novo (Tentativas restantes: 3): '))
            if x == y:
                print('Parabéns, você acertou na tentativa número', tentativa2)

            else:
                if y <= 12 and y >= 1:
                    x = int(input('O valor está entre 1 e 12, tente de novo (Tentativas restantes: 2): '))
                    if x == y:
                        print('Parabéns, você acertou na tentativa número', tentativa3)
                elif y <= 24 and y > 12:
                    x = int(input('O valor está entre 13 e 24, tente de novo (Tentativas restantes: 2): '))
                    if x == y:
                        print('Parabéns, você acertou na tentativa número', tentativa3)
                elif y <= 36  and y > 24:
                    x = int(input('O valor está entre 25 e 36, tente de novo (Tentativas restantes: 2): '))
                    if x == y:
                        print('Parabéns, você acertou na tentativa número', tentativa3)
                elif y <= 48 and y > 36:
                    x = int(input('O valor está entre 37 e 48, tente de novo (Tentativas restantes: 2): '))
                    if x == y:
                        print('Parabéns, você acertou na tentativa número', tentativa3)
                elif y <= 60 and y > 48:
                    x = int(input('O valor está entre 49 e 60, tente de novo (Tentativas restantes: 2): '))
                    if x == y:
                        print('Parabéns, você acertou na tentativa número', tentativa3)
                elif y <= 72 and y > 60:
                    x = int(input('O valor está entre 61 e 72, tente de novo (Tentativas restantes: 2): '))
                    if x == y:
                        print('Parabéns, você acertou na tentativa número', tentativa3)
                elif y <= 83 and y > 72:
                    x = int(input('O valor está entre 72 e 83, tente de novo (Tentativas restantes: 2): '))
                    if x == y:
                        print('Parabéns, você acertou na tentativa número', tentativa3)
                elif y <= 95 and y > 83:
                    x = int(input('O valor está entre 84 e 95, tente de novo (Tentativas restantes: 2): '))
                    if x == y:
                        print('Parabéns, você acertou na tentativa número', tentativa3)
                elif y <= 100 and y > 95:
                    x = int(input('Jackpot, você está na margem bônus, o alcance do seu número foi reduzido para 4 números e está entre 96 e 100! (Tentativas restantes: 2)'))
                    if x == y:
                        print('Parabéns, você acertou na tentativa', tentativa3)

                    else:
                        if y <= 6 and y >= 1:
                            x = int(input('O valor está entre 1 e 6, tente de novo (Tentativas restantes: 1): '))
                        if x == y:
                            print('Parabéns, você acertou na tentativa número', tentativa4)
                        elif y <= 13 and y > 6:
                            x = int(input('O valor está entre 7 e 13, tente de novo (Tentativas restantes: 1): '))
                        if x == y:
                            print('Parabéns, você acertou na tentativa número', tentativa4)
                        elif y <= 20  and y > 13:
                            x = int(input('O valor está entre 14 e 20, tente de novo (Tentativas restantes: 1): '))
                        if x == y:
                            print('Parabéns, você acertou na tentativa número', tentativa4)
                        elif y <= 27 and y > 20:
                            x = int(input('O valor está entre 21 e 27, tente de novo (Tentativas restantes: 1): '))
                        if x == y:
                            print('Parabéns, você acertou na tentativa número', tentativa4)
                        elif y <= 33 and y > 27:
                            x = int(input('O valor está entre 28 e 34, tente de novo (Tentativas restantes: 1): '))
                        if x == y:
                            print('Parabéns, você acertou na tentativa número', tentativa4)
                        elif y <= 40 and y > 33:
                            x = int(input('O valor está entre 34 e 40, tente de novo (Tentativas restantes: 1): '))
                        if x == y:
                            print('Parabéns, você acertou na tentativa número', tentativa4)
                        elif y <= 47 and y > 40:
                            x = int(input('O valor está entre 41 e 47, tente de novo (Tentativas restantes: 1): '))
                        if x == y:
                            print('Parabéns, você acertou na tentativa número', tentativa4)
                        elif y <= 54 and y > 47:
                            x = int(input('O valor está entre 48 e 54, tente de novo (Tentativas restantes: 1): '))
                        if x == y:
                            print('Parabéns, você acertou na tentativa número', tentativa4)
                        elif y <= 60 and y > 54:
                            x = int(input('O valor está entre 55 e 60, tente de novo (Tentativas restantes: 1): '))
                        if x == y:
                            print('Parabéns, você acertou na tentativa', tentativa4)
                        elif y <= 67 and y > 60:
                            x = int(input('O valor está entre 61 e 67, tente de novo (Tentativas restantes: 1): '))
                        if x == y:
                            print('Parabéns, você acertou na tentativa número', tentativa4)
                        elif y <= 74 and y > 67:
                            x = int(input('O valor está entre 68 e 74, tente de novo (Tentativas restantes: 1): '))
                        if x == y:
                            print('Parabéns, você acertou na tentativa número', tentativa4)
                        elif y <= 81 and y > 74:
                            x = int(input('O valor está entre 75 e 81, tente de novo (Tentativas restantes: 1): '))
                        if x == y:
                            print('Parabéns, você acertou na tentativa número', tentativa4)
                        elif y <= 88 and y > 81:
                            x = int(input('O valor está entre 82 e 88, tente de novo (Tentativas restantes: 1): '))
                        if x == y:
                            print('Parabéns, você acertou na tentativa número', tentativa4)
                        elif y <= 95 and y > 88:
                            x = int(input('O valor está entre 89 e 95, tente de novo (Tentativas restantes: 1): '))
                        if x == y:
                            print('Parabéns, você acertou na tentativa número', tentativa4)
                        elif y <= 100 and y > 95:
                            x = int(input('Jackpot, você está na margem bônus, o alcance do seu número foi reduzido para 4 números e está entre 96 e 100! (Tentativas restantes: 1)'))
                        if x == y:
                            print('Parabéns, você acertou na tentativa número', tentativa4)
                        else:
                            print('Que azar! Infelizmente suas tentativas acabaram, tente novamente ou feche a aplicação. O número era', y)