lista = []
input_usuario = input("Lista de la compra. Escribe fin para salir: ")

while input_usuario != "fin":
    lista.append(input_usuario)
    input_usuario = input("Lista de la compra. Escribe fin para salir: ")

for i in lista:
    print("Has de comprar {}.".format(i))