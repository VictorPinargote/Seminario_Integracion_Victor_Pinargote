class Guerrero:
    nombre: str
    raza: str

    def __init__(self, nombre: str, raza: str):
        self.nombre = nombre
        self.raza = raza

    def mostrar_info(self):
        print("Nombre ", self.nombre)
        print("Raza ", self.raza)

Goku = Guerrero("Goku", "Saiyayin")
Vegeta = Guerrero("Vegeta", "Saiyayin")
Picolo = Guerrero("Picolo", "Namekiano")
Victor = Guerrero("Victor", "Tu Macho")