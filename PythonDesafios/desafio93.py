''' Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. '''
dados = {
    'Nome': str(input('Nome do jogador: ').title()),
    'Partidas': int(input('Quantas partidas este jogador jogou? '))
            }
Quantidade = []
tot = 0
for i in range(1, dados['Partidas']+1):
    Quantidade.append(int(input(f"Número de gols na partida {i}: ")))
    tot += Quantidade[i-1]
dados['Gols'] = Quantidade
dados['Total'] = tot

print('\033[1;34m=*\033[m'*31)
print(dados)

print('\033[1;34m=*\033[m'*31)
for k, v in dados.items():
    print(f'O campo {k} tem o valor: {v}')

print('\033[1;33m=*\033[m'*31)
print(f"O jogador {dados['Nome']} jogou {dados['Partidas']} partidas.")
for i in range(0, dados['Partidas']):
    print(f"=> Na partida {i+1}, fez {Quantidade[i]} gols.")
print(f"Totalizando {dados['Total']} gols no campeonato.")
