''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto.'''
sex = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sex not in 'MF':
    sex = str(input('Dado inválido. Digite novamente: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(sex))
