''' Faça um programa que leia nome e média de um aluno, guardando tbm a situação em um dicionário. No final, mostre o
conteúdo da estrutura na tela. '''
aluno = {'Nome': str(input('Nome: ')), 'Média': float(input('Média: ')), 'Situação': ''}
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 4 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('=-'*20)
for k, v in aluno.items():
    print(f'    - {k}: {v}')
