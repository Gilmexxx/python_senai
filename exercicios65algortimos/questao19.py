# Arquivo questao19.py

# 19. Escreva um algoritmo que peça ao usuário o nome de uma fruta e verifique se a fruta é uma maçã.

# a funcao .lower() nao é usado pra nao fazer distincao de como os caracteres sao escritos

fruta = str(input('Digite o nome de uma fruta: \n')) .lower()

if fruta == str('maça'):
    print(f'A fruta informada É MAÇA!')
else:
    print(f'A fruta informada NAO É MAÇA!')

