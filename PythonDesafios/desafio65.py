''' Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores.'''
resposta = 0
numeros = []
while resposta != 'N':
    num = int(input('Digite um número: '))
    numeros.append(num)
    resposta = str(input('Deseja continuar?\n[S/N]: ')).upper()
print('A média dos números digitados é {:.0f}.'.format(sum(numeros)/len(numeros)))
print('O maior número digitado é {}.'.format(max(numeros)))
print('O menor número digitado é {}.'.format(min(numeros)))
