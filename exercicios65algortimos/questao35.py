# Arquivo questao35.py

# 35. Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a multiplicação deles é igual a 20.

numero = int(input('Digite o primeiro numero'))
numero2 = int(input('Digite o  segundo numero'))

multiplicao = numero * numero2

if multiplicao == 20:
    print('A multiplicacao dos dois numero é IGUAL A 20')
else:
    print("A multiplicacao dos dosi numeros NAO É IGUAL 20")