''' Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores.'''
resp = 0
numeros = []
while resp != 'N':
    num = int(input('Digite um número: '))
    numeros.append(num)
    resp = str(input('Deseja continuar (S OU N)? ')).strip().upper()
    if resp == 'N':
        print('Armazenamento de números finalizado.\n')
print('A média dos números digitados é: {:.1f}'.format(sum(numeros)/len(numeros)))
print('O maior valor digitado é {} e o menor é {}.'.format(max(numeros), min(numeros)))
