# Arquivo questao27.py

# 27. Crie um programa que solicite ao usuário três números e exiba o maior deles.

# Solicita três números ao usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Verifica qual é o maior número
if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

# Exibe o maior número
print(f"O maior número é: {maior}")