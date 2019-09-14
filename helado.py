apetece_input = input("Te apetece un helado? ").upper()
dinero_input = input("Tienes suficiente dinero? ").upper()
if dinero_input != "SI":
    tia_input = input("Está tu tía? ").upper()
tienda_input = input("La tienda está abierta? ").upper()

apetece = apetece_input == "SI"
permitir = dinero_input or tia_input == "SI"
tienda = tienda_input == "SI"

if apetece and permitir and tienda:
    print("Cómetelo.")
else:
    print("Adiós.")
