

# 1. Crie um programa que pergunte ao usuário um número de 1 a 3 e exiba o nome correspondente ao número (1: "um", 2: "dois", 3: "três").


numero = int(input('Informe um numero de 1 a 3: \n'))
if numero == 1:
    print(f'{numero} - Um')
elif numero == 2:
    print(f'{numero} - Dois')
elif numero == 3:
    print(f'{numero} - Três')
else:
    print('Voce nao digitou de 1 a 3, refaça a execucao!')