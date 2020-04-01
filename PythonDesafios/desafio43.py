'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela
abaixo. abaido de 18.5 = abaixo do peso; entre 18.5 e 25 = peso ideal; 25 ate 30 = sobrepeso; 30 a 40 = obesidade; acima
de 40 = obesidade mórbida.
'''
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso/pow(altura, 2)

if imc < 18.5:
    print('\033[1;32mVocê está abaixo do peso ideal! Se alimente melhor!\033[m')
elif 18.5 <= imc <= 25:
    print('\033[1;34mVocê está no seu peso ideal! Continue assim :)\033[m')
elif 25 < imc <= 30:
    print('\033[1;33mVocê está com sobrepeso! Dê uma maneirada na alimentação!\033[m')
elif 30 < imc <= 40:
    print('\033[1;35mVocê está obeso! Vamos fazer uma reeducação alimentar!\033[m')
elif imc > 40:
    print('\033[4;36mOBESIDADE MÓRBIDA!!! SOS\033[m')
