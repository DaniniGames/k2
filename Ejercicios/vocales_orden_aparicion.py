frase_a_cambiar = input("Introduce el texto a modificar: ").lower()
vocales = ["a", "e", "i", "o", "u"]
aparicion = 0

for i in frase_a_cambiar:
    if i in vocales:
        aparicion += 1
        frase_a_cambiar = frase_a_cambiar.replace(i, str(aparicion), 1)

print(frase_a_cambiar)