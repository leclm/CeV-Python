''' Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto. '''
preço = float(input('Qual o preço do produto? R$'))
novo = preço*0.95
print('O valor com desconto para este produto é de R${:.2f}!'.format(novo))
