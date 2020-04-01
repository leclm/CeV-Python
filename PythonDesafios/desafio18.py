'''
Faça um programa que leia um ângulo qualquer e mostre na tela o sen, cos e tan desse ângulo.
'''
from math import cos, sin, tan, radians

ag = float(input('Digite um ângulo: '))
ar = radians(ag)
cos = cos(radians(ag))
sin = sin(radians(ag))
tan = tan(radians(ag))
print('Dado o ângulo {}°, seu valor em radianos é {:.2f}.'.format(ag, ar), end='')
print(' O cosseno desse ângulo é {:.2f}, o seno é {:.2f} e a tangente é {:.2f}.'.format(cos, sin, tan))
