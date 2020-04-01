frase = 'Bom dia lindo dia prof shirley cesmag'
# de strings
print(frase[2::4])  # printa os carac de 2 até o final, pulando de 4 em 4
print(frase[::2])  # printa a str do ínicio as fim pulando de 2 em 2
print(frase[2:17:2])  # printa os carac começando no 2 indo até o 16, pulando de 2 em 2
print(frase[:30])  # printa os carac do ínicio até o index 29 (30 não conta)
print(frase[3:])  #  printa os caracteres começando no 3 e indo até o fim da string
# Análise de strings
print(len(frase))  # retorna o número de microespaços na string
print(frase.count('dia'))  # retorna quantas vezes aparece 'dia' na string toda
print(frase.count('dia', 3, 30)) # retornar quantas vezes aparece o que eu procurei no intervalo de index 3 até 30
print(frase.find('dia'))  # retorna o index do início do que eu procurei
print(frase.find('olá'))  # retornar -1 signif que não tem o que eu procuro na string
print('dia' in frase)  # retorna True ou False se a string estiver contida ou não na frase
# Transformações em strings usando métodos
print(frase.replace('dia','nascer do sol')) #troca dia por nascer do sol na string. Troca todos os dias que ele achar
# como trocar só um dos dias?
print(frase.upper())
print(frase.lower())
print(frase.capitalize())  # deixa só a primeira letra da primeira palavra maiuscula, o resto todo minúsculo
print(frase.title())  # deixa maiúscula a primeira letra de todas as palavras
nova = '    Aprenda Python     '
print(nova)
print(nova.strip())  # remove os espaços em brancos em left e right
print(nova.rstrip())  # remove espaços em branco no right
print(nova.lstrip())  # remove espaçoes em branco no left
print(frase.split())  # separa uma string em pedaços e coloca numa lista
print('&'.join(frase))  # juntao os valores de uma lista e forma uma string, pode colocar coisas entre os pedaços (&)
print(frase.find('bom'))
print(frase.lower().find('bom'))  # pode colocar varios modulos na mesma linha e sem ()
print(frase.find('shirley'))

print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[2][3])  # vai pegar o valor 2 da lista (lindo) e depois mostrar a letra na posição 3 deste valor (letra d de lindo)
