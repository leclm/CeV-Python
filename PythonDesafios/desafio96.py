''' Faça um programa que tenha uma função chama área(), que receba as dimenções de um terreno retangular e mostre a área '''
def area():
    print('=' * 30)
    print(f"{'Controle de Terrenos':^30}")
    print('=' * 30)
    a = int(input('Largura: '))
    b = int(input('Comprimento: '))
    s = a*b
    print('=' * 30)
    print(f"{f'A área do terreno é {s} u.a.':^30}")


area()
