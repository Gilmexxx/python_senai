# Arquivo questao65.py

nomes = []

operacao = 'sim'

while operacao == 'sim':
    print('Informe acao desejada: ')
    print('1 cadastre nome: ')
    print('2 Atualize nome: ')
    print('3 Exclua nome: ')
    print('4 Lista nome: ')

    opcao = int(input('Informe a acao desejada:' ))

    match opcao:
        case 1:
            nome = input('que nome a acao deseja')
            nomes.append(nome)
        case 2:
            nome = input('Infome o novo nome: ')
            novo_nome = input('Qual sera o novo nome? ')
            nomes[nomes.index(nome)] = novo_nome
        case 3:
            nome = input('Que nome deseja remover? ')
            nomes.remove(nome)
        case 4:
            for indice, nome in enumerate(nomes):
                print(f'{indice} - {nome}')
        case _:
            print("Opcao invalida!")

    operacao = input('Deseja realizar outra operacao? ').lower()

    if operacao == 'nao':
        break

    print(nome)