n_tabla = int(input("Introduce el número a multiplicar: "))

for i in reversed(range(5, 16,)):
    if n_tabla * i % 2 == 0:
        print("{} · {} = {}".format(n_tabla, i, n_tabla * i))