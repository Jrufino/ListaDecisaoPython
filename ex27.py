qtdKilosMorango=float(input('Digite a quantidade em quilos de morangos:'))
qtdKilosMacas=float(input('Digite a quantidade em quilos de macas:'))   

if qtdKilosMorango<=5:
    precoMorango=2.5*qtdKilosMorango
else:
    precoMorango=2.2*qtdKilosMorango

if qtdKilosMacas<=5:
    precoMacas=1.8*qtdKilosMacas
else:
    precoMacas=1.5*qtdKilosMacas

valorVenda=precoMacas+precoMorango

if valorVenda>25:
    valorFinal=valorVenda-(valorVenda*0.10)
else:
    valorFinal=valorVenda

print('Valor da venda: R${0:.2f}'.format(valorVenda))
print('Valor a ser pago pelo cliente: R${0:.2f}'.format(valorFinal))