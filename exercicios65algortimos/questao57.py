# Arquivo questao57.py

# 57. Crie um programa que peça ao usuário para adivinhar um número secreto entre 1 e 10. Continue pedindo até que ele adivinhe o número corretamente.


import random

# Gera um número secreto aleatório entre 1 e 10
# random.randint(1, 10): Esta função faz parte do módulo random e gera um número inteiro aleatório entre os valores especificados
numero_secreto = random.randint(1, 10) # neste caso, entre 1 e 10, inclusive.

while True:
    # Solicita ao usuário para adivinhar o número
    palpite = int(input("Adivinhe o número secreto entre 1 e 10: "))
    
    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        print("Parabéns! Você adivinhou o número corretamente.")
        break
    else:
        print("Palpite incorreto. Tente novamente.")