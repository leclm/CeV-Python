''' Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
informações possíveis sobre ele '''

something = input('Digite algo: ')
print('É composto por números e letras? {}'.format('Sim.' if something.isalnum() else 'Não.'))
print('Todos os caracteres podem ser impressos? {}'.format('Sim' if something.isprintable() else 'Não.'))
