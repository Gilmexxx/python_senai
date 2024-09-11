# Arquivo questao45.py

# 45. Escreva um algoritmo que peça ao usuário para inserir 5 números e, ao final, exiba o maior número inserido.

maior = 0

for i in range (5):
    numero = int(input(f'Informe o numero {i +1}: '))

    if numero > maior:
        maior = numero

print(f'O maior numero é: {maior}')
