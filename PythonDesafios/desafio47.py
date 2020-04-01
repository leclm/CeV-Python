''' Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 a 50.'''

par = []
for i in range(1, 51): #faz todos os laços, menos dos ímpares
    if i % 2 == 0:
        par.append(i)
print('Os \033[33mnúmeros pares\033[m são entre 1 e 50 são:\n{}'.format(str(par).strip('[]')))

for i in range(2, 51, 2): # ocupa o processador pela metade do tempo do que na outra forma, pois faz a metade de laços(pula de 2 em 2)
    print(i, end=' ')
