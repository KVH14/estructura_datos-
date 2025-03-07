class Persona:
    def __init__(self, nombre: str, edad: int, genero: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def presentar(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.genero}.")

nombre = input("Ingrese su nombre: ")
print("")
edad = int(input("Ingrese su edad: "))
print("")
genero = input("Ingrese su género: ")


persona = Persona(nombre, edad, genero)
persona.presentar()
