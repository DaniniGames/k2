numeros = []
numero_usuario = ""

numeros_analisis = input("Introduce la cantidad de números que quieres analizar: ")
while not numeros_analisis.isdigit():
    numeros_analisis = input("Debes introducir un número: ")

while len(numeros) < int(numeros_analisis):
    while not numero_usuario.isdigit():
        numero_usuario = input("Introduce un número:  ")
    numeros.append(int(numero_usuario))
    numero_usuario = ""
    print("Número añadido")

numero_peke = numeros[0]
largo_lista = 0
media = 0

for i in numeros:
    if i < numero_peke:
        numero_peke = i
for i in numeros:
    largo_lista += 1
for i in numeros:
    media += i
print("El número más pequeño es {}, has introducido {} números y la media es de {}.".format(numero_peke, largo_lista, media / largo_lista))