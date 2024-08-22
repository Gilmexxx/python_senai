# Arquivo questao5.py
# 5. Faça um programa que solicite ao usuário dois números e verifique se ambos são pares.

numero1 = int(input('Digite o PRIMEIRO NUMERO: \n'))
numero2 = int(input('Digite o SEGUNDO NUMERO: \n'))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print(f'O número {numero1} É PAR!')
elif numero2 % 2 == 0:
    print(f'O numero {numero2} É PAR!')
else:
    print(f'O numero {numero1} É IMPAR!') or print(f'O numero {numero2} É IMPAR')

