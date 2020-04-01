'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h mostre uma mensagem dizendo que ele
foi multado. A multa vai custar R$7,00 por cada km acima do limite.
'''
veloc = int(input('Digite a velocidade do carro: '))
multa = (veloc - 80) * 7
if veloc > 80:
    print('\033[30;41mVocê foi multado!\033[m\nO valor da multa é \033[4;31mR${:.2f}\033[m.'.format(multa))
else:
    print('Você está dentro do limite de velocidade!')
