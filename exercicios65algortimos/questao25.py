# Arquivo questao25.py

# 25. Escreva um programa que peça ao usuário um número de 0 a 20 e verifique se ele está entre 10 e 15.

# Solicita um número ao usuário
numero = int(input("Digite um número de 0 a 20: "))

# Verifica se o número está entre 10 e 15
if 10 <= numero <= 15:
    print("O número está entre 10 e 15.")
else:
    print("O número não está entre 10 e 15.")