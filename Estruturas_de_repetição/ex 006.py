'''
Faça um programa que leia 5 números e informe o maior número.
'''
# Pedindo os 5 números ao usuário:
print('Digite 5 números abaixo: ')
num1 = int(input('primeiro número:'))
num2 = int(input('segundo número:'))
num3 = int(input('terceiro número:'))
num4 = int(input('quarto número:'))
num5 = int(input('quinto número:'))

# Escolhenddo um número para ser o maior:
MAIOR_NUMERO = num1

# Verificando qual é o maior número:
if MAIOR_NUMERO < num2:
    MAIOR_NUMERO = num2
if MAIOR_NUMERO < num3:
    MAIOR_NUMERO = num3
if MAIOR_NUMERO < num4:
    MAIOR_NUMERO = num4
if MAIOR_NUMERO < num5:
    MAIOR_NUMERO = num5

# Imprimindo o maior número:
print(f'O maior número é {MAIOR_NUMERO}.')




