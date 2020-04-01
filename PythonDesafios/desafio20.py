'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que
leia o nome dos 4 alunos e mostre a ordem sorteada.
'''

import random
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
nomes = [a1, a2, a3, a4]
t = random.sample(nomes, 4)
print('A ordem das apresentações será: {}.'.format(' -> '.join(t)))

'''
nomes = []
for i in range(4):
    aluno = input('Digite o nome do aluno ' + str(len(nomes)+1) + ': ')
    nomes.append(aluno)
    
random.shuffle(lista)
print(' > '.join(lista))  # quando usar shuffle faz assim, colocando a lista reordenada no join

var = random.sample(lista, 4)
print(' > '.join(var))  # quando usar sample faz assim, colocando a nova variavel da amostra
'''