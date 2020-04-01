'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável. '''
def escreva(txt):
    print('=' * len(txt))
    print(txt)
    print('=' * len(txt))


escreva('   Eu sou linda    ')
escreva('   Meu irmão é maravilhoso    ')
escreva('   Hoje é halloween e eu vou participar de uma festa com meu irmção e minha tia    ')
