#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.


temperatura_fahrenheit = float(input('Informe a temperatura em graus Fahrenheit: '))
temperatura_celsius =  ((temperatura_fahrenheit-32) / 9) * 5

print(f'{temperatura_fahrenheit} graus Fahrenheit é igual a {temperatura_celsius} em gruas Celsius')