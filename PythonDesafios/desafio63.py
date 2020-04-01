''' Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia
 de fibonacci. '''
print('Sequência de Fibonacci')
n = int(input('Quantos termos da sequência de Fibonacci vc quer ver? '))
t1 = 0
t2 = 1
print('~'*20)
print('{} -> {}'.format(t1, t2), end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print('-> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('-> FIM!')