'''
Crie um programa que leia o nome de uma cidade e dia se ela começa ou não com o nome "SÃO".\
'''
city = input('Digite o nome da sua cidade: ')
list = city.lower().split()
print(list)
if list[0] == 'são' or list[0] == 'sao':
    print('O nome da sua cidade começa com "SÃO".')
else:
    print('O nome da sua cidade não começa com "SÃO".')

cidade = str(input('Digite o nome da sua cidade: ')).replace('ã', 'a').lower().strip()
print('sao' in cidade)
print(cidade[0:3] == 'sao')


