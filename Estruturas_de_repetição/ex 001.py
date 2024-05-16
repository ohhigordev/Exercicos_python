'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor 
seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
# Criando o while True para fazer um ciclo infinito:
while True:
    nota = float(input('Dgite uma nota de 0 a 10: '))
    # Criando a condição de uma nota valide:
    if 0 <= nota and nota <= 10:
        print('Nota valida:', nota)
        break # Usando o break para sair do while loop já que a nota é valida!

    # Criando a condição se a nota não for validae
    else:
        print('Nota invalida! Por favor, digite uma nota entre zero e dez.')

