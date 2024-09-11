# Arquivo questao53.py

# 53. Escreva um programa que peça ao usuário um número e exiba a contagem regressiva desse número até 1.


# Solicita ao usuário para inserir um número
numero = int(input("Insira um número: "))

# Exibe a contagem regressiva do número até 1
# # range(numero, 0, -1): Esta função gera uma sequência de números começando em numero e terminando em 1 (não inclui 0). 
# O terceiro argumento -1 indica que a sequência deve ser gerada em ordem decrescente.

for i in range(numero, 0, -1):
    print(i)