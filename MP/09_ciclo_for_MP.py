print("Bucles en Python - Venta de Cursos")
print()
print("==== Bucle For con Lista de Cursos ====")
cursos = ["Curso de Python", "Curso de FastAPI", "Curso de Angular", "Curso de SQL"]

for curso in cursos:
    print("Curso disponible:", curso)

print()
print("==== Bucle For con Range ====")
for numero in range(1, 6):
    print("Modulo numero:", numero)

print()
print("==== Bucle For con Break ====")
for curso in cursos:
    if curso == "Curso de Angular":
        print("Curso encontrado, deteniendo busqueda...")
        break
    print("Revisando:", curso)

print()
print("==== Bucle While ====")
cupos_disponibles = 3
while cupos_disponibles > 0:
    print("Cupo asignado. Quedan:", cupos_disponibles - 1)
    cupos_disponibles = cupos_disponibles - 1

print("Inscripciones cerradas por hoy")