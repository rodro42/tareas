# Ejercicio 1: Calcular el promedio de una lista
print("Ejercicio 1: Calcular el promedio de una lista")
numeros = [7, 8, 6, 9, 10]
suma = 0
for n in numeros:
    suma += n
promedio = suma / len(numeros)
print("Promedio:", promedio)

# Ejercicio 2: Encontrar el mayor número
print("Ejercicio 2: Encontrar el mayor número")
numeros = [12, 45, 7, 89, 23]
mayor = numeros[0]
for n in numeros:
    if n > mayor:
        mayor = n
print("Mayor número:", mayor)

# Ejercicio 3: Contar cuántos son pares
print("Ejercicio 3: Contar cuántos son pares")
numeros = [1, 4, 7, 8, 10, 3]
pares = 0
for n in numeros:
    if n % 2 == 0:
        pares += 1
print("Cantidad de pares:", pares)


##Ejercicio 4: Invertir una lista manualmente
print("Ejercicio 4: Invertir una lista manualmente")
lista = [5, 10, 15, 20]
lista_invertida = []

for i in range(len(lista)-1, -1, -1):
    lista_invertida.append(lista[i])

print("Lista invertida:", lista_invertida)

##Ejercicio 5: Sumar dos listas elemento a elemento
print("Ejercicio 5: Sumar dos listas elemento a elemento")
a = [1, 2, 3]
b = [4, 5, 6]
resultado = []

for i in range(len(a)):
    resultado.append(a[i] + b[i])

print("Suma:", resultado)

##Ejercicio 6: Contar ocurrencias de un valor dado
print("Ejercicio 6: Contar ocurrencias de un valor dado")
buscar = 3
lista = [1, 3, 5, 3, 9, 3, 7]
contador = 0

for elemento in lista:
    if elemento == buscar:
        contador += 1

print("Aparece", contador, "veces")

##Ejercicio 7: Crear una lista con solo los números mayores a 10
print("Ejercicio 7: Crear una lista con solo los números mayores a 10")
original = [4, 15, 9, 20, 2, 18]
nueva_lista = []

for n in original:
    if n > 10:
        nueva_lista.append(n)

print("Mayores a 10:", nueva_lista)

##Ejercicio 8: Buscar si un número está en una lista
print("Ejercicio 8: Buscar si un número está en una lista")
numeros = [11, 22, 33, 44]
buscar = 33
encontrado = False
for n in numeros:
    if n == buscar:
        encontrado = True
        break
if encontrado:
    print("Sí está en la lista")
else:
    print("No se encontró")

##Ejercicio 9: Sumar solo los impares
print("Ejercicio 9: Sumar solo los impares")
lista = [2, 5, 7, 8, 11]
suma = 0
for num in lista:
    if num % 2 != 0:
        suma += num
print("Suma de impares:", suma)

##Ejercicio 10: Eliminar duplicados (sin usar sets)
print("Ejercicio 10: Eliminar duplicados (sin usar sets)")
lista = [4, 5, 4, 7, 5, 8, 4]
lista_sin_duplicados = []
for n in lista:
    if n not in lista_sin_duplicados:
        lista_sin_duplicados.append(n)
print("Lista limpia:", lista_sin_duplicados)

##¡Detecta el Bug! (Errores en listas de Python) 
##1: Índice fuera de rango
print("1: Índice fuera de rango")
numeros = [3, 6, 9]
for i in range(len(numeros)):  
    print(numeros[i])
    
##2: Lista vacía y acceso directo
print("2: Lista vacía y acceso directo")
frutas = []
if frutas:
    print(frutas[0])
else:
    print("La lista está vacía")

##3: Variable no inicializada
print("3: Variable no inicializada")
lista = [2, 4, 6]
suma = 0
for num in lista:
    suma += num
print(suma) 

##4: Error en condición lógica
print("4: Error en condición lógica")
edades = [15, 22, 30, 18]
mayores = 0

for e in edades:
    if e > 18:
        mayores += 1  
print("Mayores de 18:", mayores)

##5: Comparación incorrecta
print("5: Comparación incorrecta")
nombres = ["Ana", "Luis", "María"]
if "Luis" in nombres:
    print("Está Luis")
    
    
##6: Error por tipo de dato
print("6: Error por tipo de dato")
numeros = [10, 20, 30]
print("Suma: " + str(sum(numeros)))
