'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

tamnho_arquivo = float(input('Informe o tamanho de um arquivo para download(em MB):  '))
velocidade = float(input('Informe a velocidade de um link de Internet (em Mbps):  ')) #recebe  em megabit por segundo

donwload = tamnho_arquivo / velocidade

print(f'O tempo aproximado de download do arquivo usando este link em minutos é: {(donwload * 60):.0f} minutos')
