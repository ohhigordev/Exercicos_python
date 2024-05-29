'''
Faça um Programa que leia um vetor A com 10 números inteiros, 
calcule e mostre a soma dos quadrados dos elementos do vetor.
'''
# Criando a listas:
vetor_a = []

# Vamos pedir os 10 números ao usuário:
for i in range(10):
    # Pediu os 10 números ao usuário:
    numero = int(input(f'Digite o {i + 1}º número inteiro:'))
    # Adicionando esses números ao vetor_a:
    vetor_a.append(numero)

# Agora vamor calcular a soma dos quadrados:
soma_dos_quadrados = 0
for numero in vetor_a:
    soma_dos_quadrados += numero ** 2

# Imprimindo a soma dos quadrados:
print(f'A soma dos quadrados é:', soma_dos_quadrados)


    




