# Arquivo questao62.py

# 62. Escreva um programa que solicite ao usuário para inserir 3 nomes e armazene-os em uma lista. Em seguida, imprima a lista completa.

# Inicializa uma lista vazia para armazenar os nomes
nomes = []

# Solicita ao usuário para inserir 3 nomes
for i in range(3):
    nome = input("Insira um nome: ")
    nomes.append(nome)

# Imprime a lista completa de nomes
print("Os nomes inseridos são:", nomes)