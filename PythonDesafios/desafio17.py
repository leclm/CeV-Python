'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimento da hipotenusa.
'''
import math
ca = float(input('Qual o comprimento do ca? '))
co = float(input('Qual o comprimento do co? '))
h = math.hypot(ca, co)
# h = math.sqrt(pow(ca, 2) + pow(co, 2))
print('O comprimento da hipotenusa é {:.2f}.'.format(h))
