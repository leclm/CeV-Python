'''# EXEMPLO 1
cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou!')
# EXEMPLO 2
n = 0  # stop com flag
while n != 999:
    n = int(input('Digite um número: '))
# EXEMPLO 3
n = s = 0
while True:  # stop com break
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma dos números digitados é {s}.')  #PEP 468 FSTRINGS
'''# EXEMPLO 4
nome = 'José'
idade = 34
salário = 5700.5
print(f'O {nome:~^20} tem {idade} anos e ganha R${salário:.2f} por mês.')
print(f'{nome:~^20}')  # centraliza o nome entre os ~ dentro de 20 espaços
print(f'{nome:~>20}')  # alinha o nome a direita dentro do 20 espaços, nome fica a direita
print(f'{nome:~<20}')  # alinha o nome a esquerda dentro do 20 espaços, nome fica a esquerda
