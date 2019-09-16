lista = [2, 4, 7, 70, 80, 23, 54]

multiplos_dos = []
multiplos_tres = []
multiplos_cinco = []
multiplos_siete = []

for i in lista:
    if i % 2 == 0:
        multiplos_dos.append(i)
    if i % 3 == 0:
        multiplos_tres.append(i)
    if i % 5 == 0:
        multiplos_cinco.append(i)
    if i % 7 == 0:
        multiplos_siete.append(i)

print("Múltiplos de 2: {}".format(multiplos_dos))
print("Múltiplos de 3: {}".format(multiplos_tres))
print("Múltiplos de 5: {}".format(multiplos_cinco))
print("Múltiplos de 7: {}".format(multiplos_siete))