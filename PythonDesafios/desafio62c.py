''' Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
ele disser que quer mostrar 0 termos. '''
a1 = int(input('Digite o primeiro termo na PA: '))
r = int(input('Digite a razão da PA: '))
total = 0
mais = 10
c = 0
while mais != 0:
    total += mais
    while c < total:
        print(a1, end=' -> ')
        a1 += r
        c += 1
    mais = int(input('Quantos termos mais vc quer ver desta PA? '))
print('Programa encerrado!')
