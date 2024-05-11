'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
Altura = float(input('Digite sua altura: '))
sexualidade = input('Digite seu genero sexual: [M/F]').strip().upper()

# Calculando peso ideal masculino.
if sexualidade == 'M':
    peso_ideal = (72.7 * Altura) - 58
    print(f'Com base na sua altura de {Altura:.2f} m seu peso ideal é de {peso_ideal:.1f}')

# Calculando peso ideal feminino.
elif sexualidade == 'F':
    peso_ideal = (62.1 * Altura) - 44.7
    print(f'Com base na sua altura de {Altura:.2f} m seu peso ideal é de {peso_ideal:.1f}')
else:
    print('Valor invalido, tente novamente!')


