''' Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
mostre uma listagem de preços, organizando os dados de forma tabular. '''
listagem = ('Caderno', 8.99, 'Lapiseira', 15.49, 'Borracha', 2.99, 'Calculadora', 49.90, 'Mochila', 123.89, 'Corretivo',
            5.99, 'Jaqueta corta vento', 239.90)
print('='*40)
print(f'{"Tabela de Preços":^40}')
print('='*40)
for item in listagem:
    if listagem.index(item) % 2 == 0:
        print(f'{item:.<30}', end='')
    else:
        print(f'R${item:>7.2f}')
print('='*40)
