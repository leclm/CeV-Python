""" Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele fez. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tem sido
informado corretamente. """
def ficha(nome=False, gols=1):
    nome = str(input('Nome do jogador: '))
    gols = str(input('Número de gols marcado: '))
    if nome == '' and gols == '':
        print(f'O jogador desconhecido fez 0 gols.')
    elif nome == '':
        print(f'O jogador desconhecido fez {gols} gols.')
    elif gols == '':
        print(f'O jogador {nome} fez 0 gol(s).')
    else:
        print(f'O jogador {nome} fez {gols} gols.')


ficha()
