elegir_poke = input("Quieres combatir contra Squirtle, Charmander o Bulbasaur? ")

vida_pikachu = 100
vida_enemigo = 0
ataque = 0
nombre_poke = 0

if elegir_poke == "Squirtle":
    vida_enemigo = 90
    nombre_poke = "Squirtle"
    ataque = 11

elif elegir_poke == "Charmander":
    vida_enemigo = 80
    nombre_poke = "Charmander"
    ataque = 12

elif elegir_poke == "Bulbasaur":
    vida_enemigo = 100
    nombre_poke = "Bulbasaur"
    ataque = 10

while vida_pikachu > 0 and vida_enemigo > 0:
    elegir_ataque = input("Usar chispazo o bola voltio?")

    if elegir_ataque == "Chispazo":
        vida_enemigo -= 10
    elif elegir_ataque == "Bola voltio":
        vida_enemigo -= 12

    print("La vida de {} es de {}.".format(nombre_poke, vida_enemigo))

    vida_pikachu -= ataque
    print("{} te ha quitado  de vida.".format(nombre_poke, ataque))

    print("Tu vida es de {}.".format(vida_pikachu))

if vida_enemigo <= 0:
    print("Has ganado.")

elif vida_pikachu <= 0:
    print("Has perdido.")

print("El combate ha finalizado.")