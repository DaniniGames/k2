adivinanza = 3
intentos = 5

while intentos > 0:

    user_num = int(input("Adivina el número. Tienes {} intentos: ".format(intentos)))

    if user_num == adivinanza:
     print("Has ganado.")
     break
    elif intentos == 1 and user_num != adivinanza:
        print("Has perdido.")
    else:
        intentos -= 1
        print ("Te quedan {} intentos.".format(intentos))


