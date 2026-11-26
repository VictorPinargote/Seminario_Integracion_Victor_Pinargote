print("Polimorfismo en POO en Python - Venta de Cursos")
print()

print("==== Clase Base y Clases con Mismo Metodo ====")
class Curso:
    def __init__(self, titulo, precio):
        self.titulo = titulo
        self.precio = precio

    def tipo_acceso(self):
        print("Acceso general al curso:", self.titulo)

class CursoGrabado(Curso):
    def tipo_acceso(self):
        print("Acceso on-demand (videos grabados) en:", self.titulo, "- $" + str(self.precio))

class CursoEnVivo(Curso):
    def tipo_acceso(self):
        print("Acceso a sala en vivo y chat en:", self.titulo, "- $" + str(self.precio))

class CursoTaller(Curso):
    def tipo_acceso(self):
        print("Acceso a laboratorio practico y repositorios en:", self.titulo, "- $" + str(self.precio))

print()
print("==== Usar Polimorfismo con Lista de Cursos ====")
catalogo = [
    CursoGrabado("Python desde Cero", 19.99),
    CursoEnVivo("FastAPI en Tiempo Real", 34.99),
    CursoTaller("Git y GitHub Practico", 14.99)
]

for curso in catalogo:
    curso.tipo_acceso()