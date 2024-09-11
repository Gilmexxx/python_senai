# Arquivo questao56.py

# 56. Escreva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, e utilize um laço while para exibir a mensagem a quantidade de vezes desejada.

# Solicita ao usuário para inserir a quantidade de vezes que a mensagem deve ser exibida
quantidade = int(input("Quantas vezes você quer que a mensagem seja exibida? "))

# Inicializa um contador
contador = 0

# Usa um laço while para exibir a mensagem a quantidade de vezes desejada
while contador < quantidade:
    print("Esta é a mensagem.")
    contador += 1