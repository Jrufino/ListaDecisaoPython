data=str(input('Insira uma data no formato: ddmmaaaa\n'))
dia=int(data[0:2])
mes=int(data[2:4])
ano=int(data[4:8])

if dia<1 or dia>31:
    print("Dia invalido")
elif mes<1 or mes>12:
    print("Mes invalido")
elif ano<-9999 or ano>9999:
    print("Mes invalido")
else:
    print('Data valida:{}/{}/{}'.format(dia,mes,ano))