''' Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira
função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os
valores pares sorteados pela função anterior. '''
from random import randint
numeros = []
def sorteia():
    print('Os números sorteados foram: ', end='')
    for n in range(5):
        num = randint(0, 10)
        numeros.append(num)
        print(num, end=' ', flush=True)


def somaPar():
    soma = 0
    for n in range(len(numeros)):
        if numeros[n] % 2 == 0:
            soma += numeros[n]
    print(f"A soma dos números pares sorteados é {soma}.")


sorteia()
somaPar()
