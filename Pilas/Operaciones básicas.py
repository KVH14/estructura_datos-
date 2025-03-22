class Pila:
    """Clase que representa una pila (estructura LIFO - Last In, First Out)."""

    def __init__(self) -> None:
        """Inicializa una pila vacía."""
        self.elementos: list[str] = []

    def push(self, elemento: str) -> None:
        """Inserta un elemento en la pila.
        
        Args:
            elemento (str): Elemento a agregar en la pila.
        """
        self.elementos.append(elemento)

    def pop(self) -> str:
        """Elimina y devuelve el último elemento de la pila.
        
        Returns:
            str: El último elemento de la pila o un mensaje si está vacía.
        """
        if self.isEmpty():
            return "Pila vacía"
        return self.elementos.pop()

    def peek(self) -> str:
        """Devuelve el elemento superior sin eliminarlo.
        
        Returns:
            str: El elemento en la cima de la pila o un mensaje si está vacía.
        """
        if self.isEmpty():
            return "Pila vacía"
        return self.elementos[-1]

    def isEmpty(self) -> bool:
        """Verifica si la pila está vacía.
        
        Returns:
            bool: True si la pila está vacía, False en caso contrario.
        """
        return len(self.elementos) == 0


# Crear una instancia de la pila
pila = Pila()

# Bucle para el menú de operaciones
while True:
    print("\nMenú de Operaciones")
    print("1. Insertar elemento (push)")
    print("2. Eliminar elemento (pop)")
    print("3. Ver cima de la pila (peek)")
    print("4. Verificar si la pila está vacía (isEmpty)")
    print("5. Salir")
    
    opcion: str = input("Elige una opción: ")  # Solicitar opción al usuario

    if opcion == "1":
        # Insertar un elemento en la pila
        valor: str = input("Ingresa un valor para apilar: ")
        pila.push(valor)
        print(f"Se insertó {valor} en la pila.")
        print(f"Elementos en la pila: {pila.elementos}")

    elif opcion == "2":
        # Eliminar el último elemento de la pila
        print(f"Se eliminó: {pila.pop()}")

    elif opcion == "3":
        # Mostrar el elemento en la cima sin eliminarlo
        print(f"Elemento en la cima: {pila.peek()}")

    elif opcion == "4":
        # Verificar si la pila está vacía
        print("La pila está vacía." if pila.isEmpty() else "La pila tiene elementos.")

    elif opcion == "5":
        # Salir del programa
        print("Saliendo del programa...")
        break

    else:
        # Manejo de opción inválida
        print("Opción no válida, intenta de nuevo.")
