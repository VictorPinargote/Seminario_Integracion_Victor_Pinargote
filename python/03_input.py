print("Incluir Datos con Input")
nombre = input("¿Cual es tu nombre?: ")
print("Hola,", nombre, "Bienvenido a Python")
print("hasta luego " +  nombre + " nos vemos pronto")

cantidad = int(input("¿Cuantas rosquillas quieres?: "))
print(cantidad+2)
total = cantidad
print("Rosquillas totales" , total)

print("CONVERSIONES DE TIPOS DE DATOS")
print("==== Tienda de api ====")
nombre_cliente = input("¿Cual es tu nombre?: ")
precio = float(input("¿Cual es el precio de las rosquillas?: "))
cantidad = int(input("Cantidad: "))
total = precio * cantidad
print("El total a pagar es: ", total)
print("El total a pagar es (round): ", round(total, 2))
print(f"El total a pagar es (round): {round(total, 2)*cantidad}")