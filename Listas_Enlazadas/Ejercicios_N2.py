# Clase que representa una tarea con descripción, prioridad y fecha de vencimiento.
class Tarea:
    def __init__(self, descrip, prioridad, fecha):
        self.desc, self.prioridad, self.fecha = descrip, prioridad, fecha  # Se almacenan los datos de la tarea

    def __str__(self):
        # Devuelve una representación en cadena de la tarea
        return f"{self.prioridad} - {self.desc} (Vence: {self.fecha})"

# Clase Nodo para la lista enlazada, almacena una tarea y un puntero al siguiente nodo.
class Nodo:
    def __init__(self, tarea):
        self.tarea, self.siguiente = tarea, None  # El nodo contiene una tarea y apunta al siguiente nodo (inicialmente None)

# Lista enlazada para almacenar las tareas
class ListaTareas:
    def __init__(self):
        self.cabeza = None  # La lista inicia vacía

    # Agrega una nueva tarea al final de la lista
    def agregar_tarea(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if not self.cabeza:  # Si la lista está vacía, el nuevo nodo es la cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:  # Recorre la lista hasta el último nodo
                actual = actual.siguiente 
            actual.siguiente = nuevo_nodo  # Agrega el nuevo nodo al final

    # Elimina una tarea de la lista según su descripción
    def eliminar_tarea(self, descrip):
        actual, previo = self.cabeza, None
        while actual and actual.tarea.desc != descrip:  # Busca la tarea en la lista
            previo, actual = actual, actual.siguiente
        if actual:  # Si se encontró la tarea
            if previo:  # Si no es la primera en la lista
                previo.siguiente = actual.siguiente  # Se salta el nodo eliminado
            else:
                self.cabeza = actual.siguiente  # Si es la primera, se actualiza la cabeza

    # Muestra todas las tareas en la lista
    def mostrar_tareas(self):
        actual = self.cabeza
        print("Tareas:" if actual else "No hay tareas.")  # Mensaje dependiendo de si hay tareas o no
        while actual:  # Recorre y muestra cada tarea
            print(actual.tarea)
            actual = actual.siguiente

# Se crea una instancia de la lista de tareas
lista = ListaTareas()

# Menú interactivo para gestionar las tareas
while (opcion := input("1.Agregar  2.Eliminar  3.Mostrar  4.Salir Elige: ")) != "4":
    if opcion == "1":  # Agregar una nueva tarea
        desc = input("Descripción: ")
        prioridad = int(input("Prioridad: "))
        fecha = input("Fecha: ")
        lista.agregar_tarea(Tarea(desc, prioridad, fecha))
    elif opcion == "2":  # Eliminar una tarea
        lista.eliminar_tarea(input("Descripción a eliminar: "))
    elif opcion == "3":  # Mostrar todas las tareas
        lista.mostrar_tareas()
    else:
        print("Opción no válida.")  # Mensaje de error si la opción no es válida
