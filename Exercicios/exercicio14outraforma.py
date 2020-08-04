salario_hora = float(input('digite o valor da hora trablhada: '))
hora_trabalhada = float(input('Digite o  total de hora trablhada: '))

salario_bruto = salario_hora * hora_trabalhada
print('O Salario Bruto é R$ ', salario_bruto)

ir = salario_bruto * 11 / 100
inss = salario_bruto * 8 / 100
sindicato = salario_bruto * 5 / 100

print('Descontos de imposto de renda R$', ir)
print('Descontos de INSS R$', inss)
print('Descontos de sindicato R$', sindicato)
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos
print('O salario liquido com descontos ir, inss, sindicato R$', salario_liquido)
