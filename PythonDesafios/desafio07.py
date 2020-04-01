'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média. '''
notas = []
n1 = float(input('Digite a nota 1: '))
notas.append(n1)
n2 = float(input('Digite a nota 2: '))
notas.append(n2)
s = n1+n2
# print(len(notas))
m = s/len(notas) # m = s/2
print('A média das notas é {}.'.format(m))


