for i in range(0, 2):
    print('Oi')

for c in range(1, 4):
    print(c)

for x in range(4, 0, -1):
    print(x)

n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for i in range(i, f+1, p):
    print(i)

s = 0
for i in range(0, 3):
    num = int(input('Digite um valor: '))
    s += num
print('O somatório destes valores é {}.'.format(s))
print('FIM!')
