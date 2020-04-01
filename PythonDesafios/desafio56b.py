''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do prog mostre: a média de idade do
grupo >> qual o nome do HOMEM mais velho >> quantas mulheres têm menos de 20 anos. '''
somaidades = 0
maisvelho = 0
nomemaisvelho = 0
totm = 0
for i in range(0, 4):
    print('\033[1;35m===== PESSOA {} ======\033[m'.format(i+1))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    somaidades += idade
    sexo = str(input('Sexo [M/F]: ')).lower()
    if i == 0 and sexo == 'm':
        maisvelho = idade
        nomemaisvelho = nome
    if idade > maisvelho and sexo == 'm':
        maisvelho = idade
        nomemaisvelho = nome
    if sexo == 'f' and idade < 20:
        totm += 1
print(somaidades)
print(totm)
média = somaidades / 4
print('A média das idades deste grupo é {} anos.'.format(média))
print('O nome do homem mais velho é {}.'.format(nomemaisvelho))
print('O número de mulher com menos de 20 anos é {}.'.format(totm))
