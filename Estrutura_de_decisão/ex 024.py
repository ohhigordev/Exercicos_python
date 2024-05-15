'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
'''

# Pedindo os números ao usuário:
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

# Verificando qual operação o usuario deseja realizar:
print("""Qual operação você deseja realizar:
      [S] - somar
      [SU] - subtrair
      [M] - Multipicar 
      [D] - dividir
""")
opcao = input('Digite aqui a sua escolha: ').strip().upper()

# Fazendo a operação escolhida pelo usuário:
if opcao == 'S':
    resultado = num1 + num2
elif opcao == 'SU':
    resultado = num1 - num2
elif opcao == 'M':
    resultado = num1 * num2
elif opcao == 'D':
    resultado = num1 / num2

# Fazendo o restante das verificações:
def verificar_numero_par_ou_impar (resultado):
    if resultado % 2 == 0:
        return 'par'
    else:
        return 'impar'

def verificar_numero_positivo_negativo (resultado):
    if resultado < 0:
        return 'negativo'
    else:
        return 'positivo'

def verificar_tipo_numero (resultado):
    if round(resultado) == resultado:
        return 'inteiro'
    else:
        return 'decimal'

# Chamando as funções:
numero_par_ou_impar = verificar_numero_par_ou_impar(resultado)
numero_positivo_ou_negativo = verificar_numero_positivo_negativo(resultado)
numero_decimal_ou_inteiro = verificar_tipo_numero(resultado)

# imprimindo o número:
print(f'O número {resultado} é {numero_par_ou_impar}, {numero_positivo_ou_negativo}, {numero_decimal_ou_inteiro}.')

