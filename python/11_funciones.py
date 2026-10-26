def kame

def atacar(guerrero):
    print(guerrero, "realiza un ataque")

atacar("Goku")
atacar("Vegeta")
atacar("Picolo")
atacar("Victor")

def calcular_poder(poder, ataque):
    danio= poder * ataque
    return danio

resultado = calcular_poder(4, 25)
print("El poder de victor pinargote es: ", resultado)

resultado = calcular_poder(4, 25)
print("El poder de Goku es: ", resultado)

def transformar_saiyayin(nombre, poder):
    if poder>=1000:
        print(f"Trnasformacion de {nombre} a Supersaiyayin exitoso")
    else:
        print(f"{nombre} Nececitra Aumentar tu poder")

transformar_saiyayin("Victor", 5000)
transformar_saiyayin("gohan", 15000)

nombre_personaje: str = "Goku"
edad: int = 33
altura: float = 1.74
es_activo: bool = True

def multiplicador_poder(entrenamiento: float, edad: int) -> float:
    return entrenamiento*edad

poder:float = multiplicador_poder(25,5,2)
print("Poder calcualdo ", poder)