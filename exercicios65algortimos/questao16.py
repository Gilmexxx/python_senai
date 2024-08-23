# Arquivo questao16.py

# 16. Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e
#  exiba o preço correspondente por litro.

gasolina = 1
etanol = 2
diesel = 3

combustivel = int(input('Escolha combustivel: 1- gasolina / 2- etanol / 3- diesel'))

if combustivel == 1:
    print(f'O combustivel {'gasolina'} custa hoje R$ 5.89/L')

elif combustivel == 2:
    print(f'O combustivel {'etanol'} custa hoje R$ 4.03/L')

elif combustivel == 3:
    print(f'O combustivel {'diesel'} custa hoje R$ 5.79/L')
else:
    print('Voce nao informou o combustivel valido. Digite novamente!')

