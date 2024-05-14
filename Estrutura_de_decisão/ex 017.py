# Feito com auxilio do ChatGPT!!!

'''
Faça um Programa que peça um número correspondente a um determinado ano e em seguida 
informe se este ano é ou não bissexto.
'''

# Definindo a regra do ano bissexto:
def eh_bissexto(ano):
    # Um ano é bissexto se ele for divisivel por 4.
    # Exceto quando ele é divisil por 100, a menos que ele também seja divisil por 400.
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


def main():
    ano = int(input('Digite um ano: '))

    if eh_bissexto(ano):
        print(f'O ano {ano} é bissexto!')
    
    else:
        print(f'O ano {ano} não é bissexto!')

if __name__ == '__main__':
    main()

