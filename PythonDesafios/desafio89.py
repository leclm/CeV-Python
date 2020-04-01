''' Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
 um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada um individualmente.'''
ficha = []
resp = 0
while resp != 'N':
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    med = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], med])
    resp = str(input('Deseja adicionar outro aluno [S/N]? ')).strip().upper()[0]
    while resp not in 'NS':
        resp = str(input('Deseja adicionar outro aluno [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break
print('=-'*20)
print(f'{"Boletim":^40}')
print('=-'*20)
print(f'{"N°":<12}', f'{"NOME":^12}', f'{"MÉDIA":>12}')
print('=-'*20)
for i, v in enumerate(ficha):
    print(f'{i:<12}', f'{ficha[i][0]:^12}'.title(), f'{ficha[i][2]:>12}')
aluno = 0
while aluno != '999':
    aluno = int(input('\nDigite o número do aluno para ver suas notas (digite 999 para sair): '))
    if aluno < len(ficha):
        print(f'As notas de {ficha[aluno][0].title()} são: {ficha[aluno][1]}')
    if aluno >= len(ficha) and aluno != 999:
        print('\nAluno não existente. Tente novamente.')
    if aluno == 999:
        print('\nPrograma Finalizado!')
        break
