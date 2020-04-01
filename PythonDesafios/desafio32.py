'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
from datetime import date
ano = int(input('Digite um ano (se quiser o ano atual digite 0): '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é \033[1;35mbissexto\033[m!'.format(ano))
else:
    print('O ano {} não é \033[4mbissexto\033[m!'.format(ano))
