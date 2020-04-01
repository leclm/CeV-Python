'''Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.'''
import math
num = float(input('Digite um número: '))
print('A parte inteira do número real {} é {}.'.format(num, int(num)))
print('A parte inteira no número real {} é {}.'.format(num, math.fabs(num))) #return the absolute value (without signal)
print('A parte inteira do número real {} é {}.'.format(num, math.trunc(num))) #return the num as a integer
