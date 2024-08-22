# Arquivo questao10.py

# 10. Crie um algoritmo que solicite ao usuário uma idade e verifique se ela é maior ou igual a 18.

idade = int(input('Digite sua idade. \n'))

if idade >= 18:
    print('A idade é IGUAL OU MAIOR que 18 anos')
elif idade < 18:
    print('A idade é MENOR que 18 anos')