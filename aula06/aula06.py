# ESTRUTURA METCASE PARA MELHORAR A ESTRUTURA ''ELIF''
# 21/08/2024 - quarta feira

''' # comentado para pode executar o codigo separdo depois de ----

candidato =  int(input('Informe a chapa do candidato: \n'))

if candidato == 13:
    print ('Votou no lula!')
elif candidato == 22:
    print('Votou no bolsonaro')
else:
    print('Candidato invalido')




# o comando 'match' bloco match case é uma estrutura de controle de fluxo que permite comparar 
# uma variável com diferentes valores ou padrões de forma mais organizada e legível do que as tradicionais estruturas if/elif/else

candidato =  int(input('Informe a chapa do candidato: \n'))

match candidato:

    case 13:
        print ('Votou no lula!')
    case 22:
        print('Votou no bolsonaro')
    case _:
        print('Candidato invalido')


# ATRIBUICAO DE VALORES A UMA VARIAVEL INCREMENTANDO VALOR A VALOR

numero = 10
print (numero)

numero = numero + 10
print (numero)

numero =  numero - 10
print (numero)



# REATRIBUICAO DE VALORES A UMA VARIAVEL INCREMENTANDO VALOR USANDO (+=)(-=)(*=) (/=)

numero = 10 
print (numero)

numero += 10 # encrementa somando por 10
print (numero)

numero -= 10 # encrementa diminuindo por 10
print (numero)

numero /= 10 # encrementa dividindo por 10
print (numero)

numero *= 10 # encrementa multiplicando por 10
print (numero)



# VERIFICANDO SE UM NUMERO É PAR OU IMPAR USANDO (%) MODE

numero = int(input('Informe o numero: \n'))

if numero % 2 == 0: # se a divisao de um numero o resto for '0' entao vai dar par
    print('numero é par')
else:
    print('numero é impar')




# LAÇOS DE REPETIÇÃO

for i in range(5):
    print(i)



# lacoes de repeticao 'for = para' 'in = na' usando VETOR - Exemplo 1

nomes = ['Gilmar','Ana', 'Edivan', 'Gilvan']

for nome in nomes:
    print(nome)


# lacoes de repeticao 'for = para' 'in = na' usando VETOR - Exemplo 2

frutas = ['bana', maça', 'morango', 'laranja']

for item in frutas:
    print(item)



# lacoes de repeticao 'for = para' 'in = na' usando INDICE (nada mais é que pegar posicao do iten na lista. 
# Lembre-se que a lista começa com 0

frutas = ['bana', 'maça', 'morango', 'laranja']
print (frutas[2])


# for indice, fruta in enumerate(frutas)
# print(f'Suas grutas sao {indice:}{frutas})

frutas = ['bana', 'maça', 'morango', 'laranja']

for indice, fruta in enumerate(frutas):
    print(f'Suas frutas sao {indice}:{fruta}')




# for indice, fruta in enumerate(frutas)
# print(f'Suas grutas sao {indice:}{frutas})

nomes = []

for i in range(5):
    nome = input('Informe o seu nome \n')
    nomes .append(nome)

for nome in nomes:
    print(nome)



# laço 'WHILE' em portugues 'ENQUANTO'


numero = None

while numero != 0:
    numero = int(input('Informe o numero: '))


# LAÇO DE REPTICAO WHILE


contador =1
numero = int(input('Informe o numero: '))

while contador < 10
    print(numero * 2)
    contador +=1


'''

numero = 10
while True:
    numero *= 10
    print(numero)
    if numero > 12:
        break