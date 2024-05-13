# Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'{n1} é o maior número.')
elif n2 > n1:
    print(f'{n2} é o maior número.')
elif n1 == n2:
    print(f'Os dois números são iguais! Tente novamente!')
else:
    print('Números invalidos, tente novamente!')
    
