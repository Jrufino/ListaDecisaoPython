num1=float(input('Digite o primeiro numero: '))
num2=float(input('Digite o segundo numero: '))
num3=float(input('Digite o terceiro numero: '))

if num1>num2 and num1>num3:
    primeiroNumero=num1
elif num2>1 and num2>num3:
    primeiroNumero=num2
else:
    primeiroNumero=num3

if num1<num2 and num1<num3:
    ultimoNumero=num1
elif num2<1 and num2<num3:
    ultimoNumero=num2
else:
    ultimoNumero=num3

if primeiroNumero!=num1 and ultimoNumero!=num1:
    segundoNumero=num1
elif primeiroNumero!=num2 and ultimoNumero!=num2:
    segundoNumero=num2
else:
    segundoNumero=num3

print('Ordem decrescente {} {} {}'.format(primeiroNumero,segundoNumero,ultimoNumero))
