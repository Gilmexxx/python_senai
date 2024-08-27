# Arquivo questao46.py

# 46. Desenvolva um programa que pergunte ao usuário para inserir 10 números e, ao final, exiba a média dos números inseridos.


# Inicializa a soma dos números
soma = 0

# Solicita ao usuário para inserir 10 números
for i in range(10):
    numero = float(input(f"Digite o número {i+1}: "))
    soma += numero

# Calcula a média dos números
media = soma / 10

# Exibe a média
print(f"A média dos números inseridos é: {media}")