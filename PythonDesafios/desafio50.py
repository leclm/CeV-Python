''' Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.'''
números = []
for i in range(0, 6):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        números.append(num)
        soma = sum(números)
print('A soma dos números pares digitados é {}!'.format(soma))


pares = 0
for i in range(0, 6):
    num = int(input('Digite o {}° número: '.format(i+1)))
    if num % 2 == 0:
        pares += num
print('A soma dos números pares desta sequência é {}.'.format(pares))
