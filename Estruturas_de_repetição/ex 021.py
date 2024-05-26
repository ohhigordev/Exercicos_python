'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

# Primeiro vamos solictar ao usuário um número inteiro:
num = int(input('Digite um número: '))

# Agora vamos verificar se esse número é primo:
if num <= 1:
    print(f'O número {num} não é primo.') # Um número não pode ser negativo ou nulo e primo ao mesmo tempo.
elif num == 2:
    print(f'O número {num} é primo.') # 2 é o único número par que é primo.
elif num % 2 == 0:
    print(f'O número{num} não é primo.') # Se um número for par e maior do que 2 ele não é primo.

else:
    eh_primo = True
    for i in range(3, int(num**0.5) + 1, 2): # Esse loop foi usado para verificar a divisibilidade de número impares maiores que 2.
        if num % i == 0:
            eh_primo = False
            break
    
    if eh_primo:
        print(f'O número {num} é primo.')
    else:
        print(f'O número {num} não é primo.')


