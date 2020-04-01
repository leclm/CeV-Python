''' Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o menor e o maior peso lido.'''
# OPÇÃO 1
pesos = []
for i in range(0, 5):
    peso = float(input('Qual o peso da pessoa {}? '.format(i+1)))
    pesos.append(peso)
print('O maior peso digitado é {:.1f}kg e o menor é {:.1f}kg.'.format(max(pesos), min(pesos)))

# OPÇÃO 2
pesomax = 0
pesomin = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(i)))
    if i == 1:
        pesomax = peso
        pesomin = peso
    else:
        if peso > pesomax:
            pesomax = peso
        if peso < pesomin:
            pesomin = peso
print('O maior peso cadastrado é {:.1f} e o menor é {:.1f}.'.format(pesomax, pesomin))
