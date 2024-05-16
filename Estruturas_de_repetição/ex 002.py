'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações
'''
from time import sleep

while True:
    # Pedir o nome e senha do usuário:
    print('Abaixo pediremos o seu nome e senha, lembrando que elas não podem ser iguais!')
    print('===================\n')
    nome = input('Dgite seu nome: ')
    senha = input('digite sua senha: ')
    print('\n')
    print('===================')

    print('Validando usuário....')
    sleep(2)

    if nome == senha:
        print('ERRO! Seu nome de usuário e sua senha são iguais.')
    else:
        print('Usuário valido!')
        break

print('Programa encerrado.')


