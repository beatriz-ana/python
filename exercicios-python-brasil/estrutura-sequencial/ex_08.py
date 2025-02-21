#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
salario_por_hora = float(input('Informe quanto você ganha por hora: '))
horas_trabalhadas = float(input('Quantas horas você trabalhou?'))

salario_total = salario_por_hora * horas_trabalhadas

print('O salário desse mês sera: ', salario_total)