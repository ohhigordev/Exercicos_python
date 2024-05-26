'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''

# Primeiro vamos definir o maior valor, menor valor e a soma dos números:
def analisar_numeros(numeros):
    menor_valor = min(numeros)
    maior_valor = max(numeros)
    soma_valores = sum(numeros)

    # Vamos retornar os valores agora:
    return menor_valor, maior_valor, soma_valores


# Função principal:
def main():
    # Solicitar ao usuário a quantidade de números:
    n = int(input('Digite a quantidade de números: '))

    # Vamos inicializar a lista para armazenas os números:
    numeros = []

    # Agora vamos inicialiar um loop para ler os N números:
    for i in range(n):
        numero = float(input(f'Digite o {i + 1} número: '))
        numeros.append(numero)
    
    # Analisar os números:
    menor, maior, soma = analisar_numeros(numeros)

    # Exibe os resultados:
    print('\n')
    print('==== EXIBINDO RESULTADOS ====')
    print(f'Menor valor: {menor}')
    print(f'Maior valor: {maior}')
    print(f'Soma dos valores: {soma}')
    print('======================')

# Executa a função principal:
if __name__ == '__main__':
    main()






