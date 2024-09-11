# Arquivo questao58.py

# 58. Desenvolva um algoritmo que solicite ao usuário uma palavra e continue pedindo outra palavra até que ele digite "sair".

# Inicializa uma lista vazia
nomes = []

while True:
    # Solicita ao usuário para inserir um nome
    nome = input("Insira um nome (digite 'sair' para encerrar): ")
    
    # Verifica se a palavra é "sair"
    if nome.lower() == "sair":
        break
        
    # Adiciona o nome à lista
    nomes.append(nome)
    
# Imprime os nomes inseridos
    print(f'Os nomes inseridos são:{nomes}')
    

