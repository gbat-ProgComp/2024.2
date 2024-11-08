# Este progama lê três números inteiros e 
# os exibe em ordem crescente.
#   Galileu Batista, Nov/2024

MSG_ENTRADA = "Digite um número: "
MSG_ORDEM   = "Valores em ordem crescente:"

try:
    a = int (input(MSG_ENTRADA))
    b = int (input(MSG_ENTRADA))
    c = int (input(MSG_ENTRADA))
    
    if a < b:
        if c < a:
            print (MSG_ORDEM, c, a, b) 
        else:
            if c < b: 
                print (MSG_ORDEM, a, c, b) 
            else:
                print (MSG_ORDEM, a, b, c)
    else:
        if c < b:
            print (MSG_ORDEM, c, b, a)
        else:
           if c < a:
               print (MSG_ORDEM, b, c, a)
           else:
               print (MSG_ORDEM, b, a, c)
except:
    print ("Erro na conversão para int!")