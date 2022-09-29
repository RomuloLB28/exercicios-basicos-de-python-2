
# leia a temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
#A fórmula de conversão é: F = C*(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius

graus_celsius = float(input("Digite a temperatura em Celsius\n"))

graus_fahrenheit = graus_celsius*(9/5)+32

print(f"o valor da temperatura em Fahrenheit é:{graus_fahrenheit}°F")
