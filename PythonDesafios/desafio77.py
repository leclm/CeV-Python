''' Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.
'''
palavras = ('leticia', 'eduardo', 'namorado', 'felicidade', 'companheirismo', 'paixao', 'amorzinho', 'bonitinho', 'rabinho')
for i in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[i].upper()} as vogais são: ', end='')
    while 'a' in palavras[i]:
        print('A ', end='')
        break
    while 'e' in palavras[i]:
        print('E ', end='')
        break
    while 'i' in palavras[i]:
        print('I ', end='')
        break
    while 'o' in palavras[i]:
        print('O ', end='')
        break
    while 'u' in palavras[i]:
        print('U ', end='')
        break
