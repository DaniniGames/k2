frase_a_convertir = input("Introduce la frase que quieres convertir: ")
aes = ["a", "A"]

for i in frase_a_convertir:
    if i in aes:
        frase_a_convertir = frase_a_convertir.replace(i, "VACA", 1)

print(frase_a_convertir)
