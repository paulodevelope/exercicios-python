'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$'''

salario_hora = float(input('digite o valor da hora trablhada: '))
hora_trabalhada = float(input('Digite o  total de hora trablhada: '))

salario_bruto = salario_hora* hora_trabalhada
print('O Salario Bruto é R$ ', salario_bruto)

print('Descontos:')
ir = salario_bruto * 11 / 100
print('Imposto de renda R$', ir)

inss = salario_bruto * 8 / 100
print('INSS R$', inss)

Sindicato = salario_bruto * 5 / 100
print('Sindicato R$', Sindicato)

salario_liquido = salario_bruto - ir - inss - Sindicato
print('O valor liquido do salario com descontos é R$ ', salario_liquido)

