# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

print('Digite uma data: aa/mm/aaaa')
dia = int(input('Digite um dia: '))
mes = int(input('Digite um mês: '))
ano = int(input('Digite um ano: '))

if 31 < dia:
    print('Dia digitado invalido! Tente novamente.')
elif 12 < mes:
    print('O mês digitado é invalido! Tente novamente.')
elif ano < 0:
    print('Ano digitado invalida! Tente novamente.')

else:
    print(f'{dia}/{mes}/{ano}')


