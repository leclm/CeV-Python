''' Crie um tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de
colocação. Depois mostre: a) Apenas os 5 primeiros colocados >> b) Os últimos 4 colocados da tabela >> c) uma lista com
os times em ordem alfabética >> d) Em que posição da tabela está o time da Chapecoense.'''
coloc = ('Flamengo', 'Santos', 'Corinthians', 'São Paulo', 'Palmeiras', 'Internacional', 'Atlético', 'Bahia',
        'Atlético-PR', 'Botafogo', 'Grêmio', 'Fortaleza', 'Goiás', 'Ceará SC', 'Vasco da Gama', 'Cruzeiro',
        'Chapecoense', 'Fluminense', 'CSA', 'Avaí')
print(f'Os cinco primeiros colocados são: {coloc[0:5]}'.replace('(', '').rstrip(')').replace("'", ""))  # 5 não incluso
print(f'Os últimos quatros colocados são: {coloc[-4:]}'.replace('(', '').rstrip(')').replace("'", ""))
print(f'Os times em ordem alfabética são: {sorted(coloc)}'.replace('[', '').rstrip(']').replace("'", ""))
print(f"A Chapecoense está na {coloc.index('Chapecoense') + 1}ª colacação.")
