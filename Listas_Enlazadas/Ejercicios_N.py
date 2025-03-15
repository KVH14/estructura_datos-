# Definición de la clase Animal
class Animal:
    def __init__(self, nombre: str, edad: int, tipo_animal: str):
        # Atributos del animal
        self.nombre = nombre
        self.edad = edad
        self.tipo_animal = tipo_animal
 
    def __str__(self):
        # Representación en cadena del objeto Animal
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Tipo de Animal: {self.tipo_animal}"

# Definición de la clase Nodo para la lista enlazada
class Node:
    def __init__(self, data: Animal) -> None:
        self.data = data  # Contiene un objeto Animal
        self.next = None  # Apunta al siguiente nodo en la lista

# Definición de la clase ListaEnlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicialmente la lista está vacía
        
    def agregar_animal(self, animal: Animal) -> None:
        # Crea un nuevo nodo con el animal
        nodo = Node(animal)
        # Si la lista está vacía, el nuevo nodo será la cabeza
        if self.cabeza is None:
            self.cabeza = nodo

# Entrada de datos del usuario
nombre = input("Ingrese el nombre del animal: ")
edad = int(input("Ingrese la edad del animal: "))
tipo_animal = input("Ingrese el tipo de animal: ")

# Creación del objeto Animal con los datos ingresados
animal = Animal(nombre, edad, tipo_animal)

# Imprime la información del animal
print(animal)
