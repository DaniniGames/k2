frase = input("Introduce la frase a analizar: ")
mayus = 0

for i in frase:
    if i.isupper():
        mayus += 1

print("La frase tiene {} mayúsculas".format(mayus))