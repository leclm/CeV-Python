'''
Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem cobrando R$0,50 por km
para viagens até 200km e R$0,45 para viagens mais longas.
'''
dist = float(input('Qual a distância da viagem? '))
if dist <= 200:
    preço = dist*0.5
    print('O preço da passagem é R${:.2f}!'.format(preço))
else:
    preço = dist*0.45
    print('O preço da passagem é R${:.2f}!'.format(preço))
####
print('o preço da passagem é R${:.2f}!'.format(dist*0.5) if dist <= 200 else 'O preço da passagem é R${:.2f}!'.format(dist*0.45))
