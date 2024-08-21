# 3. Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) e exiba o nome do dia correspondente.


dia = int(input('Digite o dia da semana de 1 a 7: \n'))

if dia == 1:
    print(f'{dia} - Segunda-feira')
elif dia == 2:
    print(f'{dia} - Terça-feira')
elif dia == 3:
    print(f'{dia} - Quarta-feira')
elif dia == 4:
    print(f'{dia} - Quinta-feira')
elif dia == 5:
    print(f'{dia} - Sexta-feira')
elif dia == 6:
    print(f'{dia} - Sabado')
elif dia == 7:
    print(f'{dia} - Domingo')
else:
    print('Voce NAO digitou de 1 a 7. Refaça!')