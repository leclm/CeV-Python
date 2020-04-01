''' Faça um mini sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai
aparecer. Quando o usuário digitar a palavra FIM, o programa se encerra. OBS: use cores.'''
def ajuda():
    a = 0
    while a != 'fim':
        tam = len(txt)
        print(f'  SISTEMA DE AJUDA PyHELP \'{tam}\' ')
        a = str(input('  Função ou Biblioteca > '))
        if a == 'fim':
            print('  ATÉ LOGO  ')
            break
        help(a)


ajuda()
