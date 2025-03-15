class Tarea:
    def __init__(self, descrip, prioridad, fecha):
        self.desc, self.prioridad, self.fecha = descrip, prioridad, fecha

    def __str__(self):
        return f"{self.prioridad} - {self.desc} (Vence: {self.fecha})"

class Nodo:
    def __init__(self, tarea):
        self.tarea, self.siguiente = tarea, None

class ListaTareas:
    def __init__(self):
        self.cabeza = None

    def agregar_tarea(self, tarea):
        nuevo_nodo = Nodo(tarea)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar_tarea(self, descrip):
       actual, previo = self.cabeza, None
       while actual and actual.tarea.descrip != descrip:
          previo, actual = actual, actual.siguiente
       if actual:
          if previo:
               previo.siguiente = actual.siguiente
          else:
               self.cabeza = actual.siguiente

    def mostrar_tareas(self):
        actual = self.cabeza
        print("Tareas:" if actual else " No hay tareas.")
        while actual:
            print(actual.tarea)
            actual = actual.siguiente

lista = ListaTareas()

while (opcion := input("1.Agregar  2.Eliminar  3.Mostrar  4.Salir Elige: ")) != "4":
    if opcion == "1":
        lista.agregar_tarea(Tarea(input("Descripción: "), int(input("Prioridad: ")), input("Fecha: ")))
    elif opcion == "2":
        lista.eliminar_tarea(input("Descripción a eliminar: "))
    elif opcion == "3":
        lista.mostrar_tareas()
    else:
        print("Opción no válida.")
