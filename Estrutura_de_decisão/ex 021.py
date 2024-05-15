'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois 
informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas 
existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
'''

def caixa_eletronico(saque):
    if saque < 10 or saque > 600:
        print("Valor de saque inválido. O valor mínimo é de 10 reais e o máximo é de 600 reais.")
        return
    
    notas = [100, 50, 10, 5, 1]
    quantidade_notas = [0, 0, 0, 0, 0]

    for i in range(len(notas)):
        quantidade_notas[i] = saque // notas[i]
        saque -= quantidade_notas[i] * notas[i]

    print("Notas fornecidas:")
    for i in range(len(notas)):
        if quantidade_notas[i] > 0:
            print(f"{quantidade_notas[i]} nota(s) de {notas[i]} reais")

# Solicita ao usuário o valor do saque
saque = int(input("Digite o valor do saque (entre 10 e 600 reais): "))
caixa_eletronico(saque)



