''' Faça um programa que tenha um função chamada contador(), que receba três parâmetros: ínicio, fim e passo e realize
a contagem. Seu programa tem que realizar três contagens através da função criada: a) De 1 até 10, de 1 em 1 >>
b) De 10 até 0, de 2 em 2 >> c) Uma contagem personalizada. '''
from time import sleep
def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print('=-' * 20)
    print(f'Contagem de {i} até {f}, de {p} em {p}:')
    sleep(0.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.25)
            cont += p
        print('FIM')
    if i > f:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.25)
            cont -= p
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('=-' * 20)
print('Agora é com você!')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(início, fim, passo)

