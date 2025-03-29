from pydantic import BaseModel

class Ticket(BaseModel):
    name: str  # name of the person
    type: str  # type of consultation
    identity: int  # identity card
    case_description: str  # description of the case
    age: int  # age of the person
    priority_attention: bool = None  # None if not provided

    def __init__(self, **data): #lo que hace ** es recibir un diccionario en este caso el diccionario que resive va a hacer el de ticket 
        #data es como una variable que almacena los datos de un Ticket, pero en forma de diccionario.
        if "priority_attention" not in data or data["priority_attention"] is None:
            data["priority_attention"] = data.get("age", 0) >= 60 # ¿que hace esto? si no hay un valor de prioridad en el diccionario, se le asigna el valor de True o False dependiendo de la edad
        # Esto es para que la edad mayor a 60 años tenga prioridad
        super().__init__(**data)# llama al constructor de BaseModel, pasando los datos ya procesados.