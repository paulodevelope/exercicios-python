# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

num_int1 = int(input('Digite o primeiro numero inteiro: '))
num_int2 = int(input('Digite o segundo  numero inteiro: '))
num_real1 = float(input('Digite o terceiro numero real: '))

r1 =  num_int1 * 2 + (num_int2/2)
print('O produto do dobro do primeiro com metade do segundo é : ', r1)

r2 = num_int1 * 3 + num_real1
print('A soma do triplo do primeiro com o terceiro é: ', r2)

r3 = num_real1 ** 3
print(' O terceiro elevado ao cubo é: ', r3)

