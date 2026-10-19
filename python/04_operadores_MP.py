print("Operadores en Python")
print()
print("==== Operadores Aritmeticos ====")
print()
print("Suma + : ", 5, "+", 3, "=", 5+3)
print("Resta - : ", 5, "-", 3, "=", 5-3)
print("Multiplicacion * : ", 5, "*", 3, "=", 5*3)
print("Division / : ", 5, "/", 3, "=", 5/3)
print("Division Entera // : ", 5, "//",  3, "=", 5//3)
print("Modulo % : ", 5, "%", 3, "=", 5%3)
print("Potencia ** : ", 5, "**",  3, "=", 5**3)
print()

print("Tabla de multiplicar del 5")
print(5, "x", 1, "=", 5*1)
print(5, "x", 2, "=", 5*2)
print(5, "x", 3, "=", 5*3)
print(5, "x", 4, "=", 5*4)
print(5, "x", 5, "=", 5*5)
print(5, "x", 6, "=", 5*6)
print(5, "x", 7, "=", 5*7)
print(5, "x", 8, "=", 5*8)
print(5, "x", 9, "=", 5*9)
print(5, "x", 10, "=", 5*10)
print()

print("==== Operadores de Comparacion ====")
print()
print("Igualdad == : ", 5, "==", 5, "=", 5==5)
print("Igualdad == : ", 5, "==", 3, "=", 5==3)
print("Desigualdad != : ", 5, "!=", 3, "=", 5!=3)
print("Desigualdad != : ", 5, "!=", 5, "=", 5!=5)
print("Mayor que > : ", 5, ">", 3, "=", 5>3)
print("Menor que < : ", 5, "<", 3, "=", 5<3)
print("Mayor o igual que >= : ", 5, ">=", 3, "=", 5>=3)
print("Mayor o igual que >= : ", 5, ">=", 8, "=", 5>=8)
print("Menor o igual que <= : ", 5, "<=", 8, "=", 5<=8)
print("Menor o igual que <= : ", 5, "<=", 3, "=", 5<=3)
print()

print("==== Operadores Logicos ====")
print(" OperadorAND : ", True, "and", True, "=", True and True)
print(" Operador AND : ", (5==5), "and", (4>3), "=", (5==5) and (4>3))
print(" Operador AND : ", True, "and", False, "=", True and False)
print(" Operador AND : ", (5==5), "and", (4<3), "=", (5==5) and (4<3))
print(" Operador OR : ", True, "or", False, "=", True or False)
print(" Operador OR : ", (4<3), "or", (5==5), "=", (4<3) or (5==5))
print(" Operador OR : ", False, "or", False, "=", False or False)
print(" Operador OR : ", (5==5), "or", (4<3), "=", (5==5) or (4<3))
print(" Operador NOT : ", not True, "=", not True)
print(" Operador NOT : ", not (5==5), "=", not (5==5))
print()

tiene_dinero = True
tienda_abierta = True

puede_comprar = tiene_dinero and tienda_abierta
print("¿Puede comprar? : ", puede_comprar)

es_cliente_vip = False
tiene_dinero = True
acceso_credito= es_cliente_vip or tiene_dinero
print("Acceso a crédito:", acceso_credito)