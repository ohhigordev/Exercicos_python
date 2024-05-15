'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
'''
from time import sleep
# Criando uma historinha:
print('Você está em um interrogatorio, seram feitas 5 perguntas!')
sleep(1.5)
print('Lembre-se que você não pode mentir...')
sleep(1.5)
podemos_começar = input('Podemos começar? [S/N]').strip().upper()
sleep

# Realizando as perguntas para o usuário:
if podemos_começar == 'S':
    PERGUNTAS_REPONDIDAS_SIM = 0
    PERGUNTAS_REPOSNDIDAS_NAO = 0
    print('Reponda [S/N]')

    # Pergunta 01:
    pergunta1 = input('Você telefonou para a vitima? ').strip().upper()
    if pergunta1 == 'S':
        PERGUNTAS_REPONDIDAS_SIM += 1
    elif pergunta1 == 'N':
        PERGUNTAS_REPOSNDIDAS_NAO += 1
    sleep(2)

    # Pergunta 02:
    pergunta2 = input('Esteve no local do crime? ').strip().upper()
    if pergunta2 == 'S':
        PERGUNTAS_REPONDIDAS_SIM += 1
    elif pergunta1 == 'N':
        PERGUNTAS_REPOSNDIDAS_NAO += 1
    sleep(2)

    # Pergunta 03:
    pergunta3 = input('Mora perto da vitima? ').strip().upper()
    if pergunta3 == 'S':
        PERGUNTAS_REPONDIDAS_SIM += 1
    elif pergunta3 == 'N':
        PERGUNTAS_REPOSNDIDAS_NAO += 1
    sleep(2)

    # Pergunta 04:
    pergunta4 = input('Já trabalhou com a vitima? ').strip().upper()
    if pergunta4 == 'S':
        PERGUNTAS_REPONDIDAS_SIM += 1
    elif pergunta4 == 'N':
        PERGUNTAS_REPOSNDIDAS_NAO += 1   
    sleep(2)

    # Pergunta 05:
    pergunta5 = input('Você devia para a vitima? ').strip().upper()
    if pergunta5 == 'S':
        PERGUNTAS_REPONDIDAS_SIM += 1
    elif pergunta5 == 'N':
        PERGUNTAS_REPOSNDIDAS_NAO += 1   
    sleep(2)


    # verifcando se o usuário é ASSASINO, SUSPEITO, CUMPLICE ou INICENTE.
    if PERGUNTAS_REPONDIDAS_SIM == 5:
        usuario = 'ASSASINO(A)'
    elif 3 <= PERGUNTAS_REPONDIDAS_SIM <= 4:
        usuario = 'CUMPLICE'
    elif PERGUNTAS_REPONDIDAS_SIM == 2:
        usuario = 'SUSPEITO(A)'
    else:
        usuario = 'INOCENTE'

# Imprimindo o resultado:
print('Verificando...')
sleep(2)

print(f'''==== RESULTADO ====
Perguntas respondidas 'S': {PERGUNTAS_REPONDIDAS_SIM}
Perguntas repondidas  'N': {PERGUNTAS_REPOSNDIDAS_NAO}

O usuário é {usuario}!
==============================
''')





