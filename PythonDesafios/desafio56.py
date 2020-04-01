''' Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do prog mostre: a média de idade do
grupo >> qual o nome do HOMEM mais velho >> quantas mulheres têm menos de 20 anos. '''
idade_f_menor = []
idades = []
imasc = []
nmasc = []
for i in range(0, 4):
    sexo = str(input('Qual o sexo da pessoa {}? (Digite F ou M) '.format(i+1))).lower()
    if sexo == 'f':
        nome = str(input('Qual o nome da pessoa {}? '.format(i + 1)))
        idade = int(input('Qual a idade da pessoa {}? '.format(i + 1)))
        idades.append(idade)
        if idade < 20:
            idade_f_menor.append(idade)
    if sexo == 'm':
        nome = str(input('Qual o nome da pessoa {}? '.format(i + 1)))
        nmasc.append(nome)
        idade = int(input('Qual a idade da pessoa {}? '.format(i + 1)))
        imasc.append(idade)
        idades.append(idade)
maior_idade_masc = max(imasc)
index_mim = imasc.index(maior_idade_masc)
index_nome = nmasc[index_mim]
print('A média das idades é {} anos.'.format(int(sum(idades)/len(idades))))
print('O nome do homem mais velho é {}!'.format(index_nome.title()))
print('O número de mulheres com menos de 20 anos é {}.'.format(len(idade_f_menor)))
