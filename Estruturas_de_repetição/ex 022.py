'''
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, 
por quais número ele é divisível.
'''
# Primeiro vamos solicitar ao usuário um número inteiro:
num = int(input('Digite um número: '))

# Agora vamos verificar se o número é primo:
if num <= 1:
    print(f'O número {num} não é primo.')

else:
    divisores = []
    for i in range(1, num + 1):
        if num % 1 == 0:
            divisores.append(i)


    if len(divisores) == 2:
        print(f'O número {num} é primo.')
    else:
        print(f'O número {num} não é um numero primo.')
        print(f'Ele é divisivel por: {divisores}')
        


