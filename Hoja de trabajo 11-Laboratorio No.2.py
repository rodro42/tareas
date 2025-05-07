from calculadora import RaizCuadrada, Potencia, Logaritmo, Factorial

def solicitar_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada inválida. Intenta nuevamente.")

def solicitar_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print("Debe ser un número entero no negativo.")
                continue
            return numero
        except ValueError:
            print("Entrada inválida. Intenta nuevamente.")

def menu():
    print("\n--- Calculadora Científica ---")
    print("1. Raíz Cuadrada")
    print("2. Potencia")
    print("3. Logaritmo")
    print("4. Factorial")
    print("5. Salir")
    return input("Seleccione una opción: ")

while True:
    opcion = menu()

    try:
        if opcion == "1":
            numero = solicitar_float("Ingrese el número: ")
            operacion = RaizCuadrada(numero)
            resultado = operacion.calcular()
            print(f"Resultado: {resultado}")

        elif opcion == "2":
            base = solicitar_float("Ingrese la base: ")
            exponente = solicitar_float("Ingrese el exponente: ")
            operacion = Potencia(base, exponente)
            resultado = operacion.calcular()
            print(f"Resultado: {resultado}")

        elif opcion == "3":
            numero = solicitar_float("Ingrese el número (mayor que 0): ")
            base = solicitar_float("Ingrese la base del logaritmo (mayor que 0 y distinta de 1): ")
            if numero <= 0 or base <= 0 or base == 1:
                raise ValueError("El número debe ser > 0 y la base > 0 y ≠ 1.")
            operacion = Logaritmo(numero, base)
            resultado = operacion.calcular()
            print(f"Resultado: {resultado}")

        elif opcion == "4":
            numero = solicitar_entero_positivo("Ingrese un número entero no negativo: ")
            operacion = Factorial(numero)
            resultado = operacion.calcular()
            print(f"Resultado: {resultado}")

        elif opcion == "5":
            print("Saliendo de la calculadora.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

    except ValueError as e:
        print(f"Error: {e}")
