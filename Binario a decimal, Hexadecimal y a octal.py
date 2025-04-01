binario = input("Ingrese un número en binario: ")

es_valido = True
for d in binario:
    if d != '0' and d != '1':
        es_valido = False
        break

if not es_valido:
    print("Entrada no válida. Ingrese solo 0 y 1.")
else:
    decimal = 0
    potencia = 1
    for d in reversed(binario):
        if d == '1':
            decimal += potencia
        potencia *= 2

    valores_hex = "0123456789ABCDEF"
    hexadecimal = ""
    temp_decimal = decimal

    while temp_decimal > 0:
        hexadecimal = valores_hex[temp_decimal % 16] + hexadecimal
        temp_decimal //= 16

    if hexadecimal == "":
        hexadecimal = "0"

    octal = ""
    temp_decimal = decimal

    while temp_decimal > 0:
        octal = str(temp_decimal % 8) + octal
        temp_decimal //= 8

    if octal == "":
        octal = "0"

    print("Decimal:", decimal)
    print("Hexadecimal:", hexadecimal)
    print("Octal:", octal)