'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''

hora_de_trabalho_mes = int(input('Quantas horas você trabalha por mês: '))
valor_da_hora_de_trabalho = int(input('Quanto custa sua hora de trabalho: '))

salario_bruto = valor_da_hora_de_trabalho * hora_de_trabalho_mes

if salario_bruto <= 900:
    desconto_ir = 'isento'
    desconto_sindicato = (salario_bruto * 3) / 100
    salario_liquido = salario_bruto - desconto_sindicato
    print(f'Com seu salário de R${salario_bruto:.2f} você está insento do IR e só pagará 3% do imposto do sindicato.')
    print(f'Seu salario liquido será de R${salario_liquido:.2f}. ')

elif 900 < salario_bruto <= 1500:
    desconto_ir = (salario_bruto * 5) / 100
    desconto_sindicato = (salario_bruto * 3) / 100
    salario_liquido = salario_bruto - (desconto_ir + desconto_sindicato)
    print(f'Com seu salário de R${salario_bruto:.2f} você pagará 5% de IR e 3% do imposto do sindicato.')
    print(f'Seu salário liquido será de R${salario_liquido:.2f}')

elif 1500 < salario_bruto <= 2500:
    desconto_ir = (salario_bruto * 10) / 100
    desconto_sindicato = (salario_bruto * 3) / 100
    salario_liquido = salario_bruto - (desconto_ir + desconto_sindicato)
    print(f'Com seu salário de R${salario_bruto:.2f} você pagará 10% de IR e 3% do imposto do sindicato.')
    print(f'Seu salário liquido será de R${salario_liquido:.2f}')

elif 2500 < salario_bruto:
    desconto_ir = (salario_bruto * 20) / 100
    desconto_sindicato = (salario_bruto * 3) / 100
    salario_liquido = salario_bruto - (desconto_ir + desconto_sindicato)
    print(f'Com seu salário de R${salario_bruto:.2f} você pagará 20% de IR e 3% do imposto do sindicato.')
    print(f'Seu salário liquido será de R${salario_liquido:.2f}')

else:
    print('Valor invvalido, tente novamente!')


print('Obrigado, tenha um bom dia!')

