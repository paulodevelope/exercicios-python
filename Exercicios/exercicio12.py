#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
# primeira forma de fazer:
# h = float(input ('Digite a altura da pessoa: '))

#peso_homem = (72.7*h) - 58
#print('Se for do sexo masculino o peso ideal é: ',peso_homem)

#peso_mulher = (62.1*h) - 44.7
#print('Se for so sexo feminino o peso ideal é: ', peso_mulher)


# Utilizando estruturas de controle:

sexo = input('Digite seu sexo: (1)Para homem (2)Para mulher: ')

if sexo == 1:
    aH = input('Digite sua altura: ')
    vH = 72.7 * aH
    rH = vH - 58
    print ('Seu peso ideal é ',rH,'quilos')
elif sexo == 2:
    aM = input('Digite sua altura: ')
    vM = 62.1 * aM
    rM = vM - 44.7
    print ('Seu peso ideal é ',rM,'quilos')


