# Arquivo questao48.py

# 48. Escreva um algoritmo que solicite ao usuário uma palavra e exiba cada letra da palavra em uma linha separada.


# Solicita ao usuário que insira uma palavra
palavra = input("Digite uma palavra: ")

# Exibe cada letra da palavra em uma linha separada
# O código for letra in palavra: é uma estrutura de loop em Python que itera sobre cada caractere (ou letra) de uma string. 
# Portanto, for letra in palavra: significa que o loop for irá iterar sobre cada caractere da string palavra, executando o bloco de código dentro do loop para cada caractere.

for letra in palavra:
    print(letra)