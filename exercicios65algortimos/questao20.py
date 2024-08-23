# Arquivo questao20.py

# 20. Crie um programa que solicite ao usuário a temperatura em graus Celsius e converta para Fahrenheit.

# formula de conversao = (0 °C × 9/5) + 32 = 32 °F


temperaturaCelsius = int(input('Informe a temperatura em graus celsius: \n'))
fahrenheit = (temperaturaCelsius * 9/5) + 32

print(f'A temperatura{temperaturaCelsius} celsius convertidade em fahrenheit é igual a {fahrenheit} ')
