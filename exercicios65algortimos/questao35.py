# Arquivo questao35.py


# 35. Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a multiplicação deles é igual a 20.

# Solicita ao usuário para digitar dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Calcula a multiplicação dos números
resultado = numero1 * numero2

# Verifica se o resultado é igual a 20
if resultado == 20:
    print("A multiplicação é igual a 20!")
else:
    print("A multiplicação não é igual a 20.")