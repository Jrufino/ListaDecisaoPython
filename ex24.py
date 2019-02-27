import math
import sys

opcao=str.upper(input('Escolha uma opcao: a- adicao|s-subtracao|d-divisao|m-multiplicacao: '))

num1=int(input('Digite o primeiro numero: '))
num2=int(input('Digite o segundo numero: '))


if opcao=='A':
    resultado=num1+num2
elif opcao=='S':
    resultado=num1-num2
elif opcao=='D':
    resultado=num1/num2
elif opcao=='M':
    resultado=num1*num2
else:
    print('Opcao invalida')
    sys.exit

print('Resultado da operacao: {}'.format(resultado))

if resultado%2==1:
    print('Eh impar')
else:
    print('Eh par')

if resultado>=0:
    print('Eh positivo')
else:
    print('Eh negativo')

if math.ceil(resultado)==resultado:
    print('Eh inteiro')
else:
    print('Eh decimal')