# Arquivo questao38.py

# 38. Escreva um programa que peça ao usuário para digitar sua altura em metros e verifique se ela é maior que 1.75.

altura = float(input('Informe sua altura: '))

if altura > 1.75:
    print(f'Minha altura é:',{altura}, 'é maior que 1.75')
else:
    print('Minha altura ',{altura}, 'nao é maior que 1.75')
