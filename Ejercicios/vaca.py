frase_a_convertir = input("Introduce la frase que quieres convertir: ")
vocales = ["a", "e", "i", "o", "u"]

for i in frase_a_convertir:
    if i == "A" or i == "a":
        frase_a_convertir = frase_a_convertir.replace(i, "VACA", 1)

print(frase_a_convertir)
