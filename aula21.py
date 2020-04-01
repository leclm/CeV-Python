#INTERACTIVE HELP
#help(input)  # posso usar no console, mas nao funciona aqui. Da pra usar no IDEL velha
#print(input.__doc__)  # nao necessariamente vai dar a mesmo informação que usando o help()
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.  # isso se chama docstring, explicação da função
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM')


#contador(2, 10, 2)
#help(contador())  # se colocar () depois de contador nao funciona o help
help(contador)  # tem que ser assim

# PARÂMETRO OPCIONAL
def soma(a, b, c):  # deixando desse jeito se eu colocar só 2 valores quando chamar a função vai dar erro
    s = a + b + c
    print(f'A soma dos valores vale {s}.')


soma(2, 3, 4)

def soma(a, b, c=0):  # se eu nao colocar um valor para c ele vai valer automaticamente 0. posso por a=0 e b=0 tbm e aí se eu chamar soma() não da erro.
    s = a + b + c
    print(f'A soma dos valores vale {s}.')


soma(a=2, c=3)


# ESCOPO DE VARIÁVEIS: Local onde a variável vai existir e nao vai existir mais
def teste():
    x = 9  # variável locas
    print(f'No programa principal a variável n vale {n}.')  # n aparece pq ele esta definido no escobo global do programa
    print(f'No programa principal a variável x vale {x}.')


n = 2  # variável global
print(f'No programa principal a variável n vale {n}.')
teste()
print(f'No programa principal a variável x vale {x}.')  # da erro pq x esta no escolo local da função teste

                # EXEMPLO ESCOPOS DE VARIÁVEIS
def teste(b):  # b é o parametro formal
    global a  # dessa forma o valor de a=5 vai ser perdido e a vai passar a valer 8, no global e no local
    a = 8  # tenho duas variáveis a no promgrama, uma local (esta) e uma global (a=3)
    b += 4
    c = 5
    print(f'A dentro vale {a}')  # variável global
    print(f'B dentro vale {b}')  # somou a + 4
    print(f'C dentro vale {c}')


a = 3
teste(a)  # a é o parametro real
print(f'A fora vale {a}')

# RETORNANDO VALORES: UTIL SE QUE QUERO TER PERSONALIZAÇÃO DE RESULTADOS
def soma(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma é {s}.')


soma(3, 4, 1)
soma(4, 2)
soma(2)


def soma(a=0, b=0, c=0):
    s = a + b + c
    return s  # pra usar return eu tenho que atribuir variáveis (r1, r2, r3) ou colocar direto no print(soma(4))


r1 = soma(3, 4, 1)
r2 = soma(4, 2)
r3 = soma(2)
print(f'As minhas somas deram {r1}, {r2} e {r3}.')

# EXERCÍCIO PRÁTICO: FATORIAL
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(3)
f3 = fatorial(6)
print(f'Os fatoriais são {f1}, {f2} e {f3}.')

# EXERCÍCIO PRÁTICO PAR OU ÍMPAR
def par(num = 0):
    if num % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número para saber se é par: '))
print(par(num), end='. ')
if par(num):
    print('É par!')
else:
    print('Não é par!')
