'''14) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.'''

LIMITE = 50

peso_peixes = float(input("Informe o peso de peixes:"))

if peso_peixes> LIMITE:

    excesso_peso = peso_peixes - LIMITE
    multa = excesso_peso * 4.00
    print(f'O peso de peixes informado foi {peso_peixes}kg, {excesso_peso}kg a mais que o estabelecido pelo regulamento e isso gerou uma multa de R${multa:.2f}')
     
else:
    print(f'O peso de peixes informado foi {peso_peixes}Kg de peixes, está dentro do limite estabelecido pelo regulamento')