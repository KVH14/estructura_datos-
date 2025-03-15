class Vehiculo:
   marca:str
   modelo:int

   def __init__(self,marca:str,combustible:int,tipo:str):
       self.marca=marca
       self.combustible=combustible
   def __str__(self)->str:
        return f"la Marca del vehiculo es : {self.marca} y el nivel de combustible es: {self.combustible}"
    

   def encender(self):
       pass
   def acelerar(self):
       pass
   def frenar(self):
         pass
   def apagar(self):
       pass


class Moto(Vehiculo):
    pass
class Carro(Vehiculo):
    pass

vehiculo1=Vehiculo("Mazda",80)
print(vehiculo1)

moto1=Moto("Honda",50)
print(moto1)

carro1=Carro("Renault",100)
print(carro1)