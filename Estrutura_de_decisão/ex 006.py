# Faça um Programa que leia três números e mostre o maior deles.


# Pedindo os números ao usuario:
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

# Declarando o maior número:
MAIOR_NUMERO = n1

# variaveis:
if n2 > MAIOR_NUMERO:
    MAIOR_NUMERO = n2
elif n3 > MAIOR_NUMERO:
    MAIOR_NUMERO = n3


# Imprimeindo o maior número:
print(f'{MAIOR_NUMERO} é o maior número!')

