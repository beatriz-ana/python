'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

#O upper()método retorna uma string onde todos os caracteres estão em maiúsculas.
letra = input('Informe uma letra: ').upper()

#O isalpha() método retorna True se todos os caracteres forem letras do alfabeto (az)
if letra.isalpha():
    if letra in ('A', 'E','I','O','U'):
        print(f'A letra informada é uma vogal!')
    else:
        print(f'A letra informada é uma consoante!')
else:
    print(f'Não é uma letra!')
    