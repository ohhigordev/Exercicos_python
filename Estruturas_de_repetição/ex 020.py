'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a 
números inteiros positivos e menores que 16.
'''
# Importar a bibioteca FACTORIAL:
from math import factorial

# Vamos criar um While Loop para quer possamos calcular o fatorial várias vezes:
while True:
    num = int(input('Digite um número: '))
    # Vamos criar a condição do programa:
    if 0 < num < 16:
        print(f'O fatorial do número {num} é:', factorial(num))
    else:
        print('O número digitado não obedece as condições do programa.\n')
        break 


