'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. Para salários superiores
a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais o aumento é de 15%.
'''
salary = float(input('Qual seu salário? R$ '))
if salary > 1250:
    print('Seu novo salário com aumento do 10% é R${:.2f}!'.format(salary*1.1))
else:
    print('Seu novo salário com aumento de 15% é R${:.2f}!'.format(salary*1.15))
