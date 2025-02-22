'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total'''
#Exemplo feito como o enunciado, não usando if/else
print('Bem vindo a nossa loja de tintas!')

area_pintada = float(input('Informe o tamanho em metros quadrados da área a ser pintada: '))

litro = area_pintada / 3
latas = litro/18 

preco = latas * 80

print(f'\nA quantidades de latas de tinta é {latas:.2f} a serem compradas e o preço total é de R${preco:.2f} ')