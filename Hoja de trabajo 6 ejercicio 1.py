saldo = 3000  
intentos = 0  
max_intentos = 3  
while True:  
    print(f"\nSaldo actual: Q{saldo}")  
    
    try:  
        monto = int(input("Ingrese monto a retirar (0 para salir): "))  
    except ValueError:  
        print("Error: Ingrese un número válido.")  
        continue  

    if monto == 0:  
        print("Gracias por usar el cajero. Adiós.")  
        break  
    elif monto > saldo:  
        intentos += 1  
        print(f"Saldo insuficiente. Intentos restantes: {max_intentos - intentos}")  
        if intentos >= max_intentos:  
            print("Demasiados intentos fallidos. Adiós.")  
            break  
    else:  
        saldo -= monto  
        print(f"Retiro exitoso. Nuevo saldo: Q{saldo}")  
        intentos = 0  

        if saldo == 0:  
            print("Saldo agotado. Adiós.")  
            break