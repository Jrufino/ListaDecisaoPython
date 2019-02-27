import sys

ladoUm=float(input('Digite o primeiro lado do triangulo: '))
ladoDois=float(input('Digite o segundo lado do triangulo: '))
ladoTres=float(input('Digite o terceiro lado do triangulo: '))

if (ladoUm+ladoDois)>ladoTres and (ladoUm+ladoTres)>ladoDois and (ladoDois+ladoTres)>ladoUm:
    triangulo=True
else:
    triangulo=False
    print("Nao eh um triangulo")
    sys.exit()

if ladoUm==ladoDois==ladoTres:
    trianguloEquilatero=True
    print("Triangulo Equilatero")
    sys.exit()
else:
    trianguloEquilatero=False

if ladoUm==ladoDois or ladoUm==ladoDois or ladoDois==ladoTres:
    trianguloIsosceles=True
    print("Triangulo Isosceles")
    sys.exit()
else:
    trianguloIsosceles=False

if ladoUm!=ladoDois and ladoUm!=ladoTres and ladoDois!=ladoTres:
    trianguloEscaleno=True
    print("Triangulo Escaleno")
    sys.exit()
else:
    trianguloEscaleno=False