'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
'''

def potencia(base, expoente):
    resultado = 1
    for _ in range(expoente):
        resultado *= base
    return resultado


def main():
    # Solicitar a entrada do usuário para a base e expoente:
    base = int(input('Digite a base: '))
    expoente = int(input('Digite o expoente: '))

    # Calcular a potência utilizando a função definida:
    resultado = potencia(base, expoente)

    # Exibe o resultado:
    print(f'{base} elevado a {expoente} é igual a {resultado}')

if __name__ == '__main__':
    main()





