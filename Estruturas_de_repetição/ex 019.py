'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
'''
# Função para obter o menor, maior e soma dos valores
def analisar_numeros(numeros):
    menor_valor = min(numeros)
    maior_valor = max(numeros)
    soma_valores = sum(numeros)
    return menor_valor, maior_valor, soma_valores

# Função principal
def main():
    # Solicita ao usuário a quantidade de números
    n = int(input("Digite a quantidade de números: "))
    
    # Inicializa a lista para armazenar os números
    numeros = []
    
    # Loop para ler os N números
    for i in range(n):
        # Aqui o programa fará a verificação se os valores estão dentro dos limites infinitamente:
        while True:
            numero = float(input(f"Digite o {i+1} número (entre 0 e 1000): "))

            # Fazendo a verificação:
            if 0 <= numero <= 1000:
                numeros.append(numero)
                break # Se os números dados pelo usuário forem satisfatorial ele para o While Loop!
            else:
                print("Número fora do intervalo permitido. Tente novamente.")
                # Se os números não forem satisfatorios ele pedirá ao usuário novos números até que a condição do programa seja atendida!
    
    # Analisa os números
    menor, maior, soma = analisar_numeros(numeros)
    
    # Exibe os resultados
    print(f"Menor valor: {menor}")
    print(f"Maior valor: {maior}")
    print(f"Soma dos valores: {soma}")

# Executa a função principal
if __name__ == "__main__":
    main()



