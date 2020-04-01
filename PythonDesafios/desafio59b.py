''' Crie um programa que leia dois valores e mostre um menu na tela: [1 soma >> [2 multiplicar >> [3 maior >> [4 novos
números >> [5 sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.'''
print('\033[1;36m=-\033[m'*20)
print('\033[1;33mOperações Matemáticas\033[m'.center(45))
print('\033[1;36m=-\033[m'*20)
print('Escolha dois valores para realizar operações entre eles!')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
print('')
print('Escolha uma das opções do menu abaixo: ')
print('''1. Soma\n2. Multiplicação\n3. Maior Valor\n4. Resetar Valores\n5. Sair do Programa''')
print('')
escolha = 0
while escolha != 5:
    escolha = int(input('Sua escolha: '))
    if escolha == 1:
        print('A soma entre {} e {} é igual a {}.\n'.format(n1, n2, n1 + n2))
    elif escolha == 2:
        print('O produto entre {} e {} é {}.\n'.format(n1, n2, n1 * n2))
    elif escolha == 3:
        if n1 > n2:
            print('O maior valor entre {} e {} é {}.\n'.format(n1, n2, n1))
        elif n1 < n2:
            print('O maior valor entre {} e {} é {}.\n'.format(n1, n2, n2))
        else:
            print('Não existe maior valor. Os dois valores são iguas!\n')
    elif escolha == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    else:
        print('Escolha inválida!\n')
print('Você saiu do programa!')
