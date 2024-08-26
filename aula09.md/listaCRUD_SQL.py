
# princiapis dados de insercao de dados


cavaleiros = ['Seya', 'Shun', 'Aldebarcam','Aldebarcam','Shiryu', 'Yoga', 'Aldebarcam']
print(cavaleiros) # pra listar é o print - seria equivalente ao select no banco de dados

# a funcao .append() adiciona um (somente 1) novo elemento no final da lista
cavaleiros.append ('Ikki') 
print (cavaleiros)


# a funcao .extend() adiciona vareios (mais de 1) novos elemento no final usando uma lista
cavaleiros.extend(['shina', 'marin'])  
print(cavaleiros)


cavaleiros.insert(0, 'Athena')
print(cavaleiros)

# inserindo na lista em uma posicao especifica que é no inicio 3 da lista 
# lembre que a lista inicia no 0
cavaleiros.insert(3, 'Gilmar')
print(cavaleiros)

#---------------

# remove, exclui um elemento pelo valor na primeiro ocorrencia da lista apenas
cavaleiros.remove('Shun')
print(cavaleiros)

# pop exclui o ultimo elemento da lista ou indice informado
cavaleiros.pop()
print(cavaleiros)

# pop exclui o ultimo elemento da lista ou indice informado e me fala qual foi o nome excluido
cavaleiros.pop()
elemento = cavaleiros.pop()
print(elemento)
print(cavaleiros)


# .pop() exclui o ultimo elemento da lista ou indice informado 
cavaleiros.pop()
elemento = cavaleiros.pop(2)
print(cavaleiros)
print(elemento)

# indice - retona o indice da primeira ocorrencia de um valor procurado procurando elementos usando indice
print(cavaleiros.index('Shiryu'))
print(cavaleiros)

# alterando valor de um elemento da lista
cavaleiros[cavaleiros.index('Athena')] = 'Deusa de Athena'
print(cavaleiros)

# contabilizando quantidade de elementos repetidos
print(cavaleiros.count("Aldebarcam"))




