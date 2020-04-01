'''
Faça um programa que leia uma frase pelo teclado e mostre: a) quantas vezes aparece a letra A; b) Em que posição ela
aparece a primeira vez e c) em que posição ela aparece a última vez.
'''
frase = str(input('Digite uma frase: ')).strip().lower().replace(' ', '')
print('A letra "a" aparece {} vezes nesta frase.'.format(frase.count('a')))
print('A letra "a" aparece pela primeira vez na posição {}.'.format(frase.find('a')+1))
print('A letra "a" aparece pela última vez na posição {}.'.format(frase.rfind('a')+1))
