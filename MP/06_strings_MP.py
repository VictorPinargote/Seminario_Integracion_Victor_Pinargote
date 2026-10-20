print("Manejo de Strings en Python")
print("==== Creacion y Concatenacion ====")

nombre_curso = "Curso de Python"
plataforma = "WebCursos"
mensaje = nombre_curso + " en " + plataforma
print(mensaje)

print()
print("==== Longitud de un String (len) ====")
titulo = "Desarrollo Web Full Stack"
print("Titulo del curso:", titulo)
print("Cantidad de letras:", len(titulo))

print()
print("==== Metodos de Strings ====")
descripcion = "aprende a programar desde cero con proyectos"
print("Mayusculas (upper):", descripcion.upper())
print("Minusculas (lower):", descripcion.lower())
print("Primera letra mayuscula (capitalize):", descripcion.capitalize())
print("Formato titulo (title):", descripcion.title())

print()
print("==== Reemplazar y Quitar Espacios ====")
oferta = "   Curso de Java en descuento   "
print("Sin espacios (strip):", oferta.strip())
print("Reemplazar palabra (replace):", oferta.replace("Java", "Python"))

print()
print("==== Indices y Slicing (Cortar texto) ====")
codigo_curso = "PYTHON-2026"
print("Primera letra:", codigo_curso[0])
print("Ultima letra:", codigo_curso[-1])
print("Primeras 6 letras:", codigo_curso[0:6])

print()
print("==== Busqueda en un String ====")
print("¿Esta la palabra Python?:", "Python" in nombre_curso)
print("¿Esta la palabra Angular?:", "Angular" in nombre_curso)