# Arquivo questao52.py

# 52. Desenvolva um algoritmo que solicite ao usuário uma senha e continue pedindo até que a senha correta "1234" seja digitada.

# Define a senha correta
senha_correta = "1234"


# while True: é útil quando você deseja que um bloco de código seja executado repetidamente até que uma condição específica seja atendida.
while True:
    # Solicita ao usuário para inserir uma senha
    senha = input("Insira a senha: ")
    
    # Verifica se a senha está correta
    if senha == senha_correta:
        print("Senha correta!")
        break # (break) interrompe o loop
    else:
        print("Senha incorreta. Tente novamente.")
