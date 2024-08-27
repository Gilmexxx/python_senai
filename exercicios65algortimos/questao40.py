# Arquivo questao40.py

# 40. Escreva um programa que peça ao usuário para inserir três números e verifique se todos são iguais.


# Solicita ao usuário para inserir três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Verifica se todos os números são iguais
if num1 == num2 == num3:
    print("Todos os números são iguais.")
else:
    print("Os números não são iguais.")
