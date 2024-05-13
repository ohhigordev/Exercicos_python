# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('digite sua sexualidade: [M/F]').strip().upper()

if sexo == 'M':
    print('sexo MASCULINO!')
elif sexo == 'F':
    print('Sexo FEMININO!')
else:
    print('sexo INVÁLIDO!')
    

