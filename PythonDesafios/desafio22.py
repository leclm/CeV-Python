'''
Crie um programa que leia o nome completo de uma pessoa e mostre: a) o nome com todas as letras maiúsculas ; b) o nome
com todas minúsculas; c) quantas letras ao todo (sem considerar espaços) e d) quantas letras tem o primeiro nome.
'''
nome = str(input('Qual o seu nome completo? ')).strip()  # vai tirar os espaços no início e final
print('Seu nome com todas as letras maiúsculas fica dessa forma: {}.'.format(nome.upper()))
print('Seu nome com todas as letras minúsculas fica dessa forma: {}.'.format(nome.lower()))

sem_espaço = nome.replace(' ', '')
print('Seu nome tem {} letras.'.format(len(sem_espaço)))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))  # vai tirar os espaços do len

lista = nome.split()
print('Seu primeiro nome tem {} letras.'.format(len(lista[0])))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))  # vai dar o index do primeiro espaço que corresponde ao número de caracteres antes dele, ou seja, ao tamanho do primeiro nome
