''' Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa
progressão.'''
a1 = int(input('\033[1;31mDigite o primeiro termo da PA: \033[m'))
r = int(input('\033[1;33mDigite a razão da PA: \033[m'))
lista = [a1]
for n in range(2, 10):
    an = a1 + (n-1)*r
    lista.append(an)
print('\033[1;30mOs 10 primeiros termos desta PA são:\033[m\n\033[1;34m{}\033[m'.format(str(lista).strip('[]')))



a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
a10 = a1 + (10-1)*r
for i in range(a1, a10 + r, r):
    print('{}'.format(i), end=' -> ')
print('POR HOJE É SÓ')
