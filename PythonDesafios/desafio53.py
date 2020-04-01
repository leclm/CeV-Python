''' Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. '''
print('\033[1;33m!¡'*20)
print('\033[1;33m!¡                                    !¡\033[m')
print('\033[1;33m!¡         \033[1;34mTeste do Palíndromo\033[m        \033[1;33m!¡\033[m'.center(40))
print('\033[1;33m!¡                                    !¡\033[m')
print('\033[1;33m!¡\033[m'*20)
print('\n')
# OPÇÃO 1
txt = str(input('Digite uma frase: ')).strip().upper()
txt1 = txt.replace(' ', '')
txt2 = txt1[::-1]

if txt1 == txt2:
    print('Esta frase é um \033[4;34mpalíndromo\033[m!!')
else:
    print('Esta frase \033[4;31mnão é\033[m um palíndromo :(')
# OPÇÃO 2
txt = str(input('Digite uma frase: ')).strip().upper()
palavras = txt.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('É PALINDROMO')
else:
    print('Não é palíndromo.')