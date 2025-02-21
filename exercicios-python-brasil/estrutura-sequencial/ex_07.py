#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado_quadrado = float(input('Informe o tamanho do lado do quadrado: '))

# area = pi * raio * raio 
area = lado_quadrado * lado_quadrado

print('A dobro da área do quadrado é: ', area * 2)