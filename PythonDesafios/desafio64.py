''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).'''
tot = 0
soma = 0
n = 0
while n != 999:
    n = int(input('Digite um número: '))
    tot += 1
    soma += n
    if n == 999:
        tot -= 1
        soma -= 999
        break
print('O número de valores digitados é {} e a soma destes números é {}.'.format(tot, soma))
