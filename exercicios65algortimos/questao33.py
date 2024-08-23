# Arquivo questao33.py

# 33. Crie um programa que solicite ao usuário o valor de um produto e calcule o desconto de 10%.

# Solicita ao usuário o valor do produto
valor_produto = float(input("Digite o valor do produto: R$ "))

# Calcula o desconto de 10%
desconto = valor_produto * 0.10
valor_com_desconto = valor_produto - desconto

# Exibe o valor do desconto e o valor final com desconto
# A notação :.2f em Python é usada para formatar números de ponto flutuante (floats)
# para que sejam exibidos com duas casas decimais.
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")

