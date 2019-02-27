valorHora=float(input('Insira o valor da sua hora: R$'))
horasTrabalhadas=int(input('Insira as suas horas trabalhadas: '))

salarioBruto= valorHora*horasTrabalhadas

if salarioBruto<=900:
    impostoRenda=0 
elif salarioBruto>900 and salarioBruto<=1500:
    impostoRenda=0.05
elif salarioBruto>1500 and salarioBruto<=2500:
    impostoRenda=0.10
else:
    impostoRenda=0.2

descontoImpostoRenda=salarioBruto*impostoRenda
inss=salarioBruto*0.1
fgts=salarioBruto*0.11
sindicato=salarioBruto*0.03
totalDescontos=impostoRenda+inss+sindicato
salarioLiquido=salarioBruto-totalDescontos

impostoRenda=impostoRenda*100

print('Salario Bruto: ({0:.2f}*{1:.2f})  \t\t: R${2:.2f}'.format(horasTrabalhadas,valorHora,salarioBruto))
print('(-)IR({0:.2f}%)                  \t\t: R${1:.2f}'.format(impostoRenda,descontoImpostoRenda))
print('(-)INSS(10%)                     \t: R${0:.2f}'.format(inss))
print('FGTS (11%)                       \t: R${0:.2f}'.format(fgts))
print('Desconto sindical:               \t: R${0:.2f}'.format(sindicato))
print('Total de descontos:              \t: R${0:.2f}'.format(totalDescontos))
print('Salario Liquido                  \t: R${0:.2f}'.format(salarioLiquido))