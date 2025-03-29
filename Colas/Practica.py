#Colas:son estructuras lineales que siguen el principio FIFO (First In, First Out), es decir, el primer elemento en entrar es el primero en salir.
#El primero que llega va a estar en la parte superior y el último en la parte inferior
# ________      
# |  10  |
# |______|
# |  20  |
# |______|
# |  30  |
#Cola simple: es una cola en la que el último nodo apunta al primero, formando un ciclo
#Cola de prioridad: es una cola en la que cada nodo tiene un valor numérico que indica su prioridad, de manera que los nodos con mayor prioridad se atienden primero
#cola circular: es una cola en la que el último nodo apunta al primero, formando un ciclo
#cola de doble prioridad: es una cola en la que cada nodo tiene dos valores numéricos que indican su prioridad, de manera que los nodos con mayor prioridad se atienden primero
#Las colas se utilizan en sistemas operativos para administrar procesos, en la impresión de documentos, en la atención de clientes, entre otros.
#Operaciones básicas de una cola:       
#Enqueue: Agrega un elemento a la cola.
#Dequeue: Elimina el primer elemento agregado a la cola.
#Front: Devuelve el primer elemento de la cola sin eliminarlo.
#IsEmpty: Verifica si la cola está vacía.
#Size: Devuelve la cantidad de elementos en la cola.

enqueue: str = "Agregar un elemento a la cola"
dequeue: str = "Eliminar el primer elemento de la cola"
front: str = "Mostrar el primer elemento" 
isEmpty: str = "Verificar si la cola está vacía"
size: str = "Devolver la cantidad de elementos en la cola"