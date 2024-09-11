# Arquivo questao49.py

# 49. Desenvolva um programa que peça ao usuário para inserir 7 números e, ao final, exiba quantos desses números são maiores que 10.

# Inicializa uma lista vazia para armazenar os números
numeros = []

# Solicita ao usuário que insira 7 números
for i in range(7):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

# Conta quantos números são maiores que 10
contagem_maiores_que_10 = sum(1 for num in numeros if num > 10)

# Exibe a quantidade de números maiores que 10
print(f"Quantidade de números maiores que 10: {contagem_maiores_que_10}")