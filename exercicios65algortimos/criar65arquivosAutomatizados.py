# Defina o número de arquivos que deseja criar
num_arquivos = 65

# Loop para criar os arquivos

for i in range (1, num_arquivos + 1):
    nome_arquivo = f"questao{i}.py"
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(f"# Arquivo {nome_arquivo}\n")
    print(f"Arquivo {nome_arquivo} criado com sucesso!")

