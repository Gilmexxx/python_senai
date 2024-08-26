

# A função .lower() em Python é usada para converter todos os caracteres de uma string para letras minúsculas. 

# Por exemplo, se você tiver a string "Hello World!", ao aplicar o método .lower(), ela se tornará "hello world!"

'''
#Exemplo 1

nome = 'Lucinao Lopes Ferreira'
nome2 ='luciano lopes ferreira'

if nome.lower() == nome2.lower(): # funcao .lower() 
    pr('Sao iguais')
el
    pr('Nao sao iguais


# A função .upper() em Python é usada para converter todos os caracteres de uma string para letras maisculas. 
# Por exemplo, se você tiver a string "Hello World!", ao aplicar o método .lower(), ela se tornará "HELLO WORLD!"

nome = 'Lucinao Lopes Ferreira'
nome2 ='luciano lopes ferreira'

if nome.upper() == nome2.upper(): # funcao .upper() 
    print('Sao iguais')
else:
    print('Nao sao iguais')

# O método replace() em Python é utilizado para substituir todas as ocorrências de uma substring por outra dentro de uma string. 
# Ele retorna uma nova string com as substituições realizadas
 
 # Exemplo 1 método replace()

texto = "Hello World"
novo_texto = texto.replace("Hello", "Hi")
print(novo_texto)  # Saída: "Hi World"



# Exemplo 2 método replace()

silvano_sales = 'coraçao coracao cabeção'

silvano_sales2 = silvano_sales.reaplce('ç','c')

print(silvano_sales.replace('c','sa'))


# metodo strip() remove caracteres em branco no final e no inicio de uma string

jack_stripador = str(input('digite uma frase com espaços'))

print(jack_stripador.strip())



# metodo splip() divide uma string em elementos de uma lista

string_espalhada = 'Luciano lopes ferreira'

print(string_espalhada)
print(string_espalhada.split())



# exemplo digitando 3 nomes separando com split em elementos de uma lista

digite_nomes = str(input("Digite 3 nomes de pessoas separados por espaço"))

print(digite_nomes)
print(digite_nomes.split())



# metodo .join() transforma os elementos de uma lista em uma string - faz o contrario do motodo .split()
# concatena strings

#exemplo 1
nome_lista = ['Luciano', 'lopes', 'ferreira']

print('')
print(''.join(nome_lista))



# pint (''.join(nomelista)) - entre a aspas'' nao bota espaço para poder unir


nome_lista = ['Luciano', 'lopes', 'ferreira']

dominio = '@gmail.com'

print(''.join(nome_lista)+dominio)



# slice manipla string por indice


cidade = 'Recanto das emas, cidade do povo'

print(cidade[5:]) # o indice começa a imprimir depois do 5º caracter ('do das emas, cidade do povo')



# slice manipla string por indice e diminui posicoes se quiser - inclui os espaços na contagem

cidade = 'Recanto das emas, cidade do povo'

print(cidade[13-1:]) # o indice começa a imprimir depois do 5º caracter ('do das emas, cidade do povo') - inclui os espaços na contagem



# Invertendo a string usando fatiamento (slicing)
    # A notação [::-1] significa que estamos pegando a string inteira (:) e
    # movendo de trás para frente (-1), resultando na string invertida.

nome = "GILMAR SILVA SANTOS"

nome_invertido = nome[::-1]

    # Exibindo o resultado
print(nome_invertido)  # Saída: "sotnaS AVLIS RAMLIG"

'''

# palindormo diz-se de ou frase ou palavra que se pode ler, indiferentemente, da esquerda para a direita ou vice-versa.

palindromo = 'Arara'

if palindromo.lower() == palindromo[::-1].lower():
    print('É palindromo')
else:
    print('Não é palindormo')

    
