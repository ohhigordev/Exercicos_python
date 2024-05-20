'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

def analisar_numeros(numeros):
    if not numeros:
        raise ValueError('A lista de números não pode estar vazia')
    
    menor = min(numeros)
    maior = max(numeros)
    soma = sum(numeros)

    return menor, maior, soma

# Exemplo de uso
numeros = [5, 3, 8, 1, 7, 4, 6, 9]
menor, maior, soma = analisar_numeros(numeros)

# Imprimindo os números:
print(f'Menor valor: {menor}')
print(f'Maior valor: {maior}')
print(f'A soma dos valores: {soma}')

'''
Mais aqui o conjunto de números esta predifinido , mas podemos otimizar o programa para pedir os números ao usuário.

'''

def analisar_numeros(numeros):
    if not numeros:
        raise ValueError('A lista de números não pode estar vazia')
    
    menor = min(numeros)
    maior = max(numeros)
    soma = sum(numeros)

    return menor, maior, soma

# Solicitando ao usuário a quantidade de números que ele deseja inserir

try:
    n = int(input("Quantos números você deseja inserir? "))
    if n <= 0:
        raise ValueError("O número de entradas deve ser maior que zero.")

    numeros = []
    for i in range(n):
        numero = float(input(f"Digite o número {i+1}: "))
        numeros.append(numero)

    menor, maior, soma = analisar_numeros(numeros)

    print(f"Menor valor: {menor}")
    print(f"Maior valor: {maior}")
    print(f"Soma dos valores: {soma}")

except ValueError as e:
    print(f"Entrada inválida: {e}")

