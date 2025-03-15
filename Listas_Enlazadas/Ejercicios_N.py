class Animal:
    def __init__(self, nombre: str, edad: int, tipo_animal: str):
        self.nombre = nombre
        self.edad = edad
        self.tipo_animal = tipo_animal
        self.cabeza = None
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Tipo de Animal: {self.tipo_animal}"

class Node:
    def __init__(self, data: Animal) -> None:
        self.data = data
        self.next = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        
    def agregar_animal(self, animal: Animal) -> None:
        nodo = Node(animal)
        if self.cabeza is None:
            self.cabeza = nodo



nombre = input("Ingrese el nombre del animal: ")
edad = int(input("Ingrese la edad del animal: "))
tipo_animal = input("Ingrese el tipo de animal: ")


animal = Animal(nombre, edad, tipo_animal)


print(animal)