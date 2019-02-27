num1=int(input('Digite um numero: '))
num2=int(input('Digite mais um numero: '))

if num1>num2:
    print('O maior numero eh o numero {}'.format(num1))
elif num2>num1:
    print('O maior numero eh o numero {}'.format(num2))
else:
    print('Os numeros sao iguais')