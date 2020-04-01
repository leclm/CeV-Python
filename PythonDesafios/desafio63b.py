''' Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia
 de fibonacci. REFAZER PQ VC NAO ENTENDEU NADA LETICIA'''
print('\033[1;36m~.\033[m'*20)
print('\033[1;33mSequência de Fibonacci\033[m'.center(45))
print('\033[1;36m~.\033[m'*20)
n = int(input('\nQuantos números da \033[35mSequência de Fibonacci\033[m vc quer ver? '))
t1 = 0
t2 = 1
c = 3
print('Os {} primeiros termos da Sequência de Fibonacci são:\n'.format(n))
print('{} -> {} -> '.format(t1, t2), end='')
while c <= n:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1
print('Fim!')
