def num_mayor(x, y, z):
    if x > y and x > z:
        salida = x
    elif y > x and y > z:
        salida = y
    else:
        salida = z
    return salida


print(num_mayor(180, 991, 60))
print(num_mayor(18, 92, 54))
print(num_mayor(1, 94, 13))


def numero_en_rango(x, y, z):
    if y <= x <= z:
        return True
    else:
        return False


print(numero_en_rango(31, 32, 184))
print(numero_en_rango(50, 32, 48))
print(numero_en_rango(31, 24, 184))


def pares(lista):
    pares_lista = []
    for i in lista:
        if i % 2 == 0:
            pares_lista.append(i)
    return pares_lista


print(pares(lista=[1, 2, 3, 4, 8, 9, 26, 31, 86]))