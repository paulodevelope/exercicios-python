'''Faça um programa que peça o tamanho de um arquivo para download 
(em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

tamanho = float(input('Digite o tamnho do arquivo MB: '))
velocidade = float(input('Digite a velocidade do link: '))

download = tamanho / velocidade * 60
print('O tempo aproximado de download em minutos é: ', download)
