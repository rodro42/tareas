def llenar_arreglo(tamano, base):
    arreglo = []
    for i in range(1, tamano + 1):
        arreglo.append(base * i)
    return arreglo

tamano = int(input("Ingresa el tamaño del arreglo: "))
base = int(input("Ingresa el número base para generar los múltiplos: "))

arreglo = llenar_arreglo(tamano, base)
print("El arreglo con los primeros múltiplos de", base, "es:", arreglo)
