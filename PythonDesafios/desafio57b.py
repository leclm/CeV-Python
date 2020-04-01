''' Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto.'''

sex = str(input('Digite seu sexo M/F: '))
while sex != 'M' or sex != 'F':
    sex = str(input('Resposta inválida. Digite novamente seu sexo [M/F]: ')).upper().strip()
    if sex == 'M' or sex == 'F':
        print('Dado armazenado.')
        break


sex = str(input('Digite seu sexo M/F: ')).strip().upper()
while sex not in 'MF':
    sex = str(input('Digite seu sexo: ')).strip().upper()
if sex == 'M' or sex == 'F':
    print('Dado armazenado.')
