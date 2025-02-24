#Faça um Programa que peça dois números e imprima o maior deles.
numero_1= int(input('Informe um número:'))
numero_2= int(input('Informe outro número:'))

if numero_1 > numero_2:
    print(f'O número {numero_1} é maior!')
elif numero_1 == numero_2:
    print('Os números são iguais!')
else:
    print(f'O número {numero_2} é maior!')