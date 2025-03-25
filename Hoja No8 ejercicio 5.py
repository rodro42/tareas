contraseña_correcta = "hola123"
intentos = 3

while intentos > 0:
    contraseña_ingresada = input("Ingrese su contraseña: ")

    if contraseña_ingresada == contraseña_correcta:
        print("Acceso concedido.")
        break
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Contraseña incorrecta. Intentos restantes: {intentos}")
        else:
            print("Cuenta bloqueada. Demasiados intentos fallidos.")