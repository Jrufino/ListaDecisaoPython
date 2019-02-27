import sys

tipoCombustivel=str.upper(input('Insira o tipo: A-Alcool G- Gasolina\n'))
litrosVendidos=float(input('Litros vendidos: \n'))

if tipoCombustivel=='A':
    if litrosVendidos<=20:
        desconto=0.03
    else:
        desconto=0.05
elif  tipoCombustivel=='G':
    if litrosVendidos<=20:
        desconto=0.04
    else:
        desconto=0.06
else:
    print('Tipo de combustivel invalido')
    sys.exit()

precoGasolina=2.5
precoAlcool=1.9

if tipoCombustivel=='A':
    valorAbastecimento=(precoAlcool*litrosVendidos)
    abastecimentoDescontado=valorAbastecimento-(valorAbastecimento*desconto)
else:
    valorAbastecimento=(precoGasolina*litrosVendidos)
    abastecimentoDescontado=valorAbastecimento-(valorAbastecimento*desconto)

print('Valor do abastecimento: R${0:.2f}'.format(valorAbastecimento))
print('Valor com desconto: R${0:.2f}'.format(abastecimentoDescontado))