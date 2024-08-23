# Arquivo questao18.py


# 18. Faça um programa que peça ao usuário três números e verifique se todos são positivos.

numero1 = int(input('Digite o primeiro numero: \n'))
numero2 = int(input('Digite o primeiro numero: \n'))
numero3 = int(input('Digite o primeiro numero: \n'))

if numero1 and numero2 and numero3 > 0:
    print('Todos os numeros sao positivos')
else:
    print('Nem todos os numeros sao positivos')

'''

# Melhorando o codigo 
# a  funçao [.split()] insere os dados separado por um espaço

# Solicita três números ao usuário em uma única linha
numeros = input("Digite três números separados por espaço: ") .split()

# Converte os números para inteiros1
num1, num2, num3 = map(int, numeros)

# Verifica se todos os números são positivos
if num1 > 0 and num2 > 0 and num3 > 0:
    print("Todos os números são positivos.")
else:
    print("Nem todos os números são positivos.")

'''