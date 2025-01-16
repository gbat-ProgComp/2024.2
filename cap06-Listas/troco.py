try:
    conta = int (input ("Valor da conta: "))
    pgto  = int (input ("Valor pago: "))
    
    if pgto > conta: 
        troco = pgto - conta
        print (f"O troco é R${troco}, formado por: ")
        for nota in [200, 100, 50, 20, 10, 5, 2 , 1]:
            nCed = troco // nota
            if nCed > 0:
                print (f"\t{nCed:4d} cédula(s) de R${nota:3d}")
            troco %= nota
    elif pgto < conta:
        print ("Pagamento insuficente!")
    else:
        print ("Obrigado!")
except ValueError as e:
    print ("Erro na entrada dos dados")