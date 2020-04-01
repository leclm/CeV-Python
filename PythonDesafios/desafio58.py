''' Melhore o jogo do desafio28 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
tentar chutar até acertar, mostrando no final quantos palpites foram necessários para vencer. '''
from random import randint
print('*-'*20)
print('\033[1;36mTeste da Adivinhação\033[m'.center(45))
print('*-'*20)
print('Estou pensando em um número de 0 a 10. Vamos ver se vc acerta?\n')
computador = randint(0, 11)
palpite = 0
tentativas = 0
while palpite != computador and tentativas == 0:
    palpite = int(input('Qual o seu palpite? '))  # neste momento palpite recebe o valor que eu digitei
    tentativas += 1  # neste momento tentativa deixa de ser 0 e passa a ser 1, acrescento uma unidade em tantativas
    while palpite != computador and tentativas > 0:
        palpite = int(input('Você errou! Tente novamente: '))  # palpite deixa de ter o valor anterior e passa a ter o que eu digitar agora
        tentativas += 1  # tentativa recebe mais uma unidade e passa a ser 2
        if palpite == computador:
            print('Você acertou!')
print('O número que eu pensei foi {}! Você precisou de {} tentativas para acertar!'.format(computador, tentativas))
