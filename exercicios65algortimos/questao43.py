# Arquivo questao43.py

# 43. Desenvolva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e depois use um for para imprimir essa mensagem repetidas vezes.

# Solicita ao usuário para inserir o número de vezes que a mensagem deve ser exibida
quantidade = int(input("Quantas vezes você quer que a mensagem seja exibida? "))

# Solicita ao usuário para inserir a mensagem
mensagem = input("Digite a mensagem que você quer exibir: ")

# Usa um loop for para imprimir a mensagem repetidas vezes
for i in range(quantidade):
    print(mensagem)