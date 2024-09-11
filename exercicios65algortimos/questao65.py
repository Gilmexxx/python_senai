# Arquivo questao65.py

# 65. Escreva um programa que solicite ao usuário uma lista de 5 números e exiba o maior e o menor número dessa lista.


# Inicializa uma lista vazia para armazenar os números
numeros = []

# Solicita ao usuário para inserir 5 números
for i in range(5):
    numero = int(input("Insira um número: "))
    numeros.append(numero)

# Encontra o maior e o menor número na lista
maior_numero = max(numeros)
menor_numero = min(numeros)

# Exibe o maior e o menor número
print("O maior número é:", maior_numero)
print("O menor número é:", menor_numero)