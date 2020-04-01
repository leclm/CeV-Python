'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e CONDIÇÃO DE
PAGAMENTO: à vista dinheiro/cheque: 10% de desconto >> à vista no cartão 5% de desconto >> em até 2x no cartão: preço
normal >> 3x ou mais no cartão: 20% de juros.
'''
print('{:=^40}'.format(' LOJAS CHAGAS '))
preço = float(input('Qual o preço do produto? R$ '))
print('''Escolha a forma de pagamento:
[1] À vista no dinheiro/cheque.
[2] À vista no cartão.
[3] Até 2x no cartão.
[4] 3x ou mais no cartão.''')
cond = int(input('Sua opção: '))
if cond == 1:
    print('Nesta forma de pagamento o produto ganha 10% de desconto! Seu valor fica R$ {:.2f}.'.format(preço*0.9))
elif cond == 2:
    print('Nesta condição o produto tem 5% de desconto! Seu valor ficar R$ {:.2f}.'.format(preço*0.95))
elif cond == 3:
    print('Nesta condição o produto não recebe nenhum desconto. O valor fica R$ {:.2f}.'.format(preço))
elif cond == 4:
    print('Nesta forma de pagamento há acréscimo de 20% de juros. O valor do produto fica R$ {:.2f}.'.format(preço*1.2))
