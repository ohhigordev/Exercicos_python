'''
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''
# Primeiro vamos inicializar um vetor vazio:
numeros = []

# Depois vamos solicitar ao usuário para inserir 5 números inteiros:
for i in range(5):
    numero = int(input(f'Digite o número {i + 1}: '))

    # Agora vamos fazer com que os números digitados sejam inseridos no nosso vetor vazio:
    numeros.append(numero)

# Exibir os números inseridos:
print('Os números digitados foram:')
for numero in numeros:
    print(numero, end=' ')

