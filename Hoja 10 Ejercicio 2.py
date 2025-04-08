tamano = int(input("Ingresa el tamaño del arreglo: "))

Array1 = []
Longitud = []

for i in range(tamano):
    nombre = input(f"Ingresa el nombre {i+1}: ")
    Array1.append(nombre)
    Longitud.append(len(nombre))

print("Array1:", Array1)
print("Longitud:", Longitud)
