#leia três valores e apresente como resultado a soma de seus quadrados

valores = []
for i in range(3):
    numero = float(input("Digite um número\n"))
    quadrado = numero**2
    valores.append(quadrado)

soma = 0
for i in range(3):
    soma = soma + valores[i]
print(f"a soma dos quadrados é: {soma}")
#o código pode ser simplificado