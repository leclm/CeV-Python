''' Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O computador deverá escrever na tela se o usuário venceu ou perdeu. '''
from random import randint
from time import sleep
num = randint(0, 5)
chute = int(input('Dê um palpite: '))
print('Pensando...')
sleep(2)
if chute == num:
    print('Você acertou! Parabéns!')
else:
    print('Você errou!')
print('O número escolhido era {}!'.format(num))
