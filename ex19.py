import math

num=int(input('Digite um numero inteiro menor que 1000:'))

centenas=int(num/100)
dezenas=int((num%100)/10)
unidades=((num%100)%10)

if centenas==0 or centenas==1:
    print('{} centena'.format(centenas))
else: 
    print('{} centens'.format(centenas))

if dezenas==0 or dezenas==1:
    print('{} dezena'.format(dezenas))
else: 
    print('{} dezenas'.format(dezenas))

if unidades==0 or unidades==1:
    print('{} unidade'.format(unidades))
else: 
    print('{} unidades'.format(unidades))

