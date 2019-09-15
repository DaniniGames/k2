frase = input("Introduce la frase a analizar: ")
comas = 0
espacios = 0
puntos = 0

for i in frase:
    if i == ",":
        comas += 1
    elif i ==  " ":
        espacios += 1
    elif i ==  ".":
        puntos += 1

print("Tu frase tiene {} comas, {} espacios y {} puntos.".format(comas, espacios, puntos))