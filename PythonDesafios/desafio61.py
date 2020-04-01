''' Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiro termos da progressão
usando a estrutura while.'''
n = 1
an = 0
termos = []
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
while n < 11:
    an = a1 + (n - 1) * r
    termos.append(an)
    n += 1
print(''.join(str(termos)).strip('[]'))
