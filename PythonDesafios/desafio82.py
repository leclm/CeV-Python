''' Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
contar apenas os valores pares e os valores ímpares digitados. Ao final, mostre o conteúdo das três listas geradas.'''
num = []
p = []
i = []
resp = ' '
while resp != 'N':
    n = int(input('Digite um valor: '))
    num.append(n)
    resp = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
    if resp == 'N':
        print('\nPrograma finalizado!\n')
        break
for n in num:
    if n % 2 == 0:
        p.append(n)
    if n % 2 == 1:
        i.append(n)
print(f'Os valores digitados foram: {num}')
print(f'Os valores pares são: {p}')
print(f'Os valores ímpares são: {i}')
