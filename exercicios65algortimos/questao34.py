# Arquivo questao34.py

# 34. Escreva um programa que peça ao usuário um número e verifique se ele é positivo, negativo ou zero.


num1 = int(input('Escreva um numero: '))

if num1 == 0:
    print('O numero é igual a ZERO')

elif num1 >= 0:
    print('O numero é POSITIVO')
elif num1 <= 0:
    print('O numero é NEGATIVO')
