# Arquivo questao64.py


# 64. Crie uma lista com 10 números aleatórios e exiba apenas os números que são múltiplos de 3.

import random

# Cria uma lista com 10 números aleatórios entre 1 e 20
numeros = [random.randint(1, 20) for _ in range(10)]

# Filtra os números que são múltiplos de 3
multiplos_de_3 = [num for num in numeros if num % 3 == 0]

# Exibe a lista completa de números
print("Lista completa de números:", numeros)

# Exibe os números que são múltiplos de 3
print("Números que são múltiplos de 3:", multiplos_de_3)