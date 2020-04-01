'''
Crie um programa que leia um número inteiro e mostre na tela se ela é par ou ímpar.
'''
num = (input('Digite um número: '))  # str
n = num[-1]  # str
par = [0, 2, 4, 6, 8]  # par é tipo list e os números dentro são int
if int(n) in par:  # tem que ser int pra procurar dentro da lista pois os num dentro da list são int
    print('Este número é par.')
else:
    print('Este número é ímpar.')

####

número = int(input('Digite um número: '))
resultado = número % 2
if resultado == 0:
    print('O número {}{}{} é um número {}par{}!'.format('\033[1;33m', número, '\033[m', '\033[4;35m', '\033[m'))
else:
    print('O número {} é um número {}ímpar{}!'.format(número, '\033[7;36;40m', '\033[m'))
