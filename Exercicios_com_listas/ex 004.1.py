'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
Só que agora pedindo ao usuário os 10 caracteres.
'''
# Crinado um while loop para automatizar o programa
while True:
    # Criando uma lista de vogais para ser feita a verificação:
    vogais = ['a', 'e', 'i', 'o', 'u']

    # Criando uma lista de consoantes para adicionarmos o que não for vogal:
    consoantes = []

    # Contando as consoantes:
    contador_consoantes = 0

    # Pedir os caracteres ao usuário:
    for i in range(10):
        caratere = input(f'digite a {i + 1} letra:').strip().lower()

        # Aqui estamos veirficando se os caracteres digitados são letras, estão em minusculo e não são vogais:
        if caratere.isalpha() and caratere.lower() not in vogais:
            consoantes.append(caratere)
            contador_consoantes += 1
        
    # Imprindo a quantidade de consoantes e as proprias consoantes:
    print(f'Quantidade de consoantes:', contador_consoantes)
    print(f'Consoantes:', consoantes)





