# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês

hora_trabalhada = float(input('Quando você ganha por hora de trabalho: R$'))
Horas_por_mes = int(input('Quantas horas você trabalha por mês: '))

salario = hora_trabalhada * Horas_por_mes

print(f'Com base no que foi informado seu salário é de R${salario:.2f} .')

