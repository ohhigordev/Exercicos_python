'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
'''
# Parametro
limite_de_peso = 50
valor_multa = 4

peso_peixe = float(input('Quantos quilos de peixe marcou: '))

# Calculo do valor da multa se houver excedente.
if peso_peixe > 50:
    excedente = peso_peixe - 50
    multa = excedente * valor_multa
    print(f'Você teve um excedente de {excedente:.1f}kg e deve pagar uma multa de R${multa:.2f} .')

# Se não houver excedente.
else:
    print('Tudo certo senhor, tenha um bom dia!')

