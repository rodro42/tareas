from collections import Counter

def registrar_respuestas(n):
    respuestas = []
    for i in range(n):
        while True:
            try:
                respuesta = int(input(f"Ingresa la respuesta del cliente {i+1} (1 a 5): "))
                if respuesta < 1 or respuesta > 5:
                    print("Respuesta inválida, debe ser un número entre 1 y 5.")
                else:
                    respuestas.append(respuesta)
                    break
            except ValueError:
                print("Por favor ingresa un número válido entre 1 y 5.")
    return respuestas

def tabular_respuestas(respuestas):
    conteo = Counter(respuestas)
    tipos_respuesta = {
        5: "Excelente",
        4: "Muy Buena",
        3: "Buena",
        2: "Regular",
        1: "Malo"
    }

    print("\nRespuestas:")
    for i in range(1, 6):
        print(f"{tipos_respuesta[i]}: {conteo[i]}")

    respuesta_frecuente = conteo.most_common(1)[0][0]
    print(f"\nLa respuesta más frecuente es: {respuesta_frecuente}")

    promedio = sum(respuestas) / len(respuestas)
    print(f"\nPromedio de respuestas: {promedio:.2f}")

    menor_promedio = [i+1 for i, r in enumerate(respuestas) if r < promedio]
    porcentaje_menor_promedio = (len(menor_promedio) / len(respuestas)) * 100
    print(f"Porcentaje de clientes con respuestas menores al promedio: {porcentaje_menor_promedio:.2f}%")

n = int(input("Ingresa el número de clientes atendidos: "))
respuestas = registrar_respuestas(n)
tabular_respuestas(respuestas)
