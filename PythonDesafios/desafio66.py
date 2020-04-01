''' Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual a soma entre eles.
Desconsiderando a flag.'''
txt = '\nLeitura e Análise Numérica'
print(f'\033[1;36m{txt:^40}\033[m\n')
soma = quant = 0
while True:
    n = int(input('Digite um número (digite 999 para parar): '))
    if n == 999:
        break
    soma += n
    quant += 1
print(f'Foram digitados {quant} números e a soma entre eles é {soma}.')
