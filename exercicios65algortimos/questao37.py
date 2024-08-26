
# Arquivo questao37.py
# 36. Crie um programa que solicite ao usuário um número de 1 a 12 e exiba o mês correspondente.

# Solicita ao usuário para digitar um número de 1 a 12
numero_mes = int(input('Digite um mes de 1 a 12: '))

# Verifica se o número está dentro do intervalo válido
if 1 <= numero_mes <= 12:
   # Lista com os nomes dos meses
   meses = ["Janeiro", "Fevereiro","Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
   # Exiba o mes correspondente
   print(f'O mes digitado corresponde ao {numero_mes} é o {meses[numero_mes-1]}.')
else:
    print('Número inválido. Digite um valor entre 1 e 12.')
    
# {numero_mes} é substituído pelo valor da variável numero_mes.
# {meses[numero_mes - 1]} é substituído pelo nome do mês correspondente ao número inserido pelo usuário.