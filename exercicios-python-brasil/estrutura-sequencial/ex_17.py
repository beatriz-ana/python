'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
  comprar apenas latas de 18 litros;
  comprar apenas galões de 3,6 litros;
  misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''
import math
#math.ceil sempre arredonda para cima, pois não podemos comprar meia lata, somente latas inteiras.
litro_latas = 18
preco_latas = 80
litro_galoes = 3.6 
preco_galoes = 25


print('Bem vindo a nossa loja de tintas!')
area_pintada = float(input('Informe o tamanho em metros quadrados da área a ser pintada: '))
qtd_litros_necessarios = area_pintada / 6

#Apenas latas
qtd_latas = math.ceil(qtd_litros_necessarios / litro_latas)
custo_latas = qtd_latas * preco_latas
print('\nSomente latas de 18 litros:')
print(f'O cliente precisa comprar {qtd_latas} latas, que custarão R${custo_latas}.')

#Apenas galões
qtd_galoes = math.ceil(qtd_litros_necessarios / litro_galoes)
custo_galoes = qtd_galoes * preco_galoes
print('\nSomente Galões de 3,6 litros:')
print(f'O cliente precisa comprar {qtd_galoes} latas, que custarão R${custo_galoes}.')

#Misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga
litros_necessarios_folga = qtd_litros_necessarios * 1.1 

qtd_latas_mix = litros_necessarios_folga // litro_latas #quantidade de litros 
litros_necessarios_folga_faltando = litros_necessarios_folga - (qtd_latas_mix * litro_latas)
qtd_galoes_mix = math.ceil(litros_necessarios_folga_faltando / litro_galoes)

custo_mix = (qtd_latas_mix * preco_latas) + (qtd_galoes_mix* preco_galoes)

print("\nMix de latas e galões:")
print(f'O cliente precisa comprar {qtd_latas_mix} latas e {qtd_galoes_mix} galões, que custarão {custo_mix}')

 