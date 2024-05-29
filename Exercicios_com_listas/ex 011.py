# Criando os vetores:
Vetor_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Vetor_b = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Vertor_c = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# Criando uma lista intercalada:
lista_intercalada = []

# Agoras vamos intercalar esses dois vetores:
for elemento1, elemento2, elemento3 in zip(Vetor_a, Vetor_b, Vertor_c):
    lista_intercalada.append(elemento1)
    lista_intercalada.append(elemento2)
    lista_intercalada.append(elemento3)

# Agora vamos exibir a lista intercalada:
print('Lista intercalada:', lista_intercalada)