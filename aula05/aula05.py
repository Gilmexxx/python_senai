# APRENDENDO AS CONDICIONAIS

'''
numero1 = 5
numero2 = 3


# OPERADOR MAIOR
    # print(numero1>numero2)
    # print(numero2>numero1)


# OPERADOR MENOR

    # print(numero1<numero2)
    # print(numero2<numero1)

# com o sinal (==) (>=) (<=) (!=) eu faço comparacao de valores
# (==) usado para comparar as variaveis
# (>=) maior ou igual as variaveis
# (<=) menor ou igual as variaveis
# (!=) tira diferença entre as vaiavies

    # print(numero1 == numero2)
    #print(numero1 >= numero2)
    # print(numero1 <= numero2)

idade =  int(input('Informe sua idade: \n'))

if(idade > 120):
    print('Sou maior de idade!')
elif(idade >= 18):
     print('Sou menor de idade \n')
elif(idade < 0):
     print('ainda nao nasceu \n')
else:
     print('Sou menor de idade \n')



# CODIGO1 MUITO LONGO

idade = int(input('Informe sua idade: \n'))

if(idade >= 18):
    print ('Pode assistir o filme')
elif(idade >= 16):
    acompanhado =input('Esta acompanhado de adulto sim ou nao? \n')
    if (acompanhado == 'sim'):
        print('Pode assistir')
    else:
            print('nao pode assistir')
else:
    print('Não pode assitir.')

-----------


# CODIGO 1 MELHORADO TENHO QUE FINALIZAR ESTE CODIGO - lembrar de refazer em casa

idade = int(input('Informe sua idade: \n'))

if(idade < 18):
    print ('Pode assistir o filme')
        acompanhado =input('Esta acompanhado de adulto sim ou nao? \n')
    else (acompanhado == 'sim'):
        print('Pode assistir')
    else:
            print('nao pode assistir')



-------------

# VARIAVEIS DE COMPARACAO FAZENDO EXEMPLO DO ENCONTRO DE ALLADIN COM JASMINE
# E = AND

alladin = input('Alladin apareceu? \n')
jasmine = input('Jasmine apareceu? \n')

if (alladin =='sim') and (jasmine =='sim'):sim
    print('Love a noite inteira')
else:
    print('Nao rolou encontro')



# VARIAVEIS DE COMPARACAO FAZENDO EXEMPLO DO ENCONTRO DE ALLADIN COM JASMINE
# OU = OR

alladin = input('Alladin apareceu? \n')
jasmine = input('Jasmine apareceu? \n')

if (alladin =='sim') or (jasmine =='sim'):
    print('Love a noite inteira')
else:
    print('Nao rolou encontro')

'''
    # VARIAVEIS DE COMPARACAO FAZENDO EXEMPLO DO ENCONTRO DE ALLADIN COM JASMINE
# OU = OR e negando NOT

alladin = input('Alladin apareceu? \n')
jasmine = input('Jasmine apareceu? \n')

if not((alladin =='sim') or (jasmine =='sim')):
    print('Love a noite inteira')
else:
    print('Nao rolou encontro')