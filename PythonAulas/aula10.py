nome = str(input('Qual o seu nome? '))
if nome == 'Letícia':
    print('Que nome maravilindo!!!')
else:
    print('Seu nome é um flop...kkk')
print('Bom dia {}, beba muita água hoje!'.format(nome))
#
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1+n2)/2
print('A sua média é {:.1f}'.format(m))

print('Parabéns vc passou!' if m > 6.0 else 'Você reprovou!')  # condição simplificada, acho que nao dá pra fazer com elif

if m < 4.0:
    print('Você está reprovado!')
elif 4.0 <= m < 7.0:
    print('Você está de final!')
elif m >= 7.0:
    print('Você passou!')
