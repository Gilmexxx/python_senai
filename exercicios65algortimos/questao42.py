# Arquivo questao42.py

# 42. Escreva um algoritmo que solicite ao usuário 5 números inteiros e calcule a soma desses números.

# Inicializa a soma
soma = 0

# Solicita ao usuário para digitar 5 números inteiros
for i in range(5):
    numero = int(input(f"Digite o número {i + 1}: "))
    soma += numero

# Exibe a soma dos números
print(f"A soma dos números é: {soma}")

