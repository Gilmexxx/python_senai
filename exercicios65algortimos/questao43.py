# Arquivo questao43.py

# 43. Desenvolva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, 
# e depois use um for para imprimir essa mensagem repetidas vezes.

# for i in range() - é usado para iterar sobre uma sequência de números. A função range() gera uma sequência de números, que pode ser usada em um laço for

'''
# Solicita ao usuário para inserir o número de vezes que a mensagem deve ser exibida
quantidade = int(input("Quantas vezes você quer que a mensagem seja exibida? "))

# Solicita ao usuário para inserir a mensagem
mensagem = input("Digite a mensagem que você quer exibir: ")

# Usa um loop for para imprimir a mensagem repetidas vezes recebida de quantidade
for i in range(quantidade):
    print(mensagem)

    
# Exemplo 1     

# gera uma sequência e imprime a quantidade de vezes que o usuario digitar
quantidade = int(input('Quantas vezes voce quer ver a mensagem sendo ixibida? '))

mensagem = input('Digite a mensagem aqui: ')

for i in range(quantidade):
    print(mensagem)


#Exemplo 2 com incremento

# range(5) gera uma sequência de números de 0 a 4 (o 5 não é incluído).
for i in range(5):
    print(i)



# Exemplo 3 com incremento
# range(start, stop): Gera números de start até stop - 1.

for i in range(2, 7): # range(2, 7) gera uma sequência de números de 2 a 6
    print(i)


# Exemplo 4 com incremento
# range(start, stop, step): Gera números de start até stop - 1, com um incremento de step de 2 em 2

for i in range(1, 10, 2):
    print(i)


'''

# Exemplo 5

frase = str(input('Escreva uma frase que ira se repetir: '))

for i in range(2): # aqui ele recebe a frase digitada e repete em laço 2x
    print(frase)