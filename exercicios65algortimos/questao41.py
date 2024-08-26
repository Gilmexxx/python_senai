# Arquivo questao41.py

# 41. Crie um programa que peça ao usuário um número inteiro positivo e exiba todos os números de 1 até o número informado.


# Solicita ao usuário para digitar um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if numero > 0:
    # Usa um laço for para exibir todos os números de 1 até o número informado
    for i in range(1, numero + 1):
        print(i)
else:
    print("Por favor, digite um número inteiro positivo.")
