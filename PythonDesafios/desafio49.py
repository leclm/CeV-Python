''' Refaça o desafio 9, mostrando a tabuada que o usuário escolher, só que agora usando um laço for. '''
print('\033[1;35m*_\033[m'*20)
print('\033[1;34mMONTE SUA TABUADA!\033[m'.center(50))
print('\033[1;35m*_\033[m'*20)
num = int(input('Digite o número que você quer fazer a tabuada: '))
num2 = int(input('Digite até que número você quer essa tabuada: '))
for i in range(0, num2+1):
    result = num * i
    print('{} x {:2} = {}'.format(num, i, result))
