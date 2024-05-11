'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 => o produto do dobro do primeiro com metade do segundo .
 => a soma do triplo do primeiro com o terceiro.
 => o terceiro elevado ao cubo.
'''

n_int1 = int(input('Digite um número interio: '))
n_int2 = int(input('Digite outro número intero:'))
n_real = float(input('Digite um número real: '))

# Fazendo as oprações que a questão pede:
a = (n_int1 * 2) + (n_int2 / 2)
b = (n_int1 * 3) + n_real
c = n_real ** 3

# Imprimindo os números:
print(a)
print(b)
print(c)
