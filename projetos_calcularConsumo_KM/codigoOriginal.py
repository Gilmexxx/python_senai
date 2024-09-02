def calcular_valor_corrida(distancia_km, consumo_km_por_litro, preco_combustivel_por_litro):
    # Calcula o custo do combustível para a distância dada
    litros_necessarios = distancia_km / consumo_km_por_litro
    custo_combustivel = litros_necessarios * preco_combustivel_por_litro

    # Calcula o valor mínimo da corrida (custo do combustível)
    valor_minimo_corrida = custo_combustivel

    # Calcula o valor para ganhar 100% além do custo
    valor_com_lucro = valor_minimo_corrida * 2

    return valor_minimo_corrida, valor_com_lucro


# Exemplo de uso
distancia_km = 50  # Distância da corrida em km
consumo_km_por_litro = 10  # Consumo do carro em km/l
preco_combustivel_por_litro = 5.0  # Preço do combustível por litro em reais

valor_minimo, valor_com_lucro = calcular_valor_corrida(
    distancia_km, consumo_km_por_litro, preco_combustivel_por_litro)

print(f"Valor mínimo da corrida: R$ {valor_minimo:.2f}")
print(f"Valor da corrida com 100% de lucro: R$ {valor_com_lucro:.2f}")
