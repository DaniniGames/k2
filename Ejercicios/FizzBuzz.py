numeros = [1, 5, 8, 23, 80, 70, 34, 56, 23, 32, 55, 95, 9, 15, 90]

for i in range(len(numeros)):
    if numeros[i] % 3 == 0 and numeros[i] % 5 == 0:
        numeros[i] = "Bazinga"
    elif numeros[i] % 3 == 0:
        numeros[i] = "Fizz"
    elif numeros[i] % 5 == 0:
        numeros[i] = "Buzz"

print(numeros)