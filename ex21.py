import math

valorSaque=int(input('Digite o valor do saque: '))

notas100=int(valorSaque/100)

resto=valorSaque-notas100*100

if resto>=50:
    notas50=1
else:
    notas50=0
    
resto=resto-(notas50*50)

if resto>=40:
    notas20=2
elif resto<40 and resto>=20:
    notas20=1
else:
    notas20=0

resto=resto-(notas20*20)

if resto>=10:
    notas10=1
else:
    notas10=0

resto=resto-(notas10*10)

if resto>=5:
    notas5=1
else:
    notas5=0

resto=resto-(notas5*5)

if resto>=4:
    notas2=2
elif resto<4 and resto>=2:
    notas2=1
else:
    notas2=0

resto=resto-(notas2*2)

if resto==1:
    notas1=1
else:
    notas1=0


print('Notas de R$100:{}'.format(notas100))
print('Notas de R$50:{}'.format(notas50))
print('Notas de R$20:{}'.format(notas50))
print('Notas de R$10:{}'.format(notas10))
print('Notas de R$5:{}'.format(notas5))
print('Notas de R$2:{}'.format(notas2))
print('Notas de R$1:{}'.format(notas1))