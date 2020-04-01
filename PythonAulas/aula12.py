nome = str(input('Digite seu nome: '))
if nome == 'Letícia':
    print('Esse é o nome mais lindo da galáxia!')
elif nome == 'Katiana':
    print('Minha amiga também se chama {}!'.format(nome))
elif nome == 'Eduardo':
    print('Meu namorado se chama {}!'.format(nome))
elif nome == 'Paulo' or nome == 'João' or nome == 'José':
    print('Esse é um nome bíblico!')
else:
    print('Seu nome é bem normal!')
print('Bom dia, {}! Prazer em te conhecer :)'.format(nome))
