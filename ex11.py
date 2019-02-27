salMensal=float(input('Digite o seu salario mensal: R$'))

if salMensal< 280:
    percentualAumento=0.2
    reajuste=salMensal*percentualAumento
elif salMensal>=280 and salMensal<700:
    percentualAumento=0.15
    reajuste=salMensal*percentualAumento
elif salMensal>=700 and salMensal<1500:
    percentualAumento=0.1
    reajuste=salMensal*percentualAumento
else:
    percentualAumento=0.05
    reajuste=salMensal*percentualAumento

novoSalario=salMensal+reajuste

print('Salario atual: R${}'.format(salMensal))
print('Percentual de aumento: {}'.format(percentualAumento))
print('Valor do aumento: R${}'.format(reajuste))
print('Novo salario: R${}'.format(novoSalario))