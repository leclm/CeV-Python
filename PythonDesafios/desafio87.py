''' Aprimore o desafio anterior, mostrando noo final: a) a soma de todos os valores pares digitados >> b) a soma dos
valores da terceira coluna >> c) o maior valor da segunda linha. '''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}x{c}]: '))
for l in range(0, 3):
    n = matriz[l][2]
    soma3 += n
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}] ', end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
    print()

print(f'A soma dos números pares digitados é {soma}.')
print(f'A soma dos elementos da terceira coluna é {soma3}.')
# somaterceira = matriz[0][2] + matriz[1][2] + matriz[2][2]
# print(f'A soma dos elementos da terceira coluna é {somaterceira}.')

for c in range(0, 3):
    if c == 0:
        m = matriz[1][c]
    elif matriz[1][c] > m:
        m = matriz[1][c]
print(f'O maior valor da segunda linha é {m}.')
