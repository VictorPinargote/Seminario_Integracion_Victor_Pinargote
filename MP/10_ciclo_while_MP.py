print("Funciones en Python - Venta de Cursos")
print()

print("==== Funcion Basica ====")
def saludar_estudiante() -> None:
    print("Hola, bienvenido a la tienda de cursos online")

saludar_estudiante()

print()
print("==== Funcion con Parametros ====")
def mostrar_curso(nombre_curso: str, precio: float) -> None:
    print("Curso:", nombre_curso, "- Precio: $" + str(precio))

mostrar_curso("Python desde Cero", 19.99)
mostrar_curso("FastAPI con Python", 24.50)

print()
print("==== Funcion que Retorna un Valor ====")
def calcular_total(precio_curso: float, cantidad: int) -> float:
    total: float = precio_curso * cantidad
    return total

total_pagar: float = calcular_total(15.0, 3)
print("Total a pagar por los cursos:", total_pagar)

print()
print("==== Funcion con Valor por Defecto ====")
def aplicar_descuento(precio: float, descuento: float = 10) -> float:
    precio_final: float = precio - (precio * descuento / 100)
    return precio_final

print("Precio con descuento por defecto:", aplicar_descuento(50))
print("Precio con 20% de descuento:", aplicar_descuento(50, 20))