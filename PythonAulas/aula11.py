print('\033[32mOlá mundo!')  # vai ficar com a letra verde
print('\033[36;41mOlá mundo!')  # vai ficar com a letra ciano e o fundo vermelho até o fim da linha
print('\033[1;34;43mOlá mundo!\033[m')  # vai ficar sublinhado, com a letra azul e o fundo amarelo até o !
print('\033[4;30;46mOlá mundo!\033[m')  # vai ficar em negrito, com a letra roxa e o fundo ciano até o !
print('\033[0;33;44mOlá Mundo!\033[m')  # vai ficar com a letra amarela e o fundo azul
print('\033[7;33;44mOlá Mundo!\033[m')  # vai ficar com a letra azul e o fundo amarelo, inverteu por causa do 7
print('Os valores são \033[33m3\033[m e \033[35m5\033[m!!')
nome = 'Letícia'
print('Muito prazer em te conhecer {}{}{}!!'.format('\033[4;35m', nome, '\033[m'))
name = 'Eduardo'
cores = {'limpa': '\033[m',
         'amareloesub': '\033[4;33m',
         'azulenegrito': '\033[1;34m'}
print('Muito prazer em te conhecer {}{}{}!'.format(cores['amareloesub'], name, cores['limpa']))
print('Muito prazer em te conhecer {}{}{}!'.format(cores['azulenegrito'], nome, cores['limpa']))
