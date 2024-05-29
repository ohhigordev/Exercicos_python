'''
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, 
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
'''
# Criando os vetores:
Vetor_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Vetor_b = ['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']

# Criando uma lista intercalada:
lista_intercalada = []

# Agoras vamos intercalar esses dois vetores:
for elemento1, elemento2 in zip(Vetor_a, Vetor_b):
    lista_intercalada.append(elemento1)
    lista_intercalada.append(elemento2)

# Agora vamos exibir a lista intercalada:
print('Lista intercalada:', lista_intercalada)

