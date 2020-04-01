'''Faça um programa que leia a altura e a largura de uma parede em metros, calcule sua área e a quantidade de tinta'''
''' necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².'''
h = float(input('Qual a altura em metros da parede? '))
l = float(input('Qual a largura em metros da parede? '))
a = h*l
v = a/2
print('Você vai precisar de {} litros de tinta para pintar uma parede de área {} m².'.format(v, a))
