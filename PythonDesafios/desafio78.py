''' Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final mostre qual foi o maior e o menor
valor digitado e suas respectivas posições na lista.'''
# OPÇÃO 1
numeros = []
for n in range(5):
    numeros.append(int(input('Digite um número: ')))
print(f'O maior número é {max(numeros)} e aparece nas posições: ', end='')
for p, v in enumerate(numeros):
    if v == max(numeros):
        print(f'{p+1}', end=' ')
print(f'\nJá o menor valor é {min(numeros)} e está nas posições: ', end='')
for p, v in enumerate(numeros):
    if v == min(numeros):
        print(p+1, end=' ')

# OPÇÃO 2
numeros = []
maior = 0
menor = 0
for n in range(5):
    numeros.append(int(input('Digite um número: ')))
    if n == 0:
        maior = menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        if numeros[n] < menor:
            menor = numeros[n]
print(f'O maior número é {maior} e aparece nas posições: ', end='')
for p, v in enumerate(numeros):
    if v == maior:
        print(f'{p+1}', end='... ')
print(f'\nJá o menor valor é {menor} e está nas posições: ', end='')
for p, v in enumerate(numeros):
    if v == menor:
        print(p+1, end='... ')
