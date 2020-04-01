''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final mostre: a) Qual é o total gasto na compra >> b) Quantos produtos custam mais de 1000 reais >> c) Qual o nome
do produto mais barato. '''
print('* * * Lojão Das Da * * *\n')
mais = 0
total = 0
produtos = []
valores = []
while True:
    resp = str(input('Deseja adicionar um produto [S/N]? ')).strip().upper()
    while resp != 'N' and resp != 'S':
        resp = str(input('Deseja adicionar um produto [S/N]? ')).strip().upper()
    if resp == 'S':
        prod = str(input('Produto: '))
        produtos.append(prod)
        valor = float(input('Preço: R$ '))
        valores.append(valor)
        total += valor
        if valor > 1000:
            mais += 1
        #resp = str(input('Deseja adicionar um produto [S/N]? ')).strip().upper()
    if resp == 'N':
        break
precoMaisCaro = max(valores)
posicaoPrecoMaisCaro = valores.index(precoMaisCaro)
nomeprod = produtos[posicaoPrecoMaisCaro]
print(f'O total gasto na compra é de R${total:.2f}, sendo que {mais} produto(s) custa(m) mais de R$1000.00!')
print(f'O item "{nomeprod}" é o mais caro da compra, seu custo é de R${precoMaisCaro:.2f}!')
