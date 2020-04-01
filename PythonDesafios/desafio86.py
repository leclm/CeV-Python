''' Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final mostre a
matriz na tela, com a formatação correta. '''
linha0 = [[], [], []]
linha1 = [[], [], []]
linha2 = [[], [], []]
for l in range(3):
    n = int(input(f'Digite um número para a posição 0x{l}: '))
    linha0[l].append(n)
for l in range(3):
    n = int(input(f'Digite um número para a posição 1x{l}: '))
    linha1[l].append(n)
for l in range(3):
    n = int(input(f'Digite um número para a posição 2x{l}: '))
    linha2[l].append(n)
print(f'{linha0[0]} {linha0[1]} {linha0[2]}')
print(f'{linha1[0]} {linha1[1]} {linha1[2]}')
print(f'{linha2[0]} {linha2[1]} {linha2[2]}')
