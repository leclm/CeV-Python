''' Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre: a) quantas
vezes apareceu o valor 9 >> b) Em que posição foi digitado o primerio valor 3 >> c) quais foram os núm pares. '''
a = ()
pares = ()
for i in range(4):
    num = (int(input('Digite um número: ')),)
    a += num
for i in range(4):
    result = a[i] % 2
    if result == 0:
        np = (a[i],)
        pares += np
print(f'Os números pares desta tupla são: {pares}')
print(f'O número 9 aparece {a.count(9)} vezes nesta tupla.')
if 3 in a:
    print(f'O número 3 aparece pela primeira vez na posição {a.index(3)+1}.')
else:
    print('O número 3 não está presente nesta tupla.')
