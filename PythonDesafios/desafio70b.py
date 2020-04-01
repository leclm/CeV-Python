''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final mostre: a) Qual é o total gasto na compra >> b) Quantos produtos custam mais de 1000 reais >> c) Qual o nome
do produto mais barato. '''
print('* * * Lojão Das Da * * *\n')
tot = cont = totmil = menorpreço = maisbarato = 0
while True:
    prod = str(input('Produto: '))
    preço = float(input('Preço: R$ '))
    tot += preço
    cont += 1
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menorpreço:
        menorpreço = preço
        maisbarato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar outro produto [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'\nO total gasto na compra é R${tot:.2f}!')
print(f'Temos {totmil} produtos que custam mais de R$1000.00!')
print(f'O item mais barato é "{maisbarato}" e custa R${menorpreço:.2f}!')
