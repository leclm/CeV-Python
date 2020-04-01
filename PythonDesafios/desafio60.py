''' Faça um programa que leia um número qualquer e mostre o seu fatorial. '''
from math import factorial
numeros = []
tot = num = int(input('Digite um número: '))
print('{}!='.format(num), end='')
while num > 1:
    numeros.append((num+1)-1)
    num -= 1
print(''.join(str(numeros)).strip('[]').replace(',', 'x').replace(' ', ''), end='')
print('={}'.format(factorial(tot)))
