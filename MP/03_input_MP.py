print("Incluir Datos con Input")
nombre = input("¿Cual es tu nombre?: ")
print("Hola,", nombre, "Bienvenido a la Pagina de Cursos")
print("hasta luego " +  nombre + " nos vemos pronto")

cantidad = int(input("¿Cuantos cursos quieres comprar?: "))
print(cantidad+2)
total = cantidad
print("Cursos totales" , total)

print("CONVERSIONES DE TIPOS DE DATOS")
print("==== Tienda de Cursos ====")
nombre_cliente = input("¿Cual es tu nombre?: ")
precio = float(input("¿Cual es el precio del curso?: "))
cantidad = int(input("Cantidad de cursos: "))
total = precio * cantidad
print("El total a pagar es: ", total)
print("El total a pagar es (round): ", round(total, 2))
print(f"El total a pagar es (round): {round(total, 2)*cantidad}")
print("Gracias por tu compra,", nombre_cliente)