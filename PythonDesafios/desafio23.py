'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
ex: digite um número: 1824 >> unidade: 4 >> dezena: 2 >> centena: 8 >> milhar: 1
'''
num = input('Digite um número de 0 a 9999: ')

print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))

n = int(input('Digite um número entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
