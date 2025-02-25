'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

sexo = input('Informe o sexo  F - Feminino e M - Masculino: ')

if sexo == 'm' or sexo == 'M':
    print(f'O sexo é Masculino')
elif sexo == 'f' or sexo == 'F':
    print(f'O sexo é Feminino')
else:
    print(f'Entrada Inválida!')