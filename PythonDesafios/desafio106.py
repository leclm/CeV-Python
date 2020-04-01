''' Faça um mini sistema que utilize o interective help do python. O usuário vai digitar o comando e o manual vai
aparecer. Quando o usuário digitar a palavra FIM, o programa se encerra. OBS: use cores.'''
def ajuda():
    from time import sleep
    a = 0
    while a != 'fim':
        print('\033[2;30;42m', end='')
        print('^' * (len('SISTEMA DE AJUDA PyHELP') + 4))
        print('  SISTEMA DE AJUDA PyHELP  ')
        print('^' * (len('SISTEMA DE AJUDA PyHELP') + 4))
        print('\033[m', end='')
        a = str(input('Função ou biblioteca > '))
        if a == 'fim':
            print('\033[2;30;41m', end='')
            print('^' * (len('ATÉ LOGO') + 4))
            print('  ATÉ LOGO  ')
            print('^' * (len('ATÉ LOGO') + 4))
            print('\033[m', end='')
            break
        print('\033[2;30;46m', end='')
        print('^' * (len(f'ACESSANDO O MANUAL DO COMANDO {a}') + 6))
        print(f'  ACESSANDO O MANUAL DO COMANDO > {a}  ')
        print('^' * (len(f'ACESSANDO O MANUAL DO COMANDO {a}')  + 6))
        print('\033[2;30;46m', end='')
        sleep(0.5)
        print('\033[2;31;40m', end='')
        help(a)
        print('\033[m', end='')


ajuda()
