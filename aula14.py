# Exemplo 1
for i in range(1, 10):  # Só posso usar quando eu sei o limite
    print(i)
print('FIM')
# Exemplo 2
c = 1
while c < 10:  # posso usar quando eu sei e quando eu não sei o limite
    print(c)
    c += 1
print('FIM')
# Exemplo 3
for i in range(1, 4):
    int(input('digite: '))
print('fim')
# Exemplo 4
resposta = 'S'
while resposta == 'S':
    i = int(input('digite: '))
    resposta = str(input('Quer continuar? [S/N] ')).upper()
print('fim')
# Exemplo 5
n = 1
par = impar = 0
totpar = totimpar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += n
            totpar += 1
        else:
            impar += n
            totimpar += 1
print('A quantidade de números ímpares é {} e a sua soma é {}.\n'
      'A quantidade de números pares é {} e sua soma é {}.'.format(totimpar, impar, totpar, par))
print('Acabou!')
