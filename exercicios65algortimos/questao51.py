# Arquivo questao51.py

# 51. Crie um programa que peça ao usuário para inserir números até que ele digite o número 0. Ao final, exiba a soma de todos os números inseridos (exceto o 0).


# Inicializa a soma
soma = 0

while True:
    # Solicita ao usuário para inserir um número
    numero = int(input("Insira um número (digite 0 para sair): "))
    
    # Verifica se o número é 0
    if numero == 0:
        break
    
    # Adiciona o número à soma
    soma += numero # Isso é equivalente soma, soma = soma + numero de todos os numeros

# Exibe a soma de todos os números inseridos (exceto o 0)
print("A soma de todos os números inseridos é:", soma)
