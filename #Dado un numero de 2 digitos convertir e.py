#Dado un numero de 2 digitos convertir el equivalente a texto 
def numero_a_texto(n):
    if not (10 <= n < 100):
        return "Número fuera de rango"

    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", 
                "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

    if n < 20:
        return unidades[n]
    elif n % 10 == 0:
        return decenas[n // 10]
    else:
        return f"{decenas[n // 10]} y {unidades[n % 10]}"

print(numero_a_texto(4))
print(numero_a_texto(66))
print(numero_a_texto(10))





































