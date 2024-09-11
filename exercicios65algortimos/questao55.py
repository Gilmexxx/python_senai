# Arquivo questao55.py


# 55. Desenvolva um programa que peça ao usuário para inserir um número maior que 100. Se o número for menor ou igual a 100, continue pedindo até que um número maior que 100 seja inserido.

while True:
    # Solicita ao usuário para inserir um número
    numero = int(input("Insira um número maior que 100: "))
    
    # Verifica se o número é maior que 100
    if numero > 100:
        print("Número maior que 100 inserido. Encerrando o programa.")
        break
    else:
        print("Número menor ou igual a 100. Tente novamente.")