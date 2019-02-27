import sys

a=float(input('Insira o valor de a: '))
b=float(input('Insira o valor de b: '))
c=float(input('Insira o valor de c: '))

if a==0:
    print('Nao eh equacao de segundo grau')
    sys.exit()

delta=(b**2)-4*a*c
raizDelta=delta**0.5

if delta<0:
     print('A equacao nao possui raizes reais')
     sys.exit()
elif delta==0:
    print('A equacao possui apenas uma raiz real:')
    raiz=(-b)/(2*a)
    print('raiz da equacao: {0:.2f}'.format(raiz))
    sys.exit()
else:
    print('A equacao possui duas raizes reais:')
    raiz1=(-b+raizDelta)/(2*a)
    raiz2=(-b-raizDelta)/(2*a)
    print('Raiz 1 {0:.2f} e Raiz 2 {1:.2f}'.format(raiz1,raiz2))