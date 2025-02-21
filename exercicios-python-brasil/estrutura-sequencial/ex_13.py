'''13)Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

altura = float(input('Informe sua altura:'))

peso_ideal_homem = (72.7*altura) - 58 
peso_ideal_mulher = (62.1*altura) - 44.7

print(f'O peso ideal para essa altura é \nSexo Masculino:{peso_ideal_homem:.2f}\nSexo Feminino: {peso_ideal_mulher:.2f}')
