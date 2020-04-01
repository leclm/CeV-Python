'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
 programa será interrompido quando o número digitado for negativo.'''
while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    print('='*40)
    if n < 0:
        print('Programa finalizado!')
        break
    for i in range(1, 11):
        result = i * n
        print(f'{n} x {i} = {result}'.center(40))
    print('='*40)