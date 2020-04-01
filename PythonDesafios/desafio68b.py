'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder.
Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
v = 0
while True:
    jogador = int(input('Digite um número: '))
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar [P/I]? ')).strip().upper()[0]
    computador = randint(1, 11)
    soma = computador + jogador
    print(f'Você jogou {jogador} e o PC jogou {computador}. A soma deu {soma}.', end='')
    print(' DEU PAR!' if soma % 2 == 0 else ' DEU ÍMPAR!')
    if tipo == 'P':
        if soma % 2 == 0:
            print('Você venceu! Vamos jogar novamente...\n')
            v += 1
        elif soma % 2 == 1:
            print(f'Você perdeu! Você ganhou {v} vezes.')
            break
    if tipo == 'I':
        if soma % 2 == 0:
            print(f'Você perdeu! Você ganhou {v} vezes.')
            break
        elif soma % 2 == 1:
            print('Você venceu! Vamos jogar novamente...\n')
            v += 1