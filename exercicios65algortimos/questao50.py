# Arquivo questao50.py

# 50. Crie um programa que peça ao usuário para inserir um número e, em seguida, exiba os números de 1 até esse número, mas de forma decrescente.


# Solicita ao usuário para inserir um número
numero = int(input("Insira um número: "))

# Exibe os números de 1 até o número inserido, de forma decrescente
# range(numero, 0, -1): Esta função gera uma sequência de números começando em numero e terminando em 1 (não inclui 0). 
# O terceiro argumento -1 indica que a sequência deve ser gerada em ordem decrescente.

for i in range(numero, 0, -1):
    print(i)