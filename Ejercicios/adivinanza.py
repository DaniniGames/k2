adivinanza = int(input("Introduce el número a adivinar: "))
intentar = int(input("Qué número es? "))

while intentar != adivinanza:
    intentar = int(input("Qué número es? "))
print("Lo has adivinado.")