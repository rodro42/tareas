numero = int(input("Ingrese un número: "))  # Pedimos un número al usuario
suma = 0
n = 1

while n <= numero:  # Mientras n sea menor o igual al número ingresado
    suma += n  # Sumamos n a la variable suma
    print(f"La suma hasta {n} es: {suma}")  # Mostramos el resultado parcial
    n += 1  # Incrementamos n para la siguiente iteración

print(f"La suma total es: {suma}")  # Mostramos el resultado final