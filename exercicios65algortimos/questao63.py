# Arquivo questao63.py

# 63. Desenvolva um algoritmo que peça ao usuário para inserir 5 números, adicione-os a uma lista e, depois, exiba a soma de todos os números na lista.


# Inicializa uma lista vazia para armazenar os números
numeros = []

# Solicita ao usuário para inserir 5 números
for i in range(5):
    numero = int(input("Insira um número: "))
    numeros.append(numero)

# Calcula a soma de todos os números na lista
soma = sum(numeros)

# Exibe a soma de todos os números
print("A soma de todos os números inseridos é:", soma)