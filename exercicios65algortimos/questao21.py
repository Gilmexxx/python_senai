# Arquivo questao21.py

# 21. Escreva um algoritmo que peça ao usuário para digitar um número e verifique se ele é maior, menor ou igual a 10.


numero1 = int(input('Digite um numero: \n'))

if numero1 > 10:
    print ('O numero É MAIOR QUE 10')
elif numero1 < 10:
    print ('O numero É MENOR QUE 10')
elif numero1 == 10:
    print (F'O numero {numero1} É IGUAL A 10')    
