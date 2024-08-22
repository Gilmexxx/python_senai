# OPERADORES MATEMATICOS EM PYTHON
# Aula dia 19/08

numero1 = int(input('Digite o primeiro numero inteiro \n'))
numero2 = int(input('Digiti segundo numero inteiro \n'))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

print('A soma dos dois numeros é:', soma)
print('A subtracao dois numeros é:'+ str(subtracao))
print('A multiplicacao dos dois numeros é:`{} e a divisao foi {}'.format(multiplicacao, divisao)) # ou pode fazer a funcao (f'') conforme abaixo
print(f'A multiplicacao é: {multiplicacao} e a dividao foi {divisao}')
