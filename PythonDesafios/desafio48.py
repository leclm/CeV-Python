''' Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
intervalo de 1 até 500.'''
num = []
for i in range(1, 501):
    if i % 3 == 0 and i % 2 != 0:
        num.append(i)
print('A soma dos {} valores ímpares e múltiplos de 3 no intervalo de 1 até 500 é: {}'.format(len(num), sum(num)))

soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print('A soma de todos os números solicitados é {}.'.format(soma))
