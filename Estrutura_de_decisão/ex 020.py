'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''
# Pedindo as notas ao aluno:
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

# Vericando a media do aluno:
media = (nota1 + nota2 + nota3) / 3

# Determiando as codições:
if media == 10:
    resultado = 'APROVADO COM DISTINÇÃO'
elif 7 < media < 10:
    resultado = 'APROVADO'
elif media < 7:
    resultado = 'REPROVADO'


# Revelando o resultado:
print('==============================\n')
print(f'Com uma media de {media:.1f}')
print(f'Resultado: {resultado}\n')
print('==============================')
