# Arquivo questao59.py

# 59. Escreva um programa que solicite ao usuário para digitar dois números e verifique se o primeiro é maior que o segundo. Continue pedindo números até que o primeiro número seja maior que o segundo.

# A estrutura while True: em Python é usada para criar um loop infinito. 
# O loop será executado repetidamente até que uma condição de parada seja encontrada, geralmente usando a instrução (break)

while True: # enquanto a instrucao for verdadeira
    # Solicita ao usuário para inserir dois números
    numero1 = int(input("Insira o primeiro número: "))
    numero2 = int(input("Insira o segundo número: "))
    
    # Verifica se o primeiro número é maior que o segundo
    if numero1 > numero2:
        print("O primeiro número é maior que o segundo. Encerrando o programa.")
        break
    else:
        print("O primeiro número não é maior que o segundo. Tente novamente.")