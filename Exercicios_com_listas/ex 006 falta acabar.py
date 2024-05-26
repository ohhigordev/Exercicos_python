'''
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
'''
# Primeiro vamos criar uma lista particular de notas e medias de cada aluno:

# Aluno 1:
notas_aluno1 = []
media_aluno1 = []

# Aluno 2:
notas_aluno2 = []
media_aluno2 = []

# Aluno 3:
notas_aluno3 = []
media_aluno3 = []

# Aluno 4:
notas_aluno4 = []
media_aluno4 = []

# Aluno 5:
notas_aluno5 = []
media_aluno5 = []

# Aluno 6:
notas_aluno6 = []
media_aluno6 = [list.__format__]

# Aluno 7:
notas_aluno7 = []
media_aluno7 = []

# Aluno 8:
notas_aluno8 = []
media_aluno8 = []

# Aluno 9:
notas_aluno9 = []
media_aluno9 = []

# Aluno 10:
notas_aluno10 = []
media_aluno10 = []

# Vamos criar um loop para pedirmos as notas e calcularmos as medias dos alunos:

# Pedindo as notas ao primeiro aluno:
for i in range(1):
    print('==== Primeiro aluno ====')
    # Pedindo as notas ao usuário:
    nota1 = float(input('Digite a primeira nota:'))
    nota2 = float(input('Digite a segunda nota:'))
    nota3 = float(input('Digite a terceira nota:'))
    nota4 = float(input('Digite a quarta nota:'))

    # calculando a média:
    media = (nota1 + nota2 + nota3 + nota4) / 4

    # Adicionando as notas e as medias as listas:
    notas_aluno1.append(nota1)
    notas_aluno1.append(nota2)
    notas_aluno1.append(nota3)
    notas_aluno1.append(nota4)

    media_aluno1.append(media)

# Pedindo as notas ao segundo aluno:

for i in range(1):
    print('==== Segundo aluno ====')
    # Pedindo as notas ao usuário:
    nota1 = float(input('Digite a primeira nota:'))
    nota2 = float(input('Digite a segunda nota:'))
    nota3 = float(input('Digite a terceira nota:'))
    nota4 = float(input('Digite a quarta nota:'))

    # calculando a média:
    media = (nota1 + nota2 + nota3 + nota4) / 4

    # Adicionando as notas e as medias as listas:
    notas_aluno2.append(nota1)
    notas_aluno2.append(nota2)
    notas_aluno2.append(nota3)
    notas_aluno2.append(nota4)

    media_aluno2.append(media)

print(f'As notas do primeiro aluno são: {notas_aluno1}')
print(f'A média do primeiro aluno é: {media_aluno1}\n')

print(f'As notas do primeiro aluno são: {notas_aluno2}')
print(f'A média do primeiro aluno é: {media_aluno2}\n')

