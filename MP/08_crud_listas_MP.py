print("CRUD de Listas en Python - Venta de Cursos")
print()

# ==========================================
# CREATE (Crear lista y agregar elementos)
# ==========================================
print("==== 1. CREATE (Crear y Agregar Cursos) ====")
catalogo_cursos = ["Curso de HTML", "Curso de CSS", "Curso de Python"]
print("Catalogo inicial:", catalogo_cursos)

# Agregar al final con append()
catalogo_cursos.append("Curso de JavaScript")
catalogo_cursos.append("Curso de Angular")
print("Despues de append:", catalogo_cursos)

# Agregar en una posicion especifica con insert()
catalogo_cursos.insert(1, "Curso de Git y GitHub")
print("Despues de insert en posicion 1:", catalogo_cursos)
print()

# ==========================================
# READ (Leer y consultar elementos)
# ==========================================
print("==== 2. READ (Leer Cursos) ====")
print("Todos los cursos:", catalogo_cursos)
print("Curso en la posicion 0:", catalogo_cursos[0])
print("Curso en la posicion 2:", catalogo_cursos[2])
print("Ultimo curso de la lista:", catalogo_cursos[-1])
print("Total de cursos en la pagina:", len(catalogo_cursos))
print()

# ==========================================
# UPDATE (Actualizar o modificar elementos)
# ==========================================
print("==== 3. UPDATE (Actualizar Cursos) ====")
print("Curso antes de actualizar:", catalogo_cursos[0])
catalogo_cursos[0] = "Curso de HTML5 Avanzado"
print("Catalogo actualizado:", catalogo_cursos)

catalogo_cursos[3] = "Curso de Python y FastAPI"
print("Catalogo con otro cambio:", catalogo_cursos)
print()

# ==========================================
# DELETE (Eliminar elementos de la lista)
# ==========================================
print("==== 4. DELETE (Eliminar Cursos) ====")
# Eliminar por nombre con remove()
catalogo_cursos.remove("Curso de CSS")
print("Despues de remove('Curso de CSS'):", catalogo_cursos)

# Eliminar el ultimo elemento con pop()
curso_eliminado = catalogo_cursos.pop()
print("Curso eliminado con pop():", curso_eliminado)
print("Catalogo despues de pop():", catalogo_cursos)

# Eliminar por indice con pop(indice)
catalogo_cursos.pop(0)
print("Despues de eliminar la posicion 0:", catalogo_cursos)
print("Catalogo final de cursos:", catalogo_cursos)