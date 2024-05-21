'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''
# Função principal:
def main():
    # Primeiro vamos inicializar uma lista vazia para armazenar as notas:
    notas = []

    # Segunda vamos criar um loop para ler as 4 notas:
    for i in range(4):
        # Vamos solicitar as notas para o usuário e converter em floar:
        nota = float(input(f'Digite a nota {i + 1}: '))
        # Agora vamos adicionar as notas a lista vazia:
        notas.append(nota)
    

    # Vamos calcular a média das notas:
    media = sum(notas) / len(notas)

    # Vamos mostrar as notas
    print('\nAs notas digitadas são:')
    for i, nota in enumerate(notas, 1):
        print(f'Nota {i}: {nota}')

    # Mostrando a média das notas:
    print(f'\nA média das notas é: {media:.2f}')

# Chamando a função principal:
if __name__ == '__main__':
    main()





