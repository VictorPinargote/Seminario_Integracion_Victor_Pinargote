print("Colecciones en Python - Pagina de Cursos")
print()
print("==== 1. LISTAS (Lists) ====")
cursos = ["Python", "JavaScript", "Angular", "FastAPI"]
print("Lista de cursos:", cursos)
print("Primer curso:", cursos[0])
print("Ultimo curso:", cursos[-1])
print("Cantidad de cursos:", len(cursos))

# Modificar un elemento de la lista
cursos[1] = "Node.js"
print("Lista modificada:", cursos)

print()
print("==== 2. TUPLAS (Tuples - No se pueden modificar) ====")
categorias = ("Programacion", "Diseño", "Base de Datos")
print("Tupla de categorias:", categorias)
print("Primera categoria:", categorias[0])
print("Total categorias:", len(categorias))

print()
print("==== 3. CONJUNTOS (Sets - No permiten duplicados) ====")
estudiantes = {"Victor", "Juan", "Maria", "Victor"}
print("Conjunto de estudiantes (sin repetidos):", estudiantes)
estudiantes.add("Carlos")
print("Conjunto despues de agregar a Carlos:", estudiantes)

print()
print("==== 4. DICCIONARIOS (Dictionaries - Clave: Valor) ====")
curso_info = {
    "nombre": "Curso de Python",
    "instructor": "Victor Pinargote",
    "precio": 25.0,
    "disponible": True
}
print("Diccionario del curso:", curso_info)
print("Nombre del curso:", curso_info["nombre"])
print("Precio del curso:", curso_info["precio"])

# Cambiar el precio en el diccionario
curso_info["precio"] = 19.99
print("Diccionario con nuevo precio:", curso_info)