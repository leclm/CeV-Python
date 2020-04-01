''' Temos variáveis simples e compostas:
VS = só pode receber um elemento. Ex: numero = 1. Se eu quiser atribuir o número 2 a variável numero (numerp = 2), o
número 1 vai ser apagado e o 2 vai tomar seu lugar. Não consigo atribuir o 1 e o 2 ao mesmo tempo a VS numero.
VC = posso atribuir vários elementos a mesma variável. No python existem três tipos de VC: tuplas, listas e dicionáios.

# TUPLAS: entre parênteses, funciona mesmo se não colocar
SÃO IMÚTAVEIS: Ñ CONSIGO TROCAR/ADICIONAR/EXCLUIR OS ELEMENTOS DA TUPLA. Mas posso apagar a tupla toda usando del
Posso colocar elementos de tipos diferentes dentro da tupla, str, int, float...
Posso atribuir quantos valores eu quiser em uma tupla, só preciso definir isso.
Os elementos de uma tupla têm índices: print(lanche[1]) me da o segundo elemento da tupla >> print(lanche[0:2]) mostra
o elemento 0 e o 1, o 2 ele exclui >> print(lanche[1:]) mostra o 1 e todos os outros até o fim >> print(lanche[-1])
mostra o último >> len(lanche) mostra quantos elementos tem na tupla/VC lanche >> for c in lanche: print(c) vai mostrar
todos os elementos da VC/coleção.
Strings são VC.
'''
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
print(lanche)
print(lanche[2])  # só assim printa sem os () e ''
print(lanche[:-2])
print(lanche[:2])
print(lanche[-2:])
for cont in range(0, len(lanche)):
    print(cont)  # printa o index dos elementos na tupla

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba!')

for kkk, comida in enumerate(lanche):  # onde eu colocar o kkk vai me mostrar o index de cada elemento.
    print(f'Eu vou comer {comida} na posição {kkk}.')  # nesse modo uso duas variaveis (kkk e comida )pra poder mostrar a posição

print(sorted(lanche))  # coloca em ordem os elementos da tupla, mas nao muda a tupla, só mostra em ordem
# sorted transforma a tupla em lista pra poder mudar a ordem, mostra colchetes

a = (2, 4, 5)
b = (3, 4, 7, 8)
c = a + b
d = b + a
print(d)
print(c)
print(len(c))
print(c.count(4))  # mostra quantas vezes parece o num 4 na tupla c
print(c.index(5))  # mostra em que posição esta o elemento "5"
print(c.index(4))  # como tem dois 4 na tupla ele vai mostrar a posição do primeiro 4 que aparecer
print(c.index(4, 2))  # mostra a pos do 4 a partir do elemento da pos 2, não vai mostrar o 4 na pos 1, só o da pos 4

pessoa = ('Letícia', 24, 'F', 68.87)
del pessoa  # não posso deletar só um item ex: del pessoa[0]
print(pessoa)
