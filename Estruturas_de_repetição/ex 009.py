'''
Faça um programa que receba dois números inteiros e gere os números 
inteiros que estão no intervalo compreendido por eles
'''

def numeros_no_intervalo (num1, num2):
    # Verificar qual número é o maior:
    inico = min(num1, num2)
    fim = max(num1, num2)


    # Imprimir os números no intervalo:
    print(f'Número no intervalo enre {inico} e {fim}:')
    for numero in range(inico, fim + 1):
        print(numero, end=' ')
    

# Solicitar dois números interios ao usuário;
numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))

# Chamar a função para imprimir o intervalo dos números:
numeros_no_intervalo(numero1, numero2)


