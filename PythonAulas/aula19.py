# EXEMPLO 1
#dados = dict()
dados = {'Nome': 'Pedro', 'Idade': 24}
print(dados['Nome'])  # printa Pedro
print(dados['Idade'])  # printa 24
for item in dados:  # printa nome >> idade
    print(item)
# para adc um elemento append não funciona
dados['Sexo'] = 'M'  # como não tem sexo em dados ele cria o espaço sexo e adc o valor 'M'
del dados['Idade']  # tem que colocar o nome da chave/key (elemento) para poder deletar, se colocar 24 da erro.

filme = {'Título': 'Harry Potter',
         'Ano': 1995,
         'Diretor': 'Francisco'
         }
for k, v in filme.items():
    print(f'O {k} é {v}.')  # Ex.: O Título é Harry Potter

print(filme.keys())  # titulo, ano e diretor
print(filme.items())  # tudo dentro do dicionario, valores e chaves
print(filme.values())  # harry potter, 1995, francisco

# Exemplo 2

pessoas = {'Nome': 'Letícia', 'Idade': 24, 'Emoção': 'Angustia'}
#print(pessoas[0]) >> da erro pq não key chamada 0, as keys sao nome, idade e emoção.
print(pessoas['Nome'])  # printa Letícia, sem colchete/aspas/parenteses/chaves
print(f'A {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
print(pessoas.keys())  # mostra nome, idade e emoção; com (['
print(pessoas.items())  # mostra todo o dicionário na forma de uma lista com tuplas dentro dela
print(pessoas.values())  # mostra leticia, 24, angustia; com (['
for k in pessoas.keys():  # mostra as chaves uma embaixo da outra sem caracteres especiais
    print(k)
for v in pessoas.values():
    print(v)  # mostra os valores um embaixo do outro sem caract especiais
for i in pessoas.items():
    print(i)  # mostra os itens na forma de tupla
#del pessoas['Idade']
pessoas['Nome'] = 'Diana'  # modifica o valor de nome
pessoa['Peso'] = 65  # adc um novo elemento. Não usa append
for k, v in pessoas.items():  # não uso ennumerate em dict, uso o items
    print(f'{k} = {v}')

# EXEMPLO 3: ADC DICT EM UMA LISTA

brasil = []
est1 = {'uf': 'Paraná', 'Sigla': 'PR'}
est2 = {'uf': 'Santa Catarina', 'Sigla': 'SC'}
brasil.append(est1)
brasil.append(est2)
print(brasil[0])
print(brasil[0]['uf'])

# EXEMPLO 4

brasil = []
estado = {}
for i in range(3):
    estado['Unidade Federativa'] = str(input('UF: '))
    estado['Sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())  # precisa copiar se nao vai aparecer 3x a ultima coisa adicionada. [:] só usa em lista

#for k in brasil:  # print os 3 dicts dentro da lista brasil, um embaixo do outro sem []
 #   print(k)

for estado in brasil:
    for ficha in estado.values():
        print(ficha, end=' ')
    print()
