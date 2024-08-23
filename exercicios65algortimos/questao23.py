# Arquivo questao23.py


# lacoes de repeticao 'for = para' 'in = na' usando VETOR - Exemplo 2

# 23. Crie um algoritmo que peça ao usuário uma palavra e verifique se a palavra é "Python".
# funcao .lower() desconsira maisculo ou minusculo da palavra digitada

palavra = str(input('Escreva uma palavra: \n')).lower() # funcao .lower() desconsira maisculo ou minusculo da palavra digitada

if palavra == 'Python'.lower():
    print(f'A palavra digitada {palavra} É Python!')
else:
    print(f'A palavra digitada {palavra} NÃO É Python!')