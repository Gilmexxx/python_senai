# Arquivo questao13.py

#13. Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e 
# exiba a estação do ano correspondente.

mes = int(input('Digite o mes do ano de a 1 a 12'))

if mes == 12 or mes == 1 or mes == 2:
    print(f'O mes {mes} a estação é VERAO')
elif mes == 3 or mes == 4 or mes == 5:
    print(f'O mes {mes} a estação é OUTONO')
elif mes == 6 or mes == 7 or mes == 8:
    print(f'O mes {mes} a estação é INVERNO')
elif mes == 9 or mes == 10 or mes == 11:
    print(f'O mes {mes} a estação é PRIMAVERA')
else:
    print('voce nao digitou um mes valido. Digite novamente!')

