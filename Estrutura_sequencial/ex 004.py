# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media1 = (nota1 + nota2) / 2
media2 = (nota3 + nota4) / 2
media_final = (media1 + media2) / 2

print(f'A media das quatros notas é igual a {media_final:.2f} .')

