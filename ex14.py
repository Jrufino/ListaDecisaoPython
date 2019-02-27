import sys

notaParcial1=float(input('Insira o valor da nota1: '))
if notaParcial1<0 or notaParcial1>10:
    print('Nota invalida')
    sys.exit()
notaParcial2=float(input('Insira o valor da nota2: '))
if notaParcial2<0 or notaParcial2>10:
    print('Nota invalida')
    sys.exit()
media=(notaParcial1+notaParcial2)/2

if media>=9 and media<=10:
    conceito='A'
elif media>=7.5 and media<9:
    conceito='B'
elif media>=6 and media<7.5:
    conceito='C'
elif media>=4 and media<6:
    conceito='D'
else:
    conceito='E'

if conceito=='A' or conceito=='B' or conceito=='C':
    print('APROVADO')
else:
    print('REPROVADO')
