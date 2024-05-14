'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
'''

# Pedindo os lados do triângulo:
l1 = float(input('Digite o primeiro lado do triângulo:'))
l2 = float(input('Digite o segundo lado do triângulo:'))
l3 = float(input('Digite o terceiro lado do triângulo:'))
MAIOR_LADO = l1

# Verificando se os lados digitados formam um triãngulo:
if l2 + l3 < MAIOR_LADO:
    print('Os valores digitados não podem formar um triângulo!')
    print('Tente novamente!')

'''elif l2 < l1 + l3:
    print('Os valores digitados não podem formar um triângulo!')
    print('Tente novamente!')

elif l3 < l1 + l2:
    print('Os valores digitados não podem formar um triângulo!')
    print('Tente novamente!')'''



# Verificando o tipo de triângulo com base nos valores dados pelo úsuario:

# Triângulo Equilatero:
if l1 == l2 == l3:
    triangulo = 'Equilatero'

# Triângulo Isoceles:
elif l1 == l2:
    triangulo = 'Isoceles'

elif l2 == l3:
    triangulo = 'Isoceles'

elif l1 == l3:
    triangulo = 'Isoceles'

# Triângulo Escaleno:

elif l1 != l2 != l3:
    triangulo = 'Escaleno'

# Imprimindo o tipo de triângulo:
print(f'Triangulo {triangulo}.')


