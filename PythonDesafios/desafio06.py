'''Crie um algoritmo que leia um número e mostre seu dobro, seu triplo e sua raíz quadrada.'''
n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de {} é {}, o triplo é {} e a raíz quadrada é {}.'.format(n, d, t, (int(r))))
print('O dobro de {} é {}, o triplo é {} e a raíz quadrada é {:.2f}.'.format(n, n*2, n*3, pow(n, 0.5)))



