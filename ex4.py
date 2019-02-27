letra=str(input('Digite uma letra do alfabeto: '))
letra=letra.upper()
if letra=='A' or letra=='E' or letra=='I' or letra =='O' or letra =='U':
    vogal=True
elif letra!='A' and letra!='E' and letra!='I' and letra !='O' and letra !='U':
    vogal=False

print('Eh vogal? {}'.format(vogal))