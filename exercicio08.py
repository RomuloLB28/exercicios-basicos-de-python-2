
#Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. 
#A fórmula de conversão é: C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.

graus_kelvin = float(input("Digite a temperatura em em Kelvin\n"))
graus_celsius = graus_kelvin - 273.15

print(f"a temperatura em Celsius é:{graus_celsius}°C")


