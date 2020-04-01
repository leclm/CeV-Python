'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a
média atingida.
média abaixo de 5.0 = reprovado >> média entre 5.0 e 6.9 = recuperação >> média maior ou igual a 7.o = aprovado.
'''
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
if m >= 7.0:
    print('\033[1;36mAPROVADO!!!\033[m')
elif 5.0 <= m <= 6.9:
    print('\033[1;33mRECUPERAÇÃO!!!\033[m')
else:
    print('\033[1;31mREPROVADO!!!\033[m')