'''Crie um programa que leia a idade e o sexo de várias pessoas, a cada pessoa cadastrada o pc deverá perguntar se o
 usuário quer ou nao continuar adc pessoas. No final mostre: a) quantas pessoas tem mais de 18 anos >> b) quantos
 homens foram cadastrados >> c) quantas mulheres tem menos de 20 anos.'''
print('#'*40)
print('{:^40}'.format('CADASTRAMENTO PESSOAL'))
print('#'*40)
menor = 0
maior = 0
homem = 0
while True:
    print('\nCadastre uma pessoa')
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'F':
        idade = int(input('Idade: '))
        if idade < 20:
            menor += 1
        if idade > 18:
            maior += 1
    if sexo == 'M':
        homem += 1
        idade = int(input('Idade: '))
        if idade > 18:
            maior += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja cadastrar outra pessoa [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'\nNeste cadastro há {maior} pessoas com mais de 18 anos.')
print(f'{homem} homens cadastrados e {menor} mulheres com menos de 20 anos.')
