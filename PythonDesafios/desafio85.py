''' Crie um programa onde o usuário posso digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separado os valores pares e ímpares. No final, Mostre os valores pares e ímpares em ordem crescente. '''
num = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i}° número: '))
    if n % 2 == 0:
        num[0].append(n)
    elif n % 2 == 1:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Os números pares são: {num[0]}')
print(f'Os números ímpares são: {num[1]}')
