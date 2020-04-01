'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior >> o segundo valor é maior >> não existe valor maior, os dois são iguais.
'''
print('=*=*'*20)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('=*='*20)

if n1 > n2:
    print('O \033[1;32mprimeiro\033[m valor é maior!')
elif n2 > n1:
    print('O \033[1;34msegundo\033[m valor é maior!')
else:
    print('\033[4;35mNão existe\033[m valor maior, os dois são iguais.')
