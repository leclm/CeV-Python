'''
Refaça o exercício 35 acrescentando o recusro de msotrar que tipo de triângulo será formado: equilatero = se todos os
lados sao iguais; isosceles se tem 2 iguais ou escaleno se nao tem nenhum igual.
'''
a = float(input('Digite o comprimento da primeira reta: '))
b = float(input('Digite o comprimento da segunda reta: '))
c = float(input('Digite o comprimento da terceira reta: '))
print('\033[34m=\033[m'*100)
if a < b + c and b < a + c and c < a + b:
    print('Estas retas podem formar um triângulo ', end='')
    if a != b and b != c and c != a:
        print('do tipo escaleno, ou seja, todos os lados têm medidas diferentes.')
    elif (a == b and b != c) or (a == c and c != b) or (c == b and b != a):
        print('do tipo isósceles, ou seja, possui dois lados com as mesmas medidas. ')
    elif a == b == c:
        print('do tipo equilátero, ou seja, possui todos os lados iguais.')
else:
    print('Estas retas não podem formar um triângulo.')
