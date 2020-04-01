'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
- se ele ainda vai se alistar ao serviço militar >> - se é a hora de se alistar >> - se ja passou do tempo de
alistamento.
Seu programa tbm deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
sex = str(input('Qual o seu sexo? ')).lower()
if sex == 'feminino':
    print('O seu alistamento não é obrigatório, mas se quiser pode.')
elif sex == 'masculino':
    ano = int(input('Qual o ano do seu nascimento? '))
    atual = date.today().year
    idade = atual - ano
    if idade > 18:
        print('Já passou \033[1;35m{} ano(s)\033[m da data que você deveria ter se alistado. Você se alistou POC?'.format(idade-18))
    elif idade == 18:
        print('\033[1;30;41mEstá na hora do alistamento kkk\033[m')
    else:
        print('Você \033[1;30;42mprecisa\033[m se alistar em {} anos. Do not forget!'.format(18-idade))
else:
    print('Você disse que seu sexo é "{}", vamos avaliar particularmente seu caso.'.format(sex))
