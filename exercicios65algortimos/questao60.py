# Arquivo questao60.py

# 60. Crie um programa que peça ao usuário um número e exiba todos os divisores desse número.

# Solicita ao usuário para inserir um número
numero = int(input("Insira um número: "))

# Inicializa uma lista para armazenar os divisores
divisores = []

# Encontra todos os divisores do número
for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

# Exibe os divisores
print("Os divisores de", numero, "são:", divisores)