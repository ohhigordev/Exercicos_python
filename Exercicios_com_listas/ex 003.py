'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

# Criando listas vazias que armazenaram as notas:
nota1 = []
nota2 = []
nota3 = []
nota4 = []
media = []

# Pedindo as notas ao usuário:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

# Adicionando as notas as listas:
nota1.append(n1)
nota2.append(n2)
nota3.append(n3)
nota4.append(n4)

# Calculando a media:
m = (n1 + n2 + n3 + n4) / 4
media.append(m)

# Exibindo as notas e a media:
print(nota1, nota2, nota3, nota4)
print(media)

