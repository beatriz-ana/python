'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

sexo = int(input('Escolha: 1- Sexo Masculino / 2- Sexo Feminino: ')) 
altura = float(input('Informe sua altura:'))

peso_ideal = (72.7*altura) - 58 if sexo == 1 else (62.1*altura) - 44.7

if sexo == 1:
    print('Seu peso ideal é: ', peso_ideal)
elif sexo == 2:
    print('Seu peso ideal é: ', peso_ideal)
else:
    print('Entrada inválida!')