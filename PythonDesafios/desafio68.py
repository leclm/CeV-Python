'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder.
Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
print('\033[1;36m=-\033[m'*20)
print('\033[1;33mJOGO DO PAR OU ÍMPAR\033[m'.center(45))
print('\033[1;36m=-\033[m'*20)
cont = 0
while True:
    comp = randint(0, 10)
    n = int(input('Jogue um número: '))
    op = str(input('Par ou ímpar [P/I]? ')).upper().strip()
    soma = n + comp
    print(f'\nVocê jogou {n} e o computador jogou {comp}. Total de {soma}!')
    if op == 'P':
        if soma % 2 == 0:
            print('Deu par! Você venceu!\nVamos jogar novamente...\n')
            print('~' * 40)
            cont += 1
        else:
            print(f'Deu ímpar! GAME OVER!\nVocê venceu {cont} vezes.')
            print('~' * 40)
            break
    if op == 'I':
        if soma % 2 != 0:
            print('Deu ímpar! Você venceu!\nVamos jogar novamente...\n')
            print('~' * 40)
            cont += 1
        else:
            print(f'Deu par! GAME OVER!\nVocê venceu {cont} vezes.')
            print('~' * 40)
            break
