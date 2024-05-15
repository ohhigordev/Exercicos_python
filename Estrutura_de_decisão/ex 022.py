'''
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
Dica: utilize o operador módulo (resto da divisão).
'''

# Pedindo o número ao usuario:
num = int(input('Digite um número: '))

# Verificando se o número digitado é par ou impar:
if num % 2 == 0:
    print('Esse número é par.')
else:
    print('Esse número é impar.')

