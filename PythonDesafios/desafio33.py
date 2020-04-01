'''
Faça um programa que leia três número e fale com é o maior e qual é o menor.
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
numbers = [n1, n2, n3]
print('O maior número é {} e o menor é {}.'.format(max(numbers), min(numbers)))
