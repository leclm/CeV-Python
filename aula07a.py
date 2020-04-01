n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
mod = n1 % n2
exp = n1 ** n2
print('A soma é {}\nA multiplicação é {}\nA divisão é {}'.format(s, m, d, di, mod, exp), end='')
print(' e a divisão inteira é {}\nO módulo é {}\nA exponenciação é {}'.format(di, mod, exp))
