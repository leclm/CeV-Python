"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares"""
"""ela pode comprar. Considere US$ 3.27 = 1.00 real."""
money = float(input('Quantos taokeys vc tem nessa carteira amadah? R$'))
trumps = 3.27
doletas = money/trumps
print('Com R${:.2f} taokeys você pode comprar US${:.2f} doletas.'.format(money, doletas))
