''' Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu
programa deverá ler um número pelo teclado entre (0 e 10) e mostrá-lo por extenso. '''
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
while True:
    num = int(input('Digite um número entre 0 e 10: '))
    if 0 <= num <= 10:
        print(f'Este número por extenso é: {numeros[num]}!')
        break
    else:
        print('Você digitou um número fora do intervalo delimitado. Tente novamente!\n')
