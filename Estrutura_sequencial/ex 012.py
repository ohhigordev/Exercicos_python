# Tendo como dados de entrada a altura de uma pessoa,
#  construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Digite a sua altura: '))
peso_ideal = (72.7 * altura) - 58

print(f'Com uma altura de {altura:.2f}m seu peso ideal seria de {peso_ideal:.1f}kg .')

