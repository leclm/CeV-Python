''' Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificío, indo de 10 até 0,
com uma pausa de 1 segundo entre eles. '''
from time import sleep

print('\033[1;36m=\033[m'*40)
print('\033[1;33mCONTAGEM REGRESSIVA PARA O ANO NOVO!!!!\033[m')
print('\033[1;36m=\033[m'*40)

for x in range(10, -1, -1):
    print(x)
    sleep(0.5)
print('\033[4;35mHAPPY NEW YEAR\033[m!!!')
