# Arquivo questao44.py


# 44. Crie um programa que peça ao usuário 10 números e exiba apenas os números pares.

# Inicializa uma lista vazia para armazenar os números
numeros = []

# Solicita ao usuário que insira 10 números
for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

# Filtra e exibe apenas os números pares
numeros_pares = [num for num in numeros if num % 2 == 0]

print("Números pares:", numeros_pares)

