prod1=float(input('Digite o preco do primeiro produto: R$'))
prod2=float(input('Digite o preco do segundo produto: R$'))
prod3=float(input('Digite o preco do terceiro produto: R$'))

if prod1<prod2 and prod1<prod3:
    menorPreco=prod1
elif prod2<1 and prod2<prod3:
    menorPreco=prod2
else:
    menorPreco=prod3

print('O produto mais barato custa R${0:.2f}'.format(menorPreco))