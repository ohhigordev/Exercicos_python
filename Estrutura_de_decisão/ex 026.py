'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser 
pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

from time import sleep

# Perguntando ao usuário qual combustivel ele quer colocar:
print('Olá, bem vido ao posto Rota da Praia!')
sleep(1.5)
print('O senhor(a) gostaria de colocar alcool ou gasolina:')
print('''
===============
[G] - Gasolina
[A] - Alcool
===============
''')
sleep(2)
opcao_combustivel = input('Qual combustivel o senhor(a) escolhe: ').upper().strip()

print('Mostrando descontos...\n')
sleep(2)

# Mostrando os descontos ao usuário depois de ele escolher a gasolina:
if opcao_combustivel == 'G':
    print('''====== DESCONTOS ======
0 - 20L = '4%' de desconto
Mais de 20L = '6%' de desconto
============================
''')
    quantidade_combustivel = int(input('Quando você deseja colocar: \n'))
    print('================================================')
    print('Calculando...')
    sleep(2)

    # Calculando o desconto de 4%:
    if quantidade_combustivel <= 20:
        preço_gasolina = 2.50
        preço_sem_desconto = quantidade_combustivel * preço_gasolina
        desconto = (preço_sem_desconto * 4) / 100
        preço_com_desconto = preço_sem_desconto - desconto
    
    # Calculando o desconto de 6%:
    elif 20 < quantidade_combustivel:
        preço_gasolina = 2.50
        preço_sem_desconto = quantidade_combustivel * preço_gasolina
        desconto = (preço_sem_desconto * 6) / 100
        preço_com_desconto = preço_sem_desconto - desconto

# Mostrando os descontos ao usuário depois de ele escolher o alcool:
elif opcao_combustivel == 'A':
    print('''====== DESCONTOS ======
0 - 20L = '3%' de desconto
Mais de 20L = '5%' de desconto
============================
''')
    quantidade_combustivel = int(input('Quando você deseja colocar: '))

    # Calculando o desconto de 3%:
    if quantidade_combustivel <= 20:
        preço_alcool = 1.90
        preço_sem_desconto = quantidade_combustivel * preço_alcool
        desconto = (preço_sem_desconto * 3) / 100
        preço_com_desconto = preço_sem_desconto - desconto
    
    # Calculando o desconto de 5%:
    if quantidade_combustivel <= 20:
        preço_alcool = 1.90
        preço_sem_desconto = quantidade_combustivel * preço_alcool
        desconto = (preço_sem_desconto * 5) / 100
        preço_com_desconto = preço_sem_desconto - desconto

# Imprimeindo a quantidade de litros abastecidos e quanto o cliente irá pagar.
if opcao_combustivel == 'G':
    print(f'Você abasteceu {quantidade_combustivel}L de gasolina.')
    
    print(f'Você deveria pagar R${preço_sem_desconto:.2f} mas só ira pagar R${preço_com_desconto:.2f} .')

elif opcao_combustivel == 'A':
     print(f'Você abasteceu {quantidade_combustivel}L de alcool.')
     print(f'Você deveria pagar R${preço_sem_desconto:.2f} mas só ira pagar R${preço_com_desconto:.2f} .')   

  


