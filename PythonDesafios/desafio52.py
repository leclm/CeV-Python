''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. '''
num = int(input('Digite um número: '))
contador = 0
for i in range(1, num+1):
    if num % i == 0:
        contador += 1
        print('\033[1;34m', end='')
    else:
        print('\033[1;31m', end='')
    print('{}\033[m'.format(i), end=' ')
if contador == 2:
    print('\nO número {} é divisível apenas por 2 números, portanto, ele É PRIMO!'.format(num))
else:
    print('\nO número {} é divisível por {} números, portanto, ele NÃO É PRIMO!'.format(num, contador))
