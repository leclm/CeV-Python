''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai pagar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).'''
soma = 0
quantidade = 0
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    quantidade += 1
    num = int(input('Digite outro número (digite 999 para parar): '))
print('O total de números digitados é {} e a soma entre eles é {}.'.format(quantidade, soma))
