frase = input("Introduce la frase a analizar: ").lower()
vocales = ["a", "e", "i", "o", "u"]
vocales2 = []

for i in frase:
    if i in vocales:
        vocales2.append(i)

print(vocales2)
