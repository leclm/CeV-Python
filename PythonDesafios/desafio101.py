''' Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
pessoa, retornando um valor literal indicando de uma pessoa tem voto obrigatório, opcional ou se não pode votar. '''
def voto(ano):
    from datetime import date
    aa = date.today().year
    idade = aa - ano
    if idade < 16:
        return f'Idade {idade} anos: voto NEGADO!'
    if 16 <= idade < 18 or idade >= 65:
        return f'Idade {idade} anos: voto OPICIONAL!'
    if 18 <= idade < 65:
        return f'Idade {idade} anos: voto OBRIGATÓRIO!'


an = int(input('Em que ano você nasceu? '))
print(voto(an))
