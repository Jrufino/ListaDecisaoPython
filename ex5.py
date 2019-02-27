import sys

notaParcial1=float(input('Digite a primeira nota parcial do aluno: '))
if notaParcial1<0 or notaParcial1>10:
    print('Nota digitada nao eh valida')
    sys.exit()
else:
    pass
notaParcial2=float(input('Digite a segunda nota parcial do aluno: '))
media= (notaParcial1+notaParcial2)/2
if notaParcial2<0 or notaParcial2>10:
    print('Nota digitada nao eh valida')
    sys.exit()
else:
    pass

if media>=7 and media<10:
    print('Aprovado!')
elif media<7 and media>=0:
    print('Reprovado!')
else: 
    print('Aprovado com distincao')
