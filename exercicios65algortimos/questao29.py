# Arquivo questao29.py

# 29. Crie um algoritmo que pergunte ao usuário um número e verifique se ele é múltiplo de 3.

num1 = int(input('Digite um numero: '))

if num1 % 3 == 0:
    print(f'O numero digitado {num1} É MULTIPLO DE 3')
else:
    print(f'O numero digitado {num1} NÃO É MULTIPLO DE 3')