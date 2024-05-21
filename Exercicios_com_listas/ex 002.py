'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''
# Vamos criar uma lista vazia para comportar os 10 números que o usuário ira fornecer:
numero = []

# Aqui criamos um 'for' para pedir ao usuário 10 números interiros: 
for i in range(10):
    numeros = int(input(f'Digite o {i + 1} numero: '))

    # Agora temos que adicionar os números fornecidos pelo usuário a nossa lista vazia:
    numero.append(numeros)

# Vamos exibir os números que estão na nosso lista:
print('O números informados foram: ')

# Só que o detalhe é que temos que exibir os números na ordem inversa usando o fatiamento de listas.
for numeros in numero[::-1]:
    print(numeros, end=' ')





