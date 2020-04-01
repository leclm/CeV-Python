''' Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 termos. '''
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
ac = 0
x = 11
termos = []
ax = 0
novostermos = []
while c < 11:
    ac = a1 + (c - 1) * r
    termos.append(ac)
    c += 1
print('Os 10 primeiros termos dessa PA são: ')
print(''.join(str(termos)).strip('[]'))
while c >= 11:
    i = int(input('Você quer ver mais termos dessa PA? (Se sim, digite quantos. Se não, digite 0): '))
    while i != 0 and (x < (i+11)):
        ax = a1 + (x - 1) * r
        novostermos.append(ax)
        x += 1
    print('Os próximos {} termos dessa PA são: '.format(i))
    print(''.join(str(novostermos)).strip('[]'))
print('FIM!')
