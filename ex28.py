import sys

valorCompra=0
i=0
precoFile=0
precoAlcatra=0
precoPicanha=0
qtdFile=0
qtdAlcatra=0
qtdPicanha=0
tipoPagamento=str.upper(input('C-Credito D-Debito E-Especie: '))

while i<2:
    tipoCarne=str.upper(input('Digite o tipo de carne: F-File A-Alcatra P-Picanha\n'))
    qtdCarne=float(input('Digite a quantidade de carne em quilogramas:'))
    descontoCartao=0.05

    if tipoCarne=='F':
       if qtdCarne<=5:
            precoFile=4.9*qtdCarne
            qtdFile=qtdCarne
       else:
            precoFile=5.8*qtdCarne
            qtdFile=qtdCarne
    elif tipoCarne=='A':
        if qtdCarne<=5:
            precoAlcatra=5.9*qtdCarne
            qtdAlcatra=qtdCarne
        else:
            precoAlcatra=6.8*qtdCarne
            qtdAlcatra=qtdCarne
    elif tipoCarne=='P':
        if qtdCarne<=5:
            precoPicanha=6.9*qtdCarne
            qtdPicanha=qtdCarne
        else:
            precoPicanha=7.8*qtdCarne
            qtdPicanha=qtdCarne
    else:
        print('Tipo invalido.')
        sys.exit()

    precoCarne=precoPicanha+ precoAlcatra+precoFile

    if tipoPagamento=='C':
        precoFinalCarne=precoCarne-(precoCarne*descontoCartao)
    elif tipoPagamento=='D' or tipoPagamento=='E':
        precoFinalCarne=precoCarne
    else:
        print('Tipo de pagamento invalido')
        sys.exit()

    valorCompra=precoFinalCarne+valorCompra
    print('Valor parcial da compra: R${0:.2f}'.format(valorCompra))
    i=i+1

print('Valor final da compra: R${0:.2f}'.format(valorCompra))
print('{0:.2f}kg Alcatra: R${1:.2f}'.format(qtdAlcatra, precoAlcatra))
print('{0:.2f}kg File: R${1:.2f}'.format(qtdFile, precoFile))
print('{0:.2f}kg Picanha: R${1:.2f}'.format(qtdPicanha, precoPicanha))