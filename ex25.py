print('Responda S ou N')
resposta=str.upper(input('Telefonou para a vitima?'))
if resposta=='S':
    pontuacao=1
else:
     pontuacao=0
pontuacaoFinal= pontuacao

resposta=str.upper(input('Esteve no local do crime?'))
if resposta=='S':
    pontuacao=1
else:
    pontuacao=0
pontuacaoFinal= pontuacaoFinal+pontuacao

resposta=str.upper(input('Mora perto da vitima?'))
if resposta=='S':
    pontuacao=1
else:
    pontuacao=0
pontuacaoFinal= pontuacaoFinal+pontuacao

resposta=str.upper(input('Devia para a vitima?'))
if resposta=='S':
    pontuacao=1
else:
    pontuacao=0
pontuacaoFinal= pontuacaoFinal+pontuacao

resposta=str.upper(input('Devia para a vitima?'))
if resposta=='S':
    pontuacao=1
else:
    pontuacao=0
pontuacaoFinal= pontuacaoFinal+pontuacao

if pontuacaoFinal==5:
    print('Classificado como Assassino!')
elif pontuacaoFinal==3 or pontuacaoFinal==4:
    print('Classificado como Cumplice')
elif pontuacaoFinal==1 or pontuacaoFinal==2:
    print('Classificado como Suspeito')
else: 
    print('Classificado como Inocente')