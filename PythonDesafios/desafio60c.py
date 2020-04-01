''' Faça um programa que leia um número qualquer e mostre o seu fatorial. Fazer usando loop for!'''
num = int(input('Digite um número para saber seu fatorial: '))
f = 1
print('{}! = '.format(num), end='')
for i in range(num, 0, -1):
    print('{}'.format(i), end='')
    print(' x ' if i > 1 else ' = ', end='')
    f *= i
print('{}'.format(f))
