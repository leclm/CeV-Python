""" Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
processo de cálculo do fatorial. """
def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: o número a ser calculado.
    :param show: (opcional) mostra ou não a conta.
    :return: o valor do fatorial de um número n.
    """
    f = 1
    if show:
        for c in range(n, 0, -1):
            f *= c
            if c != 1:
                print(f"{c} x", end=' ')
            else:
                print(f"{c} = {f}", end=' ')
    else:
        for c in range(n, 0, -1):
            f *= c
        print(f'O valor do fatorial de {n} é {f}.')


fatorial(6, True)
#help(fatorial)
