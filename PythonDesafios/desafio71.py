''' Crie um programa que simule o funcionamento de um caixa eletrônico. No início pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. obs: considere
 que o caixa eletronico possui cédulas de 50, 20, 10 e 1.'''
print('='*40)
print('Caixa Eletrônico'.center(35))
print('='*40)
valor = int(input('Qual o valor que deseja sacar? R$ '))
cinq = valor // 50
valor -= cinq * 50
vinte = valor // 20
valor -= vinte * 20
dez = valor // 10
valor -= dez * 10
um = valor // 1
valor -= um * 1
print(f'O total de notas de R$50 é {cinq}')
print(f'O total de notas de R$20 é {vinte}')
print(f'O total de notas de R$10 é {dez}')
print(f'O total de notas de R$1 é {um}')
print('='*40)
print('Volte sempre ao Caixa Eletrônico mais confiável do Brasil!')
