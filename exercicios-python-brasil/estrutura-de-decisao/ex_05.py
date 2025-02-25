'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; A mensagem "Reprovado", se a média for menor do que sete; A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

nota_1 = float(input('Primeira nota : '))
nota_2 = float(input('Segunda nota : '))

media = (nota_1 + nota_2) / 2
print(f'Sua média é : {media:.1f}')

if media == 10:
    print('Você foi aprovado com Distinção!')
elif media >=7:
    print('Você foi aprovado!')
else:
    print('Você foi reprovado!')
