'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
'''
def contar_digitos(numero):

    # Convertendo para string para facilitar a manipulação dos digitos.
    numero_str = str(numero)

    # Verificando o comprimento da string para facilitar a quantidade de digitos.
    comprimento = len(numero_str)

    # Verificando a quantidade de centenas, dezenas e unidades a partir do seu comprimento:
    if comprimento == 1:
        unidades = numero
        dezenas = 0
        centenas = 0
    
    elif comprimento == 2:
        dezenas = int(numero_str[0])
        unidades = int(numero_str[1])
        centenas = 0
    
    elif comprimento == 3:
        centenas = int(numero_str[0])
        dezenas = int(numero_str[1])
        unidades = int(numero_str[2])

    else:
        print('Resultado invalido! Tente novamente.')

    return centenas, dezenas, unidades
    
# Testando com um número fornecido pelo usuário:
numero_fornecido = int(input('Digite um número inteiro menor que 1000: '))
centenas, dezenas, unidades = contar_digitos(numero_fornecido)
print(f'Centenas: {centenas}, dezenas: {dezenas}, unidades: {unidades}')


