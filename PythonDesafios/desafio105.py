''' Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornando um dicionário
com as seguintes informações: - quantidade de notas; - a maior nota; - a menor nota; - a média da turma; - a situação
(opcional). Adicione também as docstrings da função. '''
def notas(*n, sit=False):
    """
        -> Função para analisar notas e situações de vários alunos.
        :param n: uma ou mais notas dos alunos (aceita várias)
        :param sit: valor opcional, indicando se deve ou não mostrar a situação.
        :return: dicionário com várias informações sobre a situação da turma
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] > 7:
            r['Situação'] = 'Boa'
        elif r['Média'] < 5:
            r['Situação'] = 'Ruim'
        else:
            r['Situação'] = 'Regular'
    return r


resp = notas(2.5, 6.9, 1.9, 1.9, sit=True)
print(resp)
help(notas)
