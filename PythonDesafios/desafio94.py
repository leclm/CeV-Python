''' Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre: a) quantas pessoas foram cadastradas >> b) a média de idade do
grupo >> c) uma lista com todas as mulheres >> d) uma lista com todas as pessoas com idade acima da média. '''
resp = ''
p = {}
ps = []
idades = []
m = []
maiores = []
while resp != 'N':
    p['Nome'] = str(input('Nome: ')).title()
    p['Sexo'] = str(input('Sexo [M/F]: ')).upper()
    while p['Sexo'] not in 'MF':
        p['Sexo'] = str(input('Resposta inválida. Digite novamente. Sexo: ')).upper()[0]
    if p['Sexo'] == 'F':
        m.append(p['Nome'])
    p['Idade'] = int(input('Idade: '))
    idades.append(p['Idade'])
    ps.append(p.copy())
    resp = str(input('Deseja continuar [S/N]? ')).upper().strip()
    while resp not in 'NS':
        resp = str(input('Resposta inválida. Digite novamente. Deseja continuar? ')).upper()[0]
print(f"Foram cadastradas {len(ps)} pessoas.")
media = sum(idades)/len(idades)
print(f"A média das idades cadastradas é {media} anos.")
print(f"A(s) mulher(es) cadastrada(s) é(são) {m}.")
for i in range(0, len(ps)):
    if ps[i]['Idade'] > media:
        maiores.append(ps[i])
print("A lista de pessoas com idade acima da média é:")
for k in maiores:
    print(f"{k}".lstrip('{').rstrip('}'))
