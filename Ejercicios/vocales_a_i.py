frase_a_cambiar = input("Introduce la frase a modificar: ").lower()
vocales = ["a", "e", "o", "u"]
tildes = ["á", "é", "ó", "ú"]

for i in frase_a_cambiar:
    if i in vocales:
        frase_a_cambiar = frase_a_cambiar.replace(i, "i", 10)
    elif i in tildes:
        frase_a_cambiar = frase_a_cambiar.replace(i, "í", 10)

print(frase_a_cambiar)