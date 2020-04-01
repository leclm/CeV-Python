'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: a) quantas
pessoas foram cadastradas >> b) Uma listagem com as pessoas mais pesadas >> c) Uma listagem com as pessoas mais leves.'''
pessoa = []
peso = []
galera = []
resp = 0
while resp != 'N':
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    galera.append(pessoa[:])
    pessoa.clear()
    resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    while resp not in 'NS':
        resp = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break

for i in range(0, len(galera)):
    peso.append(galera[i][1])

print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'\nO maior peso é {max(peso):.3f} kg. Peso correspondente a: ', end='')
for i in range(0, len(galera)):
    if galera[i][1] == max(peso):
        print(galera[i][0], end=', ')

print(f'\nO menor peso é {min(peso):.3f} kg. Peso correspondente a: ', end='')
for i in range(0, len(galera)):
    if galera[i][1] == min(peso):
        print(galera[i][0], end=', ')

# toda vez que o peso de uma pessoa em galera for igual ao max eu quero que printe o nome dessa pessoa