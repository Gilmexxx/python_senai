# Arquivo questao22.py


#22. Escreva um programa que peça ao usuário para inserir dois números e verifique se o primeiro é maior que o segundo.

# Solicita dois números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Verifica se o primeiro número é maior que o segundo
for _ in range(1):  # O loop 'for' é usado aqui apenas para cumprir a solicitação
    if num1 > num2:
        print(f"O primeiro número ({num1}) É MAIOR que o segundo número ({num2}).")
    else:
        print(f"O primeiro número ({num1}) NÃO É MAIOR que o segundo número ({num2}).")