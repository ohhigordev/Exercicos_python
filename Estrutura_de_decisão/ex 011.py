'''
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''
percentual = 0
valor_do_aumento = 0
aumento = 0

# Pedindo para o usuario informa o seu salário:
salario = float(input('Digite o seu salario: R$'))

# Calculando o aumento com base no salário:
# salário de R$ 280.00
if salario <= 280:
    percentual = 20
    aumento = (salario * 20) / 100
    valor_do_aumento = aumento - salario

# salário de R$ 280.00 - 700.00
elif 280 < salario <= 700:
    percentual = 15
    aumento = (salario * 15) / 100
    valor_do_aumento = aumento - salario

# salário de R$ 700.00 - 1.500.00
elif 700 < salario <= 1.500:
    percentual = 10
    aumento = (salario * 10) / 100
    valor_do_aumento = aumento - salario

# salário de R$ 1500.00
elif salario == 1500:
    percentual = 5
    aumento = (salario * 5) / 100
    valor_do_aumento = aumento - salario


print('=== REAJUSTE ===\n')
print(f'Seu salário era de R${salario:.2f}\n')
print(f'O percentual de aumento foi de {percentual}%\n')
print(f'O valor do aumento foi de R${valor_do_aumento:.2f}\n')
print(f'O seu salário atual é de R${aumento:.2f}\n ')
print('====================')


# Programa não está funcionando corretamente!
