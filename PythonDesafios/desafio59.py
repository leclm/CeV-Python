''' Crie um programa que leia dois valores e mostre um menu na tela: [1 soma >> [2 multiplicar >> [3 maior >> [4 novos
números >> [5 sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.'''
from functools import reduce
from operator import mul
from time import sleep
print('*-'*20)
print('\033[1;36mOperações Matemáticas\033[m'.center(45))
print('*-'*20)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
numeros = [n1, n2]
print('Escolha uma das operações abaixo:')
print('[1] Somar\n'
      '[2] Multiplicar\n'
      '[3] Maior número\n'
      '[4] Adicionar números\n'
      '[5] Resetar números\n'
      '[6] Sair do programa\n')
esc = 0
while esc != 6:
    esc = int(input('Sua escolha: '))
    if esc == 1:
        print('A soma entre os valores digitados é: {}.\n'.format(sum(numeros)))
    elif esc == 2:
        produto = reduce(mul, numeros, 1)
        print('A multiplicação entre os valores digitados é: {}.\n'.format(str(produto)))
    elif esc == 3:
        print('O maior número entre os valores digitados é: {}.\n'.format(max(numeros)))
    elif esc == 4:
        num = int(input('Digite outro valor: \n'))
        numeros.append(num)
    elif esc == 5:
        numeros.clear()
        n1 = int(input('Digite um novo valor: \n'))
        n2 = int(input('Digite um segundo novo valor: \n'))
        numeros.append(n1)
        numeros.append(n2)
    elif esc == 6:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida, tente novamente!')
print('Você saiu do programa!')
