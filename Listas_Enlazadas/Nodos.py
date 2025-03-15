# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None # El puntero apunta a None

# class ListaEnlazada:
#     def __init__(self):
#         self.cabeza = None

# def es_vacio(self):
#     return self.cabeza is None  # Devuelve True si la cabeza es None
# def agregar_nodo(self, data):
#     nuevo_nodo = Node(data) # Creamos un nuevo nodo
#     if self.es_vacio(): # Si la lista está vacía
#         self.cabeza = nuevo_nodo # La cabeza apunta al nuevo nodo
#     else:
#         nodo_actual = self.cabeza # Nodo actual apunta a la cabeza
#         while nodo_actual.next is not None: # Mientras nodo_actual.next no sea None-next es como nombramos al puntero
#             nodo_actual = nodo_actual.next   
#         nodo_actual.next = nuevo_nodo

# def eliminar_nodo(self, dato):
#     nodo_actual = self.cabeza #lista temporal
#     if nodo_actual == dato:
#         self.cabeza = nodo_actual.next
#         return

#     while nodo_actual.next is not None:
#         if nodo_actual.next.data == dato:
#             nodo_actual.next = nodo_actual.next.next
#             return
#         nodo_actual = nodo_actual.next
    
from typing import Optional

class Node:
    def __init__(self, data: int):
        self.data = data
        self.next :Optional["Node"]= None

class ListaEnlazada:
    def __init__(self)-> None:
        self.cabeza : Optional["Node"]= None
    def agregar(self, numero: int)-> None:
        nuevo_nodo:Node = Node(numero)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.next is not None:
                nodo_actual = nodo_actual.next
            nodo_actual.next = nuevo_nodo
lista=ListaEnlazada()
lista.agregar(5)
lista.agregar(10)
lista.agregar(15)
lista.agregar(20)
lista.agregar(25)
lista.agregar(30)
