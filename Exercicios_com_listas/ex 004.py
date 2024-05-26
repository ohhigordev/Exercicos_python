'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''
# Primeiro vamos definir os 10 caracteres do nosso vetor:
caracteres = ['a', 'd', 'e', 'o', 'z', 's', 'i', 'f', 'g', 'k']

# Lista de vogais que sera feita a verificação:
vogais = ['a', 'e', 'i', 'o', 'u']
# Lista que vai armazenar as consoantes:
consoantes = []
# Contador de consoantes:
contador_consoantes = 0

# Percorrer a lista de caracteres:
for caractere in caracteres:
    # Vamos verificar se o caractere é uma letra e se ele não é uma vogal:
    if caractere.isalpha() and caractere.lower() not in vogais:
        consoantes.append(caractere)
        contador_consoantes += 1
    
# Imprimindo a quantidade de consoantes e as consoantes:
print('O número de consonates foi:', contador_consoantes)
print('Consoantes:', consoantes)




