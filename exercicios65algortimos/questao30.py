# Arquivo questao30.py

# 30. Faça um programa que pergunte ao usuário a idade e verifique se ele pode votar (idade maior ou igual a 16).

idade = int(input('Informe sua idade: '))

if idade >= 16:
    print('POSSO VOTAR')
else:
    print('Sou menor de 16  anos, NAO POSSO VOTAR')