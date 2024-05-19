'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números 
pares e a quantidade de números impares.
'''

# Inicializando contadores para números pares e impares:
numero_pares = 0
numeros_impares = 0

# Pedindo 10 números inteiros:
for i in range(10):
    numero = int(input(f'Digite o {i + 1}º número inteiro: '))

    # Verificando se o números é par ou ímpar:
    if numero % 2 == 0:
        numero_pares += 1
    else:
        numeros_impares += 1
    
# Mostrando os resultados:
print('Quantidade de números pares:', numero_pares)
print('Quantidade de números impares:', numeros_impares)

    



