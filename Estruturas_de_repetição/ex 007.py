'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
# Pedindo os 5 números ao usuário:
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))
num4 = int(input('Digite o quarto numero: '))
num5 = int(input('Digite o quinto numero: '))

# somando os numero:
soma_dos_numeros = num1 + num2 + num3 + num4 + num5
media_dos_numeros = soma_dos_numeros / 5

# Imprimindo a media e a soma dos números:
print(f'A soma dos números é {soma_dos_numeros} e a media é {media_dos_numeros:.1f}. ')

