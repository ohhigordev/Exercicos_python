'''
Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", 
conforme o caso.
'''

print('''Qual turno você estuda:
      [M] - Matutino.
      [V] - Vesperino.
      [N] - Noturno.
''')

# Perguntando ao usuario em que turno ele estuda:
turno = input('Responda aqui qual turno você estuda: ').upper().strip()

# Respondeno ao usuario conforme seu turno:
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')


