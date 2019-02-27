ano=int(input('Digite o ano:'))

if ano%400==0:
    print('Ano bissexto')
elif ano%100==0 and ano%400!=0:
    print('Nao eh ano bissexto')
elif ano%4==0:
    print('Ano bissexto')
else:
    print('Nao eh ano bissexto')