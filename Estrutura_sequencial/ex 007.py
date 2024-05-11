# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

base = float(input('Digite o tamanho da base do quadrado: '))
altura = float(input('Digite o tamanho da altura do quadrado: '))

area_quadrado = base * altura
dobro = area_quadrado * 2

print(f'A área do quadrado mede {area_quadrado:.1f} cm² e seu dobro mede {dobro:.1f}cm² .')

