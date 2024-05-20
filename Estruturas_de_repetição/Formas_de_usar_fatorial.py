# Como calcular o fatorial de um número em Python:
'''
Temos 3 formas de fzer isso que seram apresentadas abaixo:
'''
# Função Iterativa: com o uso do 'for':

def fatorial_iterativo(n):
    if n < 0:
        raise ValueError('O fatorial não está sendo definido para números negativos!')
    
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= 1
    return fatorial

# Exemplo de uso:
print(fatorial_iterativo(5)) # Saída: 120

# Função recursiva:

def fatorial_recursivo(n):
    if n < 0:
        raise ValueError('O fatorial não está difinido para números negativos!')
    
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * fatorial_recursivo(n - 1)
    
# Exemplo de uso
print(fatorial_recursivo(5)) # Saida: 120

# Usando a biblioteca 'math':

import math

# Exemplo de uso:
print(math.factorial(5)) # Saída: 120





