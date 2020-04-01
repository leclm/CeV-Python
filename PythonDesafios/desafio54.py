'''
Crie um programa que leia o ano de nascimento de 7 pessoas. No final mostre quantas pessoas ainda não atingiram a
maioridade e quantas já.
'''
from datetime import date
menor = []
maior = []
anoatual = date.today().year
for i in range(0, 7):
    anonasc = int(input('Qual o ano de nascimento da {}° pessoa? '.format(i+1)))
    idade = anoatual - anonasc
    if idade < 18:
        menor.append(idade)
    else:
        maior.append(idade)
print('Neste grupo há {} pessoas menores de idade e {} maiores de idade..'.format(len(menor), len(maior)))

# OPÇÃO 2
from datetime import date
anoatual = date.today().year
minor = 0
major = 0
for i in range(0, 7):
    anonasc = int(input('Qual o ano de nascimento da {}° pessoa? '.format(i+1)))
    idade = anoatual - anonasc
    if idade < 18:
        minor += 1
    else:
        major += 1
print('Neste grupo há {} pessoas menores de idade e {} maiores de idade..'.format(minor, major))
