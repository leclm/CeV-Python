''' Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiro termos da progressão
usando a estrutura while. FAZENDO SEM USAR A EQ DO TERMO GERAL'''
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 0
while c < 10:
    print(a1, end=' -> ')
    a1 += r
    c += 1
print('Fim!')
