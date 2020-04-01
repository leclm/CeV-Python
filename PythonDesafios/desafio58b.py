''' Melhore o jogo do desafio28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
tentar chutar até acertar, mostrando no final quantos palpites foram necessários para vencer. '''
from random import randint
print('*-'*20)
print('\033[1;36mTeste da Adivinhação\033[m'.center(45))
print('*-'*20)
print('Estou pensando em um número de 0 a 10. Vamos ver se vc acerta?\n')
computador = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... Tente novamente')
        elif jogador < computador:
            print('Mais... Tente novamente')
print('Você acertou com {} tentativas. Parabéns!'.format(palpites))
