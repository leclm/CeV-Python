''' Arredondar pra cima, para baixo, fazer raiz, import math, ver os modulos de math
importar só a função que eu quero, sqtr, floor...
'''
# import math (importa todo o módulo math)
from math import sqrt, floor, ceil #(importa só os métodos que eu quero)
num = int(input('Digite um número: '))
raíz = sqrt(num)
#print('A raíz quadrada do número {} é {}.'.format(num, math.floor(raíz)))
print('A raíz quadrada do número {} é\nArredondado para cima = {}'.format(num, ceil(raíz)))
print('Arredondado para baixo = {}\nSem arredondar {}\nCom duas casas decimais {:.2f}'.format(floor(raíz), raíz, raíz))
