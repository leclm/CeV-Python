'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo o nome dos escolhidos.
'''
from random import choice
alunos = []
for i in range(4):
    print('Digite o nome do aluno ' + str(len(alunos)+1) + ': ')
    nome = input()
    alunos.append(nome)
escolhido = choice(alunos)
print('O aluno sorteado foi: {}.'.format(escolhido))
