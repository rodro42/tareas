n = int(input("Ingrese la cantidad de clientes: "))
p = n
lista = []
promedio = 0
uno, dos, tres, cuatro, cinco = 0, 0, 0, 0, 0
suma = 0

while n != 0:
    nota = int(input("Ingrese la calificación (1-5): "))
    if nota < 1 or nota > 5:
        print("Calificación inválida, debe ser entre 1 y 5.")
        continue
    lista.append(nota)
    suma += nota
    if nota == 1:
        uno += 1
    elif nota == 2:
        dos += 1
    elif nota == 3:
        tres += 1
    elif nota == 4:
        cuatro += 1
    elif nota == 5:
        cinco += 1
    n -= 1

promedio = suma / p
menor_al_promedio = sum(1 for x in lista if x < promedio)

print("\nRespuestas:")
print(f"Excelente: {cinco}")
print(f"Muy Buena: {cuatro}")
print(f"Buena: {tres}")
print(f"Regular: {dos}")
print(f"Malo: {uno}")

print(f"\nPromedio: {promedio:.2f}")

frecuencias = {1: uno, 2: dos, 3: tres, 4: cuatro, 5: cinco}
max_respuesta = max(frecuencias, key=frecuencias.get)
print(f"\nLa respuesta más frecuente es: {max_respuesta}")

porcentaje_menor_al_promedio = (menor_al_promedio / p) * 100
print(f"\nPorcentaje de clientes con calificaciones menores al promedio: {porcentaje_menor_al_promedio:.2f}%")

