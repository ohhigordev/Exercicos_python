# Faça um Programa que leia três números e mostre o maior e o menor deles.

# Pedindo 3 números ao usuario:
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite mais um número: '))

# Declarando o maior e o menor número:
MAIOR_NUMERO = n1
MENOR_NUMERO = n3

# Descobrindo o maior número:
if n2 > MAIOR_NUMERO:
    MAIOR_NUMERO = n2
elif n3 > MAIOR_NUMERO:
    MAIOR_NUMERO = n3

# Descobrindo o menor número:
if n2 < MENOR_NUMERO:
    MENOR_NUMERO = n2
elif n1 < MENOR_NUMERO:
    MENOR_NUMERO = n1

print(f'O maior número é igual a {MAIOR_NUMERO}.')
print(f'O menor número é igual a {MENOR_NUMERO}')

