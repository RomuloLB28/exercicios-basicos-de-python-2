#leia quatro notas, calcule a média aritmética e imprima o resultado

#uma lista contendo todas as notas
notas = []
for i in range(4):
    nota = float(input(f"Digite a {i+1}° nota\n"))
    notas.append(nota)

media = sum(notas)/len(notas)
#soma das notas/pelo tamanho da lista contendo as notas, ou seja, pela quantidade de notas

print(f"a média das notas foi:{media}")