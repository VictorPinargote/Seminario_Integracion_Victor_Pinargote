print("Herencia en POO en Python - Venta de Cursos")
print()

print("==== Clase Padre ====")
class CursoBase:
    def __init__(self, titulo, precio):
        self.titulo = titulo
        self.precio = precio

    def mostrar_info(self):
        print("Curso:", self.titulo, "| Precio: $" + str(self.precio))

print()
print("==== Clase Hija (Herencia) ====")
class CursoGrabado(CursoBase):
    def __init__(self, titulo, precio, horas_video):
        super().__init__(titulo, precio)
        self.horas_video = horas_video

    def mostrar_grabado(self):
        self.mostrar_info()
        print("Duracion:", self.horas_video, "horas de video")

class CursoEnVivo(CursoBase):
    def __init__(self, titulo, precio, dia_clase):
        super().__init__(titulo, precio)
        self.dia_clase = dia_clase

    def mostrar_en_vivo(self):
        self.mostrar_info()
        print("Clases en vivo los:", self.dia_clase)

curso_video = CursoGrabado("Python Basico", 19.99, 12)
curso_vivo = CursoEnVivo("FastAPI Practico", 34.99, "Sabados")

curso_video.mostrar_grabado()
print()
curso_vivo.mostrar_en_vivo()