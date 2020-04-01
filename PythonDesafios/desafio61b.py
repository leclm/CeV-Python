''' Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiro termos da progressão
usando a estrutura while. FAZENDO SEM USAR A EQ DO TERMO GERAL'''
primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
termo = primeirotermo
while cont < 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim!')
