# funcoes
# max() informa o maior numero de uma lista
# min() informa o menor numero de uma lista
# len() conta quantos elementos tem
# sum() faz a soma de todo os elementos
# 'def' é usada para definir uma função e depois tenho quem mandar escrever ela para aparecer
# lambda() é usada para criar funções anônimas, ou seja, funções sem nome que são definidas em uma única linha. Elas são úteis quando você precisa de uma função simples e rápida, que será usada apenas uma vez ou passada como argumento para outras funções, como map(), filter() e sorted()
# // duas barras faz divisao absoluta

# () parenteses representa uma TUPLA
# {} chaves representa um DICIONARIO
# [] representa uma lista

# numero1 = int(input('Informe o primeiro numero'))
# numero2 = int(input('Informe o segundo numero'))



numeros = [1,5,8,10,3,78,100,51]
print(max(numeros)) # max() informa o maior numero de uma lista
print(min(numeros)) # min() informa o menor numero de uma lista
print(len(numeros)) # len() conta quantos elementos tem
print(sum(numeros)) # sum() faz a soma de todo os elementos


# Existe uma função em Python para calcular a média! Você pode usar a 
#   função mean() da biblioteca statistics ou calcular manualmente usando as funções sum() e len()

# Exemplo 1 retornando media
media = sum(numeros) / len(numeros) # faz uma soma sum() e divide pelo numero dos elementos len()
print(media)


# Exemplo 2 com def

def media (numeros): # 'def' é usada para definir uma função
    resultado = sum(numeros) / len(numeros)
    return resultado

resposta = media(numeros)

print(resposta)



# Exemplo 3 com def ja informando 2 numeros a e b

# defina a funcao soma
def soma(num1, num2):
    soma = (num1 + num2)
    return soma

# uso da funcao soma
print(soma(2,35))



# Exemplo 4 com def sem retorno

# defina a funcao saudacao
def saudacao(nome):
    print(f'Ola {nome}')
    
# uso da funcao saudacao
saudacao('Gilmar') # nome ja recebendo o nome 'Luciano'



# Exemplo 5 com def ja ternando nome e mensagem na funcao

from subprocess import REALTIME_PRIORITY_CLASS


def ola(nome, mensagem="Olá"):
    print(mensagem, nome)

ola('Luciano') # aqui chamou a funcao mensagem "Ola"
ola('Luciano','Oi') # aqui eu informei nome e mensagem como alternativa a "ola"



# Exemplo 6 com def com multiplo retorno


def dividir(num1, num2):
    resposta = num1 // num2
    resto =  num1 % num2
    return resposta, resto 

divisao, resto_divisao = dividir(9,2)

print(divisao)
print(resto_divisao)




# Exemplo 7 funcao lambda()

somar = lambda num1, num2: num1 + num2 # funcao lambda cria na linha a funcao soma de dois numeros
print(somar(10,5))



# Exemplo 7 parametro posicional sao os nao nomeado

def exibir_informacoes(*parametros): # '*' tem que ta colado com o nome que pode ser qualquer coisa a depender da ideia de uso por padrao usaom *args
    print('Argumentos posicionais', parametros)

exibir_informacoes(1,4, 'Luciano', 'Teste')




# Exemplo 8 parametro com argumento nomeado

def exibir_informacoes(**parametros): # '**' com multimplso argumentos
    print('Argumentos posicionais', parametros)

exibir_informacoes(nome= 'Luciano', idade= 30, curso='python')

# Exemplo 9 - dicionario da variavel (pessoa) com suas keys: 'nome, idade, estado_civil, escolaridade' com seus respectivos 'valores' value()
# key : value
# chave : valor

pessoa = {
    'nome':'Gilmar', #
    'idade': 30,
    'estado_civil': 'casado',
    'escolaridade': 'Pos Graduado'
},

pessoa2 = {
    'nome':'Daniel', #
    'idade': 19,
    'estado_civil': 'noivo',
    'escolaridade': 'Superior'
}

print(pessoa)
print(pessoa2)


'''

# Exemplo 10 - dicionario da variavel (pessoa) com suas keys: 'nome, idade, estado_civil, escolaridade' com seus respectivos 'valores' value()
# key : value
# chave : valor
# Neste exemplo temos 2 dicionarios{} de pessoa dentro de uma LISTA[]



pessoa = [{
    'nome':'Gilmar', #
    'idade': 30,
    'estado_civil': 'casado',
    'escolaridade': 'Pos Graduado'
},

{
    'nome':'Daniel', #
    'idade': 19,
    'estado_civil': 'noivo',
    'escolaridade': 'Superior'
}]

print(pessoa[0]) # Lembre que lista começa com posicao 0 = primeiro da lista do dicionario 

