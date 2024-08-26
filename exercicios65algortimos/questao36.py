# Arquivo questao36.py

# 36. Crie um programa que solicite ao usuário um número de 1 a 12 e exiba o mês correspondente.

# Lista de meses do ano
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

# Solicita ao usuário para digitar um número de 1 a 12
numero = int(input("Digite um número de 1 a 12: "))

# Verifica se o número está no intervalo válido
if 1 <= numero <= 12:
    # Exibe o mês correspondente
    print(f"O mês correspondente é {meses[numero - 1]}.")
else:
    # Exibe uma mensagem de erro se o número não for válido
    print("Número inválido. Por favor, digite um número de 1 a 12.")

