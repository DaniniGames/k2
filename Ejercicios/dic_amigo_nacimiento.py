años = dict()
salida = False

while not salida:
    accion = input("Deseas añadir un nuevo amigo con su año de nacimiento (a), consultar el año de nacimiento de un amigo (c) o salir (s): ")

    if accion == "a":
        nombre = input("Introduce el nombre del amigo: ")
        año = input("Introduce su año de nacimiento: ")
        años[nombre] = año

    elif accion == "c":
        nombre = input("Introduce el nombre del amigo cuyo año de nacimiento quires consultar: ")
        try:
            print("{} nació en el {}.".format(nombre, años[nombre]))
        except TypeError:
            print("Este amigo no está registrado.")

    elif accion == "s":
        salida = True
