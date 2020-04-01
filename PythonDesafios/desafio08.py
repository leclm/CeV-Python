'''Escreva um programa que leia um valor em m e escreva convertido em cm e mm.'''
valor = int(input('Digite um valor em metros: '))
km = valor * 0.001
hm = valor * 0.01
dam = valor * 0.1
dm = valor * 10
cm = valor * 100
mm = valor * 1000
print('A medida de {}m corresponde a:\n{}km\n{}hm\n{}dam\n'.format(valor, km, hm, dam), end='')
print('{}m\n{}dm\n{}cm\n{}mm'.format(valor, dm, cm, mm))
'''
números terminados em 3, 6 e 7 da problema no dam
números terminados em 9 da problema no km
'''
