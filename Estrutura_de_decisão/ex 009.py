# Faça um Programa que leia três números e mostre-os em ordem decrescente.


# Perguntando os números ao usuario:
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite mais um número:'))

# Declarando as constantes:
MAIOR_NUMERO = n1
NUMERO_DO_MEIO = n2
MENOR_NUMERO = n3

# Declarando o maior número:
if n2 > MAIOR_NUMERO:
    MAIOR_NUMERO = n2
elif n3 > MAIOR_NUMERO:
    MAIOR_NUMERO = n3

# Declarando o número do meio:
if n1 <= NUMERO_DO_MEIO:
    NUMERO_DO_MEIO = n1
elif n3 <= NUMERO_DO_MEIO:
    NUMERO_DO_MEIO = n3

# Declarando o menor número:
if n1 < MENOR_NUMERO:
    MENOR_NUMERO = n1
elif n2 < MENOR_NUMERO:
    MENOR_NUMERO = n2

# Imprimindo os números em ordem decrescente:
print(MAIOR_NUMERO, NUMERO_DO_MEIO, MENOR_NUMERO)



