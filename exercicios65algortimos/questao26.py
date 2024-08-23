# Arquivo questao26.py

# 26. Desenvolva um algoritmo que peça ao usuário para inserir dois números e verifique se ambos são múltiplos de 5.

numero = int(input('Insira dois numeros: \n'))

if numero % 5 == 0 :
    print('O numero É multiplo de 5')
else:
    print('O numero NAO É multiplo de 5')