print("Condicionales If")
print("==== Condicionales Simples ====")

dinero = 20
if dinero >= 15:
    print("El estudiante puede comprar el curso de Python")

print()
print("==== Condicionales If - Else ====")
cupos = 5
if cupos > 0:
    print("Si hay cupos disponibles para el curso")
else:
    print("El curso esta lleno, no hay cupos")

print()
print("==== Condicionales If - Elif - Else ====")
cantidad_cursos = 3
if cantidad_cursos >= 5:
    print("Tienes un descuento del 30% en tus cursos")
elif cantidad_cursos >= 3:
    print("Tienes un descuento del 15% en tus cursos")
elif cantidad_cursos >= 1:
    print("Pagas el precio normal del curso")
else:
    print("No tienes cursos en el carrito")

print()
print("==== Condicional con Operadores Logicos ====")
tiene_internet = True
pago_aprobado = True

if tiene_internet and pago_aprobado:
    print("Bienvenido, ya puedes ver las clases del curso")
else:
    print("No puedes acceder al curso todavia")

print("Programa terminado")