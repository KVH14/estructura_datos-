class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        #Inserta un elemento en la pila.#
        self.elementos.append(elemento)

    def pop(self):
        #Elimina y devuelve el último elemento de la pila.
        if self.isEmpty():
            return "Pila vacía"
        return self.elementos.pop()

    def peek(self):
        #Devuelve el elemento superior sin eliminarlo.
        if self.isEmpty():
            return "Pila vacía"
        return self.elementos[-1]

    def isEmpty(self):
        #Verifica si la pila está vacía
        return len(self.elementos) == 0

# Crear una pila
pila = Pila()

print("Menú de Operaciones")
print("1. Insertar elemento (push)")
print("2. Eliminar elemento (pop)")
print("3. Ver cima de la pila (peek)")
print("4. Verificar si la pila está vacía (isEmpty)")
print("5. Salir")
    
opcion = input("Elige una opción: ")
while True:
    print("Menú de Operaciones")
    print("1. Insertar elemento (push)")
    print("2. Eliminar elemento (pop)")
    print("3. Ver cima de la pila (peek)")
    print("4. Verificar si la pila está vacía (isEmpty)")
    print("5. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        valor = input("Ingresa un valor para apilar: ")
        pila.push(valor)
        print(f"Se insertó {valor} en la pila.")
        print(f"Elementos en la pila: {pila.elementos}")

    elif opcion == "2":
        print(f"Se eliminó: {pila.pop()}")

    elif opcion == "3":
        print(f"Elemento en la cima: {pila.peek()}")

    elif opcion == "4":
        if pila.isEmpty():
            print("La pila está vacía.")
        else:
            print("La pila tiene elementos.")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida, intenta de nuevo.")