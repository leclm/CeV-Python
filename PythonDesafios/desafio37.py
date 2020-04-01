'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão :
1 para binário >> 2 para octal >> 3 para hexadecimal.
'''
import math
num = int(input('Digite um número inteiro: '))
print('''Escolha sua base de conversão:
[1] Binário
[2] Octal
[3] Hexadecimal
''')
opção = int(input('Sua opção:\n '))
if opção == 1:
    print('O número digitado convertido para binário é {}!'.format(bin(num)[2:]))
elif opção == 2:
    print('O número digitado convertido para octal é {}.'.format(oct(num).strip('0o')))
elif opção == 3:
    print('O número digitado convertido para hexadecimal é {}.'.format(hex(num).strip('0x')))
else:
    print('Esta opção é \033[4;31minválida\033[m.')
