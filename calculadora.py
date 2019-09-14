op = input("Qué operación quieres realizar? multiplicar, dividir, sumar o restar: ").lower()
x = int(input("Introduce el primer valor: "))
y = int(input("Introduce el segundo valor: "))

if op == "multiplicar":
    print(x * y)
elif op == "dividir":
    print(x/y)
elif op == "sumar":
    print(x+y)
elif op == "restar":
    print(x-y)
else:
    print("Esta operación no existe")
