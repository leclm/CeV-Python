'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da
casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que não pode
exceder 30% do salário ou então o empréstimo será negado.
'''
preço = float(input('Qual o preço da casa? R$ '))
salário = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você quer pagar a casa? '))

pm = preço/(anos*12)

if pm > salário*0.3:
    print('\033[4mInfelizmente\033[m você \033[1;31mnão tem condições\033[m de bancar essa casa amadah.')
else:
    print('\033[1;31mCONGRATS POC!!!\033[m Você tá \033[4;36maprovadah\033[m no empréstimo!!')
print('Nestas condições o valor da parcela será de \033[1;32mR${:.2f}\033[m.'.format(pm))
print('E para que o empréstimo seja aprovado a parcela mensal não pode ultrapassar \033[1;35mR${:.2f}\033[m.'.format(salário*0.3))
