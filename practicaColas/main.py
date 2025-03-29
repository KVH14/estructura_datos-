from typing import Union
from fastapi import FastAPI
from model.ticket import Ticket
from controller.ticketController import TicketController
from functions.queueFunctions import add_queue
from typing import List # Importamos List(que es una lista) para poder usarlo en la función de crear turnos

app = FastAPI()

ticketTypes = {
    #Se crea un diccionario ticketTypes, donde cada clave representa un tipo de atención y su valor es una instancia
    "duda",
    "asesor",
    "caja",
    "otros"
}

# Endpoint para crear un turno
# @app.post("/ticketCreateBatch") 
# #POST en la ruta "/ticketCreateBatch"
# def crear_turnos_batch(turnos: List[Ticket]):
#     #Funcion para crear turnos en batch donde se recibe una lista de turnos donde el usuario enviará varios tickets en una sola solicitud
#     for turno in turnos:
#     #Recorre uno por uno los tickets de la lista turnos
#         add_queue(turno, ticketTypes)
#         # Agregar cada ticket a la cola
#     return {"mensaje": "Tickets agregados correctamente", "total": len(turnos)}

#     # Aquí podrías agregar la lógica para guardar el turno en una base de datos

@app.post("/ticketCreateBatch")
def crear_turnos_batch(turnos: List[Ticket]):
    return {"mensaje": "Tickets agregados correctamente", "total": len(turnos)}   

# Endpoint para obtener el siguiente turno
#GET en la ruta "/ticketNext"
@app.get("/ticketNext")
#devuelve el siguiente ticket con la mayor prioridad
def obtener_siguiente_turno():
    highest_priority_ticket = None #Guarda el ticket con mayor prioridad.
    highest_priority_type = None # Guarda el tipo de atención (ej. "caja", "dudas", etc.)

    for type, queue in ticketTypes.items(): #Devuelve todo lo de ticket
        if not queue.is_empty(): #revisa si la cola tiene tickets pendientes.
            candidate_ticket = queue.peek() #ara obtener el primer ticket sin sacarlo de la cola.
            # Si no hay ticket con mayor prioridad o el ticket actual tiene prioridad de atención
            if highest_priority_ticket is None or candidate_ticket.priority_attention:
                highest_priority_ticket = candidate_ticket #Si el ticket actual tiene prioridad, lo guardamo
                highest_priority_type = type # guardamos su tipo
    # Si no hay tickets en ninguna cola
    if highest_priority_ticket is None:
        return {"mensaje": "No hay tickets en ninguna cola."}
    #elimina el primer ticket de la cola en la que estaba
    ticketTypes[highest_priority_type].dequeue()

    #Devolver la información del ticket seleccionado
    return {
        "mensaje": "El siguiente turno es",
        "datos_turno": {
            "name": highest_priority_ticket.name, 
            "identity": highest_priority_ticket.identity,  
            "age": highest_priority_ticket.age,  
            "priority_attention": highest_priority_ticket.priority_attention
        }
    }


# Endpoint para listar los turnos en cola por el tipo de turno
#GET en la ruta "/ticketList"
@app.get("/ticketList")
#la función que se encargará de listar los turnos en la cola.
def listar_turnos_cola():

#Crear una lista vacía 
    queue = []

# Recorre cada tipo de ticket en ticketTypes
    for type, queue_controller in ticketTypes.items():
        current = queue_controller.head # Obtiene el primer nodo de la cola
        while current:
            queue.append({
                "name": current.data.name,
                "identity": current.data.identity,
                "age": current.data.age,
                "priority_attention": current.priority,
                "tipo": type  # Agregamos el tipo de atención para identificar la cola
            })
            current = current.next # Avanza al siguiente nodo

    # Ordenamos la lista por prioridad (True primero)
    queue.sort(key=lambda x: x["priority_attention"], reverse=True)
    # .sort() se usa para ordenar listas en Python.
    #Se colocan 2 parametros:
    #  key= → Indica la clave de ordenamiento.
    #  reverse=True → Ordena de mayor a menor.
    return {"mensaje": "Lista de todos los turnos en cola ordenados por prioridad", "datos_turnos": queue if queue else "No hay turnos en cola"}
# Otros endpoints existentes
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
