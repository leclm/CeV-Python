''' Faça um programa que tenha uma função chamamda maior(), que receba vários parâmetros com valores inteiros. Seu
programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep
def maior(* n):
    resp = ''
    valores = []
    while resp != 'N':
        n = int(input('Digite um inteiro: '))
        valores.append(n)
        resp = str(input('Deseja adc outro valor [S/N]? ')).upper().strip()[0]
        if resp not in 'SN':
            resp = str(input('Resposta inválida. Deseja adc outro valor [S/N]? '))
    valores.sort()
    print('Analisando valores fornecidos...')
    sleep(0.5)
    print(f'Os valores adicionadas foram: ', end='')
    for n in range(len(valores)):
        print(valores[n], end=' ')
        sleep(0.5)
    print(f'FIM. O maior dentre eles é {valores[-1]}.')


maior()
