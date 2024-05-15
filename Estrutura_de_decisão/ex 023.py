'''
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento
'''
def verificar_tipo_numero(numero):
    if round(numero) == numero:
        return 'inteiro'
    else:
        return 'decimal'


# Solicita ao usuário um número:
numero = float(input('Digite um número: '))

# Verifica e informa se o número é inteiro ou decimal:
tipo = verificar_tipo_numero(numero)
print(f'O número {numero} é {tipo}.')

