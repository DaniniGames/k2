lista_strings = ["Hola", "Maribel", "cómo", "estás?"]
lista_caracteres = []

for i in lista_strings:
    lista_caracteres.append(len(i))
print (lista_caracteres)

lista_numeros = [1, 3.4, 5, 6.7, 3, 2]
multiplicacion = 1

for i in lista_numeros:
    multiplicacion *= i
print(multiplicacion)

lista_mixta = ["Mc", "Tomcet", "Mcarrons", 3, 6, "Bel esportiva", 5, "Rodup", 8, "Deporte", "Ejercicio bélico", 1450]
lista_enteros = []
lista_strings_1 = []

for i in lista_mixta:
    if type(i) == str:
        lista_strings_1.append(i)
    else:
        lista_enteros.append(i)

print(lista_strings_1)
print(lista_enteros)