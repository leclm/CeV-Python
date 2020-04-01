''' Posicionamento dentro de listas compostas
pessoa = ['João', 19]  # crio várias listas com o nome e a idade de pessoas
pessoas = [['João', 19],['José', 23],['Nayta', 11]]  # coloco todas essas listas de outra lista
print(pessoas[0]) >>  ['João', 19]  # printa o primeiro valor da lista composta
print(pessoas[1]) >> ['José', 23]  # printa o segundo valor da lista compsota
print(pessoas[1][0]) >> José  # printa primeiro valor da lista simples dentro do segundo valor da lista composta
print(pessoas[2][1]) >> 11  # printa o segundo valor da lista simples dentro do terceiro valor da lista composta'''

# EXEMPLO 1
teste = list()  # cria lista chamada teste  (teste = []  também cria uma lista chama da teste)
# teste.append('Letícia', 24) >> da erro pq só da pra adc um valor de cada vez à lista
teste.append('Letícia')
teste.append(24)
galera = []
galera.append(teste[:])  # preciso colocar [:] pra fazer uma cópia da lista teste e quando...
print(galera)
teste[0] = 'Eduardo'  # ...eu mudar os valores da lista teste e der append em galera ela mostra o antigo e o nove valor...
teste[1] = '29'
galera.append(teste[:])  # ...não duas vezes o valor novo.
print(galera)
teste[0] = 'Lucas'
teste[1] = 9
galera.append(teste[:])
print(galera)

# EXEMPLO 2
galera = [['Letícia', 24], ['Eduardo', 29], ['Lucas', 9], ['Katiana', 26]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos.')

# EXEMPLO 3
galera = []
dados = []
for i in range(0, 3): # vai fazer 0, 1 e 2. O 3 não entra
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()  # preciso limpar se não o resultado vai ser [['le', 24], ['le', 24, 'lu', 9], ['le', 24, 'lu', 9, 'edu', 29]]
totmai = totmen = 0
for p in galera:
    if p[1] > 18:
        print(f'{p[0]} é maior de idade!')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totmen += 1
print(f'Temos {totmai} pessoas maiores de idade e {totmen} menores de idade!')
