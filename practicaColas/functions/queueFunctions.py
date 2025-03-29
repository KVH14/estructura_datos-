from model.ticket import Ticket
from controller.ticketController import TicketController

def add_queue(ticket: Ticket, ticketTypes: dict) -> None: #Función para agregar un ticket a la cola correcta
    """
    Add a ticket to the queue, using the TicketController class to manage the queue.
    you need order the tickets by type and priority. (dudas, asesor, caja, otros)
    """
    # Define los ticket types
    atencion:{
        "duda",
        "caja",
        "asesor",
        "otros"
    }
    #Verifica si el tipo de ticket (ticket.type) está en ticketTypes
    if ticket.type not in atencion:
        print("Tipo de ticket no válido")
        return
    if ticket.type not in ticketTypes:
        ticketTypes[ticket.type] = TicketController.enqueue()
    # Agrega el ticket a la cola correspondiente
    ticketTypes[ticket.type].enqueue(ticket)   
    print(f"Ticket de tipo '{ticket.type}' Añadido a la cola")
