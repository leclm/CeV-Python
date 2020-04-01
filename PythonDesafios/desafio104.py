""" Crie um programa que tenha uma função chamada leiaInt(), que vai funcionar de forma semelhante a função input() do
Python, só que fazendo a validação para aceitar apenas um valor numérico. """
def leiaInt(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[31mERRO! Digite um número inteiro válido!\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
