num1=float(input('Digite o primeiro numero: '))
num2=float(input('Digite o segundo numero: '))
num3=float(input('Digite o terceiro numero: '))

if num1>num2 and num1>num3:
    maiorNumero=num1
elif num2>1 and num2>num3:
    maiorNumero=num2
else:
    maiorNumero=num3

print('O maior numero foi {}'.format(maiorNumero))