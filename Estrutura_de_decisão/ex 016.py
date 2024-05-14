'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, 
informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir 
os demais valores, sendo encerrado;
Se o delta calculado for negativo,  Informe ao usuário e encerre o pa equação não possui raizes reais.rograma;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

'''
from time import sleep

# Pedindo ao usuário os valores de a, b e c:
a = int(input('Digite o valor de [a]: '))
b = int(input('Digite o valor de [b]: '))
c = int(input('Digite o valor de [c]: '))

if a == 0:
    print('O valor de [a] não pode ser 0 pois isso caracteriza uma equação de primeiro grau!')
    print('Tente novamente!')

else:
        
    # Imprimindo a equação do segundo grau
    print('Escrevendo...')
    sleep(1)
    print(f'f(x) = {a}x² + {b}x + {c}')
    print('Vamos denominar o valor de f(x) = 0 deixando a função dessa forma:\n')
    sleep(2)
    print(f'{a}x² + {b}x + {c} = 0')

    # calculando o delta:
    delta = (b**2) - 4 * a * c

    # Propriedades do delta:
    if delta < 0:
        print('O delta informado tem valor negativo! Por tanto não possui raizes reais')
        print('Tente novamente!')

    if delta == 0:
        print('O delta informado é nulo! Por tanto só possui uma raiz real.')

    if 0 < delta:
        print('O delta informado é positivo! Sendo assim o programa possui duas raizes reais.')


print('Programa encerrado!')