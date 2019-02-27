turno=str(input('Digite o seu turno de estudo:\
    M-Matutino\
    V-Vespertino\
    N-Noturno\n'))
turno=turno.upper()

if turno=='M':
    print('Bom dia!')
elif turno=='V':
    print('Boa tarde!')
elif turno=='N':
    print('Boa noite')
else:
    print('Digite um turno valido!')