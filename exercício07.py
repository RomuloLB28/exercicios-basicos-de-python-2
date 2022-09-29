#leia uma temperatura em graus fahrenheit e apresente-a convertida em graus Celsius. A fórmula de conversão é: C = 5*(F-32)/9
#Sendo C a temperatura em Celsius e F a temperatura em Fahrenheit

graus_fahrenheit = float(input("Digite a temperatura de Fahrenheit\n"))
graus_celsius = 5*(graus_fahrenheit-32)/9

print(f"o valor da temperatura em Celsius é: {graus_celsius}°C")


