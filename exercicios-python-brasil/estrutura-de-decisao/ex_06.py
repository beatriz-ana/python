'''Faça um Programa que leia três números e mostre o maior deles.'''

numero_1= int(input('Informe um número:'))
numero_2= int(input('Informe outro número:'))
numero_3= int(input('Informe outro número:'))

maior = numero_1

if (numero_2 > maior):
    maior = numero_2
if (numero_3 > maior):
    maior = numero_3

print(f'O numero {maior} é maior!')