''' Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. obs: considere
 que o caixa eletronico possui cédulas de 50, 20, 10 e 1.'''
print('='*40)
print('{:^40}'.format('Caixa Eletrônico'))
print('='*40)
valor = int(input('Qual valor você deseja sacar? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'O total de cédulas de R${céd} é {totcéd}.')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('='*40)
print('Obrigado por usar o Banco Letícia Lindícaa!')
