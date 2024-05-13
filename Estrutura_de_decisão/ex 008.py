# Faça um programa que pergunte o preço de três produtos e 
# informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


# Pedindo o preço dos 3 produtos:
produto1 = float(input('Digite o valor do primeiro produto: R$'))
produto2 = float(input('Digite o valor do segundo produto: R$'))
produto3 = float(input('Digite o valor do terceiro produto: R$'))

# Declarando o produto mais barato em uma variavel:
PRODUTO_MAIS_BARATO = produto1

# Descobrindo o produto mais barato:
if produto2 < PRODUTO_MAIS_BARATO:
    PRODUTO_MAIS_BARATO = produto2
elif produto3 < PRODUTO_MAIS_BARATO:
    PRODUTO_MAIS_BARATO = produto3

# Imprimindo o produto mais barato:
print(f'O produto mais barato custa R${PRODUTO_MAIS_BARATO}')



