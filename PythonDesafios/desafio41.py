'''
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua
categoria, de acordo com a idade: até 9 = mirim > ate 14 = infantil > ate 19 = junior > ate 20 = senior > acima = master
'''
from datetime import date
ano = int(input('Em que ano você nasceu? '))
year = date.today().year
idade = year - ano
if idade <= 9:
    print('Sua categoria é \033[4;32mmirim\033[m!')
elif idade <= 14:
    print('Sua categoria é \033[4;33minfantil\033[m!')
elif idade <= 19:
    print('Sua categoria é \033[4;36mjúnior\033[m!')
elif idade == 20:
    print('Sua categoria é \033[4;34msênior\033[m!')
else:
    print('Sua categoria é \033[4;35mmaster\033[m!')
