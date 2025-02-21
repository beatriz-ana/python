#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print('Vamos informar sua média, para isso precisamos que informe suas notas.')
nota_1 = int(input('Primeira nota : '))
nota_2 = int(input('Segunda nota : '))
nota_3 = int(input('Terceira nota : '))
nota_4 = int(input('Quarta nota : '))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print(f'Sua média é : {media}')
