'''15)Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

salario_por_hora = float(input('Informe quanto você ganha por hora: '))
horas_trabalhadas = float(input('Quantas horas você trabalhou?'))

salario_bruto = salario_por_hora * horas_trabalhadas

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - ir - inss - sindicato

print(f'\nSalario bruto: R${salario_bruto:.2f} \nIR(11%):R${ir:.2f} \nINSS(8%): R${inss:.2f} \nSindicato(5%): R${sindicato:.2f} \nSalario Líquido: R${salario_liquido:.2f}')