# Arquivo questao7.py
# Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if.

nota = int(input('Digite uma nota de 0 a 10: \n'))

if nota >= 0 and nota <= 5:
    print(f'A nota {nota} É BAIXA!')
elif (nota >= 6) and (nota <= 8):
    print(f'A nota {nota} É MEDIA')
elif (nota >= 9) and (nota <= 10):
    print(f'A nota {nota} É MEDIA')
else:
    print('Voce nao digitou valor de 0 a 10. Digite novamente!')