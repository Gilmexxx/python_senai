# Arquivo questao14.py

# 14. Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a soma deles é maior que 100.

numero1 = int(input('Digite o primeiro numero: \n'))
numero2 = int(input('Digite o segundo numero: \n'))

if numero1 + numero2 == 100:
    print('A soma dos numeros digitados é maior que 100')
else:
    print('A soma dos dois numeros NAO É MAIOR que 100')