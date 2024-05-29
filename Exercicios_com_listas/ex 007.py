'''
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
'''
# Primeiro vamos criar um lista onde podemos armazenar os números:
numero = []
soma = []
multiplicação = []

while True:
    # Pedindo os números ao usuário:
    numero1 = int(input(f'Digite o primeiro número interio: '))
    numero2 = int(input(f'Digite o segundo número interio: '))
    numero3 = int(input(f'Digite o terceiro número interio: '))
    numero4 = int(input(f'Digite o quarto número interio: '))
    numero5 = int(input(f'Digite o quinto número interio: '))

    # Agora vamos adicionar os números a nossa lista número:
    numero.append(numero1)
    numero.append(numero2)
    numero.append(numero3)
    numero.append(numero4)
    numero.append(numero5)

    # Vamos fazer a soma dos números e adicionar a nossa lista de soma:
    soma_numeros = numero1 + numero2 + numero3 + numero4 + numero5
    soma.append(soma_numeros)

    # Vamos fazer a multiplicação do números e aidcionar a nossa lista multiplicação:
    multiplicação_numeros = numero1 * numero2 * numero3 * numero4 * numero5
    multiplicação.append(multiplicação_numeros)

    # Agora vamos imprimir a nossas listas:
    print('==== Resultados ====')
    print('Número digitados:', numero)
    print('Multiplicação dos números:', multiplicação)
    print('Soma:', soma)






