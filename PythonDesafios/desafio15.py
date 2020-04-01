'''
Escreva um programa que pergunta a quantidade de km percorridos por um carro alugado e a quantidade de dais pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
'''
km = float(input('Quantos km você andou com o carro? '))
dias = int(input('Quantos dias você ficou com o carro? '))
valor = km*0.15 + dias*60
print('O valor a pagar pelo aluguel do carro é  de R${:.2f}.'.format(valor))
