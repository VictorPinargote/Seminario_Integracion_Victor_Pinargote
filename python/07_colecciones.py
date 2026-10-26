print("Colecciones de datos")
print("==== Listas ====")
naves=["N-1", "Transporte", "Naboo"]
print("Naves:", naves)
print("tipo:", type(naves))
print("==== Tuplas ====")
coordenadas = (15, 30, 45)
print("Coordenadas:", coordenadas)
print("tipo:", type(coordenadas))
print("==== Diccionarios ====")
droide = {
    "modelo": "R2-D2",
    "tipo": "Astrodroide",
    "activo": True
}
print("Droide:", droide)
print("tipo:", type(droide))
print("==== Conjuntos ====")
planetas = {"Tatooine", "Alderaan", "Naboo"}
print("Planetas:", planetas)
print("tipo:", type(planetas))

print("==== Crud de listas en Python ====")
advengers = [
    {"id": 1, "nombre": "Tony Stark", "heroe": "Iron Man", "estado": True},
    {"id": 2, "nombre": "Steve Rogers", "heroe": "Capitán América", "estado": True},
    {"id": 3, "nombre": "Thor Odinson", "heroe": "Thor", "estado": True},
]

id_publico = 4
def create():
    global id_publico
    print("Reclutar advenger")
    nombre = input("Ingrese el nombre del advenger: ")
    heroe = input("Ingrese el nombre del héroe: ")
    estado = input("Estado [Activo, Retirado, Desaparecido]")
    nuevo_advenger = {
        "id": id,
        "nombre": nombre,
        "estado": estado
    }
    advengers.append(nuevo_advenger)