''' Melhore o jogo do desafio28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
tentar chutar até acertar, mostrando no final quantos palpites foram necessários para vencer. '''
print('\033[1;34m=-\033[m'*22)
print('\033[1;35mJogo da Adivinhação!\033[m'.center(50))
print('\033[1;34m=-\033[m'*22)
print('Oi, sou seu computador!\nEstou pensando em um número de 0 a 10. Será que você consegue acertar?')
from random import randint
computador = randint(0, 10)
#print(computador)
palpite = int(input('Qual o seu palpite? '))
tentativas = 1
while palpite != computador:
    if palpite > computador:
        print('Seu palpite é muito alto!')
        palpite = int(input('\033[1;31mQual seu novo palpite?\033[m '))
        tentativas += 1
    elif palpite < computador:
        print('Seu palpite é muito baixo!')
        palpite = int(input('\033[1;31mQual seu novo palpite?\033[m '))
        tentativas += 1
else:
    print('\033[1;33mVocê acertou em {} tentativas! Parabéns!\033[m'.format(tentativas))
