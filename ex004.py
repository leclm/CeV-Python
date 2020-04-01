something = input('Digite algo: ')
print('É capitalizado? {}'.format('Sim.' if something.istitle() else 'Não.'))
print('O tipo primitivo desse valor é: {}'.format(type(something)))
print('Só tem espaços? {}'.format('Sim.' if something.isspace() else 'Não.'))
print('É um digito? {}'.format('Sim.' if something.isdigit() else 'Não.')) #
print('É um número? {}'.format('Sim.' if something.isnumeric() else 'Não.')) #
print('É alfanumérico? {}'.format('Sim.' if something.isalnum() else 'Não.'))
print('É alfabético? {}'.format('Sim.' if something.isalpha() else 'Não.'))
print('É maiúsculo? {}'.format('Sim.' if something.isupper() else 'Não.'))
print('É minúsculo? {}'.format('Sim.' if something.islower() else 'Não.'))
