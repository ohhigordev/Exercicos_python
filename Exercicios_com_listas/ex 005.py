'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.
'''
# Inicializando os vetores:
numeros = []
pares = []
impares = []

# Pedindo os 20 números ao usuário:
for i in range(20):
    numero = int(input(f'Digite o {i + 1} número inteiro: '))
    # Adicionando os números digitados pelo usuário a lista de numeros:
    numeros.append(numero)
    # Verificar se o número é par ou impar e armazenando no vetor correspondente:
    if numero % 2 == 0:
        pares.append(numero)
    
    else:
        impares.append(numero)
    
# Imprimindo os vetores:
print('O vetor de todos os números:', numeros)
print('O vetor dos números pares:', pares)
print('O vetor dos número impares:', impares)







