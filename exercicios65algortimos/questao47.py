# Arquivo questao47.py

# 47. Crie um programa que peça ao usuário um número e exiba a tabuada desse número de 1 a 10.


# Solicita ao usuário que insira um número
numero = int(input("Digite um número: "))

# Exibe a tabuada do número de 1 a 10

print(f"Tabuada de {numero}:")
for i in range(1, 12): # range(1, 11): A função range() gera uma sequência de números começando em 1 e terminando em 10 (o valor final 11 não é incluído).
    print(f"{numero} x {i} = {numero * i}")