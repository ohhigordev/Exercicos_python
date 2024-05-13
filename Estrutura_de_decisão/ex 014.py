'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
O algoritmo deve mostrar na tela as notas, a média, 
o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou 
“REPROVADO” se o conceito for D ou E.
'''

# Perguntando as notas ao aluno:
nome = input('Digite seu nome completo:')
nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))

# Calculando a media do aluno:
media = (nota1 + nota2) / 2

# Verificando se o aluno esta aprovado ou não:
if 9.0 < media <= 10.0:
    nota_final = 'A'
    resultado = 'APROVADO'
elif 7.5 < media <= 9.0:
    nota_final = 'B'
    resultado = 'APROVADO'
elif 6.0 < media <= 7.5:
    nota_final = 'C'
    resultado = 'APROVADO'
elif 4.0 < media <= 6.0:
    nota_final = 'D'
    resultado = 'REPROVADO'
elif 0 < media <= 4.0:
    nota_final = 'E'
    resultado = 'REPROVADO'

print('===== RESULTADO =====')
print(f'Nome do aluno:{nome}\n')
print(f'Sua media:     {media:.2f}')
print(f'Nota final:    {nota_final}')
print(f'Resultado:     {resultado}')
print('=======================')



