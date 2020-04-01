''' Aprimore o Desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
detalhes de aproveitamento de cada jogador. '''
jogadores = []
jogador = {}
resp = ''
while resp != 'N':
    jogador['Nome'] = str(input('Nome: '))
    jogador['Partidas Jogadas'] = int(input('Quantas partidas este jogador jogou? '))
    gols = []
    jogador['Gols'] = gols
    totgols = 0
    for i in range(1, jogador['Partidas Jogadas'] + 1):
        gols.append(int(input(f"Número de gols na partida {i}: ")))
        totgols += gols[i - 1]
    jogador['Total de gols'] = totgols
    jogadores.append(jogador.copy())
    resp = str(input('Deseja continuar [S/N]? ')).upper()
print('-'*50)
print("Código         Nome          Gols          Total")
print('-'*50)
for i in range(0, len(jogadores)):
    print(f"{i+1:<10} {jogadores[i]['Nome']:^10}    {jogadores[i]['Gols']} {jogadores[i]['Total de gols']:>10}")
print('-'*50)
resposta = ''
while resposta != 'N':
    levant = int(input('Mostrar levantamento de qual jogador? '))
    print(f"LEVANTAMENTO DO JOGADOR {jogadores[levant-1]['Nome']}")
    for i in range(0, len(jogadores[levant-1]['Gols'])):
        print(f"        No jogo {i+1} fez {jogadores[levant-1]['Gols'][i]} gols.")
    print('-' * 50)
    resposta = str(input('Deseja mostrar outro levantamento? ')).upper()
