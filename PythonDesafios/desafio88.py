''' Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta. '''
from random import randint
from time import sleep
todos = []
umjogo = []
print('='*40)
print(f"{'JOGO DA MEGA SENA':^40}")
print('='*40)
n = int(input('Qual o número de jogos? '))
for j in range(n):
    for i in range(6):
        palpite = randint(1, 60)
        if palpite not in umjogo:
            umjogo.append(palpite)
    todos.append(umjogo[:])
    umjogo.clear()
print(f'\n=== SORTEANDO {n} SEQUÊNCIAS ===')
todos.sort()
for n, j in enumerate(todos):
    sleep(1)
    print(f'A {n+1}ª sequência é: {j}')
print('='*3, f'{"BOA SORTE!"}', '='*3)
