# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

graus_fahrenheit = float(input('Qual é a temperatura em graus Fahrenheit: '))
celsius = 5 * ((graus_fahrenheit - 32) / 9)

print(f'Com uma temperatura de {graus_fahrenheit:.1f}°F convetido para celsius fica {celsius:.1f}°C !')
