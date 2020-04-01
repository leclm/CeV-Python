''' Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro ele não será adicionado. No final serão exibidos todos os valores únicos digitados, em ordem crescente.'''
resp = ' '
numeros = []
while resp != 'N':
    n = int(input('Digite um valor: '))
    if n in numeros:
        print('Número duplicado. O armazenamento não foi realizado!')
    if n not in numeros:
        numeros.append(n)
        print('Número armazenado com sucesso!')
    resp = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
    if resp == 'N':
        break
numeros.sort()
print(f'Os números armazenados são: {numeros}')
