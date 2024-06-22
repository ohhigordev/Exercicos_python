def main():
    # Lista para armazenar idades e altura:
    idades = []
    alturas = []

    # Recebendo a idade dos 30 alunos:
    for i in range(30):
        idade = int(input(f'Digite a idade do {i + 1} aluno: '))
        altura = float(input(f'Digite a altura do {i + 1} aluno: '))
        idades.append(idade)
        alturas.append(altura)
    
    # Cálculo da média da altura dos alunos com mais de 13 anos
    soma_alturas = 0
    qtd_alunos = 0
    
    for i in range(30):
        if idades[i] > 13:
            soma_alturas += alturas[i]
            qtd_alunos += 1

    if qtd_alunos > 0:
        media_alturas = soma_alturas / qtd_alunos
    else:
        media_alturas = 0

    # Contagem de alunos inferior à média:
    qtd_alunos_inferior_media = 0

    for i in range(30):
        if idades[i] > 13 and alturas [i] < media_alturas:
            qtd_alunos_inferior_media += 1
        
    # Exbindo resultados:
    print(f'Quantidade de alunos com mais de 13 anos e com altura inferior à média: {qtd_alunos_inferior_media}')

if __name__ == '__main__':
    main()