#leia um ângulo em radianos e apresente-o convertido em graus

radianos = float(input("Digite o valor do ângulo em radianos\n"))

graus = radianos*(180/3.14)

print(f"O valor do ângulo em graus é: {round(graus)}°")