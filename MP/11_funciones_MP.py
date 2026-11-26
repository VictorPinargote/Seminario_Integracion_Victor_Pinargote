print("POO / Clases y Objetos en Python - Venta de Cursos")
print()

print("==== Clase Basica ====")
class Curso:
    def __init__(self, titulo, precio, cupos):
        self.titulo = titulo
        self.precio = precio
        self.cupos = cupos

    def mostrar_info(self):
        print("Curso:", self.titulo, "| Precio: $" + str(self.precio), "| Cupos:", self.cupos)

    def comprar_cupo(self):
        if self.cupos > 0:
            self.cupos = self.cupos - 1
            print("Compra exitosa en", self.titulo + ". Cupos restantes:", self.cupos)
        else:
            print("No hay cupos disponibles en", self.titulo)

curso1 = Curso("Python desde Cero", 19.99, 3)
curso2 = Curso("FastAPI y Bases de Datos", 29.99, 2)

curso1.mostrar_info()
curso2.mostrar_info()

print()
print("==== Usar Metodos del Objeto ====")
curso1.comprar_cupo()
curso1.comprar_cupo()
curso1.mostrar_info()