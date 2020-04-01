''' LISTAS
comidas = ['pao', 'agua', 'cachorro-quente']
Listas são mutáveis. É uma variável composto. Pode guardar vários valores.
comidas.append('refri') >> adc refri na ultima posição da lista
comidas.insert(0, 'refri') >> adc refri na posição zero, todos os outros elementos são deslocados. Nenhum pe apagado.
del comidas[3] >> apaga o valor da posição três
comidas.pop(3) >> apaga o valor na posição três, se eu não colocar nada apaga o ultimo valor.
comidas.remove('agua') >> coloca o valor e nao o index. remove a primeira ocorrencia
comidas.sort() >> ordena pelo alfabeto/num
comidas.sort(reverse=True) >> ordena pelo alfabeto/num na ordem inversa
valores = list(range(4, 11)) >> gera em uma lista os valores ate o 10 na ordem num cresc
len(comidas)

valores = []
for i in range(3):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'O valor {v} está na posição {c}')

a = [2, 4, 6, 9]
b = a >> cria uma ligação entre as duas listas
b[2] = 1 >> mudando em b vai mudar em a tbm, pois elas estao ligadas. B não é uma copia de a, é uma ligação
b = a[:] >> dessa forma eu atribuo todos os valores de a em b, fiz uma copia de a. se mudar uma nao muda a outra


'''