'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. 
A saída deve ser conforme o exemplo abaixo:
'''
# Criando um while loop:
while True:
    # Pedindo um número ao usuário:
    numero = int(input('Digite um número e veja sua tabuada de 0 a 10: '))
    # Verificando se o número é maior que 10:
    if numero < 10:
        print(f'==== TABUDA DO {numero} ====')
        print(f'{numero} X 0 = {numero * 0}')
        print(f'{numero} X 1 = {numero * 1}')
        print(f'{numero} X 2 = {numero * 2}')
        print(f'{numero} X 3 = {numero * 3}')
        print(f'{numero} X 4 = {numero * 4}')
        print(f'{numero} X 5 = {numero * 5}')
        print(f'{numero} X 6 = {numero * 6}')
        print(f'{numero} X 7 = {numero * 7}')
        print(f'{numero} X 8 = {numero * 8}')
        print(f'{numero} X 9 = {numero * 9}')
        print(f'{numero} X 10 = {numero * 10}')
        print('=========================')
    else:
        print('O número digitado é maior que 10. Tente novamente!')
