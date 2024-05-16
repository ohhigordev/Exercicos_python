'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.
'''
# Vamos definir uma função para calcular os anos com base na população e na taxa de crescimento.
def calcular_anos(populacao_a, taxa_a, populacao_b, taxa_b):
    anos = 0
    # fazendo um while loop enquando a população_a for menor que a população_b:
    while populacao_a <= populacao_b:
        populacao_a *= 1 + taxa_a / 100
        populacao_b *= 1 + taxa_b / 100
        anos += 1
    return anos

# Pedindo ao usuário que ele informe a população e a taxa de crecimento:
populacao_a = int(input('Quantos habitantes tem na cidade A:'))
taxa_a = float(input('Qual a taxa de crescimento da cidade A: '))
populacao_b = int(input('Quantos habitantes tem na cidade B: '))
taxa_b = float(input('Qual a taxa de crescimento da cidade B: '))

anos_necessarios = calcular_anos(populacao_a, taxa_a, populacao_b, taxa_b)
print(f'Serão necessários {anos_necessarios} anos para que a população do pais A ultrapasse a do pais B.')