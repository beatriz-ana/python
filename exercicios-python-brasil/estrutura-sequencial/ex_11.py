'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. O produto do dobro do primeiro com metade do segundo .
b. A soma do triplo do primeiro com o terceiro.
c. O terceiro elevado ao cubo.'''

numero_1= int(input('Informe um número inteiro: '))
numero_2= int(input('Informe um número inteiro: '))
numero_3= float(input('Informe um número real: '))

print(f'O produto do dobro do primeiro com metade do segundo é: {(numero_1*2) *(numero_2/2)}')

print(f'A soma do triplo do primeiro com o terceiro é: {(numero_1*3) + numero_3}')

print(f'O terceiro elevado ao cubo é: {numero_3**3}')