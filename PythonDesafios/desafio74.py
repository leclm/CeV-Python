''' Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso mostre a listagem de
números gerados e tbm indique o maior e o menor valor que estão na tupla.'''
'''randrange(2, 9, 3) >> retorna um numero aleatorio no intervalo dado; 9 nao incluso; põe step se quiser
randint(2, 9) >> retorna um numero aleatorio no intervalo dado; 9 incluso; nao põe step
random >> retorna um numero aleatório entre 0 e 1'''
# FORMA 1
from random import randint
listnumeros = []
for i in range(5):
    n = randint(0, 100)
    listnumeros.append(n)
numero = tuple(listnumeros)
print(f'Os números gerados são: {numero}'.replace('(', '').replace(')', '').replace(',', ' -'))
print(f'O maior valor da tupla é: {max(numero)}')
print(f'O menor valor da tupla é: {min(numero)}')
# FORMA 2
from random import randint
a = ()
for i in range(5):
    n = (randint(0, 100),)  # precisa por , se for só um item na tupla, se nao o type é int e nao tuple
    a += n
print(f'Os números gerados são: {a}'.replace('(', '').replace(')', '').replace(',', ' -'))
print(f'O maior valor da tupla é: {max(a)}')
print(f'O menor valor da tupla é: {min(a)}')
# FORMA 3
from random import randint
a = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Os números gerados são: {a}'.replace('(', '').replace(')', '').replace(',', ' -'))
print(f'O maior valor da tupla é: {max(a)}')
print(f'O menor valor da tupla é: {min(a)}')