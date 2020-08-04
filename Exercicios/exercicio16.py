'''Faça um Programa para uma loja de tintas.
 O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
 Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e 
 que a tinta é vendida em latas de 18 litros,
 que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

metros = float(input('Digite a o tamanho da area a ser pintada em metros:'))

litros = metros/6
latas = 18
galoes = 3.6

quantidade_latas = litros * latas
print('a quantiddade de latas a ser usadas é: ', quantidade_latas)
valor_latas = quantidade_latas * 80
print('O valor se  opção latas R$ ' ,valor_latas )

quantidade_galoes = quantidade_latas * galoes
print('A quantidade se a opção for galões é: ', quantidade_galoes)
valor_galoes = quantidade_galoes * 25
print('O valor se opção for galões R$', valor_galoes)



