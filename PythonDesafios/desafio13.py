''' Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento. '''
salary = float(input('Qual seu salário atual? R$'))
new = salary*1.15
print('Seu novo salário com 15% de aumento é de R${:.2f}!'.format(new))
