import sys

notaParcial1=float(input('Digite a nota parcial 1:'))
notaParcial2=float(input('Digite a nota parcial 2:'))
notaParcial3=float(input('Digite a nota parcial 3:'))

if notaParcial1<0 or notaParcial1>10:
    print('Nota invalida')
    sys.exit()

if notaParcial2<0 or notaParcial2>10:
    print('Nota invalida')
    sys.exit()

if notaParcial3<0 or notaParcial3>10:
    print('Nota invalida')
    sys.exit()

media= (notaParcial1+notaParcial2+notaParcial3)/3

if media>=7 and media<10:
    print('Aprovado. Media {0:.2f}'.format(media))
elif media<7:
    print('Reprovado. Media {0:.2f}'.format(media))
else: 
    print('Aprovado com distincao. Media {0:.2f}'.format(media))