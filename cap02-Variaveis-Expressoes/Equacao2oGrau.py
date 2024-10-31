# Esse codigo foi desenvolvido por 
#    David Barbosa em Out/2024 no IFRN

a = int ( input('Digite o valor para a'))
b = int ( input('Digite o valor para b'))
c = int ( input ( 'Digite o valor para c'))
delta = b**2 - 4*a*c
print  ('o Valor de delta é igual', delta)
x1 =  (- b - delta ** (1/2)) / ( 2*a)
x2 = (- b + delta ** (1/2)) / ( 2*a)
print ( 'o Valor para um x é', x1 )
print ('o valor para dois x é:', x2 )