# Arquivo questao54.py

# 54. Crie um algoritmo que solicite ao usuário um número e continue pedindo outro número até que um número negativo seja inserido.

while True:
    # Solicita ao usuário para inserir um número
    numero = int(input("Insira um número (digite um número negativo para sair): "))
    
    # Verifica se o número é negativo
    if numero < 0:
        print("Número negativo inserido. Encerrando o programa.")
        break
    else:
        print("Você inseriu o número:", numero)