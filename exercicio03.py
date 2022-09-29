#peça ao usuário que digite 3 números e imprima a soma deles

soma = 0
for i in range(3):
    num = float(input("digite um número\n"))
    soma += num

print(f"a soma dos valores digitados foi:{soma}")

