'''Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada '''
num = int(input('Digite o número que vc deseja saber a tabuada: '))
num2 = int(input('Digite até qual número vc quer a tabuada: '))
print('*' * 12)
for i in range(1, num2 + 1):
    print(num, 'x', i, '=', str(i * num))
    print(str(num) + ' x ' + str(i) + ' = ' + str(i * num))
print('*' * 12)
