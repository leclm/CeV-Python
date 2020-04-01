''' Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais.
'''
palavras = ('leticia', 'eduardo', 'namorado', 'felicidade', 'companheirismo', 'paixao', 'amor', 'bonitinho', 'rabinho')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')