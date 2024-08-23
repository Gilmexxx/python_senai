
# Arquivo questao4.py
# 4. Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.

cor = str(input('Informe uma cor de preferencia entre vermelho, verde ou azul: \n')) .lower()

if cor == 'vermelho':
    print (f'{cor}')
elif cor =='verde':
    print (f'{cor}')
elif cor == 'azul':
    print (f'{cor}')
else:
    print ('A cor nao esta entre as informadas. Digite novamente!')
