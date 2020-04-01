''' Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import choice
from time import sleep

print('{:=^40}'.format(' JOKENPÔ '))
list = ['pedra', 'papel', 'tesoura']
pc = choice(list)
user = str(input('Qual sua jogada? (digite pedra, papel ou tesoura)\n')).lower()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('!!!')
sleep(1)

if pc == user:
    print('\033[1;33mEmpate!\033[m O PC escolheu {}!'.format(pc.capitalize()))
elif (pc == 'pedra' and user == 'tesoura') or (pc == 'papel' and user == 'pedra') or (pc == 'tesoura' and user == 'papel'):
    print('Você \033[1;31mperdeu\033[m! o PC escolheu {}!'.format(pc.capitalize()))
elif (pc == 'pedra' and user == 'papel') or (pc == 'papel' and user == 'tesoura') or (pc == 'tesoura' and user == 'pedra'):
    print('Você \033[1;34mvenceu\033[m! O PC escolheu {}!'.format(pc.capitalize()))
else:
    print('Digite uma das três palavras que eu te disse sua cadela')
