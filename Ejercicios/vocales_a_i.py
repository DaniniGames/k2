frase_a_cambiar = input("Introduce la frase a modificar: ").lower()
vocales = ["a", "e", "i", "o", "u"]

for i in frase_a_cambiar:
    if i in vocales:
        frase_a_cambiar = frase_a_cambiar.replace(i, "i", 1)

print(frase_a_cambiar)