print("Operadores en Python - Venta de Cursos")
print()
print("==== Operadores Aritmeticos ====")
print()
print("Suma + : ", 10, "+", 2, "=", 10+2)
print("Resta - : ", 10, "-", 2, "=", 10-2)
print("Multiplicacion * : ", 10, "*", 2, "=", 10*2)
print("Division / : ", 10, "/", 2, "=", 10/2)
print("Division Entera // : ", 10, "//",  3, "=", 10//3)
print("Modulo % : ", 10, "%", 3, "=", 10%3)
print("Potencia ** : ", 10, "**",  2, "=", 10**2)
print()

print("Tabla de multiplicar del precio del curso (10 dolares)")
print(10, "x", 1, "=", 10*1)
print(10, "x", 2, "=", 10*2)
print(10, "x", 3, "=", 10*3)
print(10, "x", 4, "=", 10*4)
print(10, "x", 5, "=", 10*5)
print(10, "x", 6, "=", 10*6)
print(10, "x", 7, "=", 10*7)
print(10, "x", 8, "=", 10*8)
print(10, "x", 9, "=", 10*9)
print(10, "x", 10, "=", 10*10)
print()

print("==== Operadores de Comparacion ====")
print()
print("Igualdad == : ", 10, "==", 10, "=", 10==10)
print("Igualdad == : ", 10, "==", 5, "=", 10==5)
print("Desigualdad != : ", 10, "!=", 5, "=", 10 != 5)
print("Desigualdad != : ", 10, "!=", 10, "=", 10!=10)
print("Mayor que > : ", 10, ">", 5, "=", 10>5)
print("Menor que < : ", 10, "<", 5, "=", 10<5)
print("Mayor o igual que >= : ", 10, ">=", 5, "=", 10>=5)
print("Mayor o igual que >= : ", 10, ">=", 15, "=", 10>=15)
print("Menor o igual que <= : ", 10, "<=", 15, "=", 10<=15)
print("Menor o igual que <= : ", 10, "<=", 5, "=", 10<=5)
print()

print("==== Operadores Logicos ====")
print(" OperadorAND : ", True, "and", True, "=", True and True)
print(" Operador AND : ", (10==10), "and", (8>5), "=", (10==10) and (8>5))
print(" Operador AND : ", True, "and", False, "=", True and False)
print(" Operador AND : ", (10==10), "and", (8<5), "=", (10==10) and (8<5))
print(" Operador OR : ", True, "or", False, "=", True or False)
print(" Operador OR : ", (8<5), "or", (10==10), "=", (8<5) or (10==10))
print(" Operador OR : ", False, "or", False, "=", False or False)
print(" Operador OR : ", (10==10), "or", (8<5), "=", (10==10) or (8<5))
print(" Operador NOT : ", not True, "=", not True)
print(" Operador NOT : ", not (10==10), "=", not (10==10))
print()

tiene_dinero = True
pagina_cursos_abierta = True

puede_comprar_curso = tiene_dinero and pagina_cursos_abierta
print("¿Puede comprar el curso? : ", puede_comprar_curso)

es_estudiante_vip = False
tiene_dinero = True
acceso_beca = es_estudiante_vip or tiene_dinero
print("Acceso a beca o curso:", acceso_beca)

tiene_cupon = True
descuento_especial = puede_comprar_curso and tiene_cupon
print("¿Tiene descuento especial?:", descuento_especial)