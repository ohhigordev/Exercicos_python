# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ').upper().strip()

if letra == 'A' or 'E' or 'I' or 'O' or 'U':
    print('A letra digitada é uma vogal!')
else:
    print('A letra digitada é uma consoante!')

