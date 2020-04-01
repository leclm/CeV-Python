''' Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: a) Quantos números foram
digitados >> b) A lista de valores ordenada de forma decrescente >> Se o valor 5 foi digitado e está ou não na lista.'''
num = []
resp = ' '
while resp != 'N':
    n = int(input('Digite um número: '))
    num.append(n)
    resp = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
    if resp == 'N':
        print('\nPrograma finalizado!\n')
        break
print(f'Ao todo foram digitados {len(num)} números.')
num.sort(reverse=True)
print(f'Os números em ordem decrescente são: {num}')
if 5 in num:
    print(f'O número 5 está na lista na posição {num.index(5)+1}.')
else:
    print('O número 5 não está na lista.')
