# Arquivo questao15.py

# 15. Escreva um programa que pergunte ao usuário uma idade e verifique se a pessoa é adolescente (entre 13 e 17 anos).


idade = int(input('Informe sua idade: \n'))

if idade >= 13 and idade <= 17:
    print ('SOU adolescente!')
else:
    print('NAO SOU adolescente!')