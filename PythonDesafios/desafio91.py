''' Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses números em um
dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. '''
from random import randint
from time import sleep
from operator import itemgetter
num = {'Jogador 1': '', 'Jogador 2': '', 'Jogador 3': '', 'Jogador 4': ''}
for i in range(1, 5):
    j = randint(1, 6)
    num[f'Jogador {i}'] = j
print(f'{"=-"*5:<10}', f'{"Valores sorteados":^10}', f'{"=-"*5:>10}')
for k, v in num.items():
    print(f'        O {k} tirou: {v}')
    sleep(0.5)
print(f'{"=-"*5:<10}', f'{"Ranking dos Jogadores":^10}', f'{"=-"*5:>10}')
ranking = dict()
ranking = sorted(num.items(), key=itemgetter(1), reverse=True)  # vai sair como list, mesmo que eu diga que é dict
for k, v in enumerate(ranking):
    print(f'    {k+1}° lugar: {v[0]} com {v[1]} pontos.')
    sleep(0.5)
