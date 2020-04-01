# EXEMPLO 1
def lin():
    print('=-' * 15)
lin()
print(f'{"Letícia Lindícia":^30}')
lin()

# EXEMPLO 2
def mensagem(msg):
    print('=-' * 20)
    print(f"{msg:^40}")
    print('=-' * 20)
mensagem('Hoje é Halloween')
mensagem('Eu estudo programação')

# EXEMPLO 3
def soma(a, b):
    s = a + b
    print(f'A soma de A = {a} e B = {b} é {s}.')
soma(b=3, a=5)  # posso inverter a ordem colocando o parametro a=x no parenteses

# EXEMPLO 4: EMPACOTAMENTO
def contador(*num):
    print(num)  # vai criar uma tupla com os parâmetros que eu colocar quando chamar a função
    for i in num:
        print(f"{i} ", end="")  # printa os num um do lado do outro sem ()
    print('Fim')
    quant = len(num)
    print(f'Recebi os números {num} e ao todo são {quant} números.'.replace('(', '').replace(')', ''))
contador(3, 5, 6)
contador(1, 4, 6, 7, 8, 0)

# EXEMPLO 5: dobrar valores dentro de uma lista (mutável). Tupla não é mutável.

def dobra(lista):
    posição = 0
    while posição < len(lista):
        lista[posição] *= 2
        posição += 1
    print(lista)
numero = [2, 4, 8, 1]
dobra(numero)
