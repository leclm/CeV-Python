''' Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
Se por acaso a CTPS for diferente de zero, o dicionário receberá tbm o ano de contratação e o salário. Calcule a
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
# from datetime import datetime
# idade = datetime.now().year - anonasc
from datetime import date
atual = date.today().year
dados = {
    'nome': str(input('Digite o seu nome: ')),
    'nasc': int(input('Ano de nascimento: ')),
    'CTPS': int(input('Número da CTPS (0 se não tiver): '))
        }
idade = atual - dados['nasc']
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = int(input('Salário R$ '))
    contribuição = date.today().year - dados['Ano de contratação']
    aposent = idade + 35 - contribuição

print('=-'*60)

print(f'Nome: {dados["nome"].title()}')
print(f'Idade: {idade} anos')
print(f'CTPS: {dados["CTPS"]}')

if dados['CTPS'] != 0:
    print(f"Contratação: {dados['Ano de contratação']}")
    print(f"Salário: R$ {dados['Salário']:.2f}")
    print(f"Idade de aposentar: {aposent}")
