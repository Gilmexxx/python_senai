# Arquivo questao36.py

<<<<<<< HEAD
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

=======

# 36. Crie um programa que solicite ao usuário um número de 1 a 12 e exiba o mês correspondente.

# Solicita ao usuário para digitar um número de 1 a 12
numero_mes = int(input("Digite um número inteiro entre 1 e 12: "))

# Verifica se o número está dentro do intervalo válido
if 1 <= numero_mes <= 12:
    # Lista com os nomes dos meses
    meses = ["Janeiro", "Fevereiro", "Março", "Abril","Maio", "Junho", "Julho", "Agosto","Setembro", "Outubro", "Novembro", "Dezembro"]
    # Exibe o mês correspondente
    print(f"O mês correspondente ao número {numero_mes} é {meses[numero_mes-1]}.")
else:
    print("Número inválido. Digite um valor entre 1 e 12.")


# {numero_mes} é substituído pelo valor da variável numero_mes.
# {meses[numero_mes - 1]} é substituído pelo nome do mês correspondente ao número inserido pelo usuário.
>>>>>>> 0d1d1e0f453dc26a7c592e612638e0de1ad11600
