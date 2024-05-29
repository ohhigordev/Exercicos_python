'''
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
'''

# Primeiramente vamos criar as listas que vão armazenar os vetores:
idade = []
altura = []

# Agora vamos criar uma range que peça a idade e a altura a um usuário:
for i in range(5):
    # Pedindo os dados ao usuário:
    idades = int(input(f'digite a {i + 1} idade:'))
    alturas = float(input(f'Digite a {i + 1} altura:'))
    
    # Adicionando os dados fornecidos as nossas listas:
    idade.append(idades)
    altura.append(alturas)

# Imprindo os dados:
print('\n Idades e alturas na ordem inversa:')
for i in range(4, -1, -1):
    print(f'Pessoa {i + 1}: Idade: {idade[i]} | Altura: {altura[i]}')
    

