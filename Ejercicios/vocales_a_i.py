frase_a_cambiar = input("Mc ").lower()
vocales = ["a", "e", "i", "o", "u"]

for i in frase_a_cambiar:
    if i in vocales:
        frase_a_cambiar = frase_a_cambiar.replace(i, "i", 1)

print(frase_a_cambiar)