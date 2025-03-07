class Vehiculo:
   marca:str
   modelo:int
   tipo:str

   def __init__(self,marca:str,combustible:int,tipo:str):
       self.marca=marca
       self.combustible=combustible
       self.tipo=tipo

   def __str__(self)->str:
       return f"la Marca del vehiculo es : {self.marca}, el nivel de combustible es: {self.combustible}  y el tipo de vehiculo es: {self.tipo}"
    
  

   def encender(self):
        if self.combustible < 10:
            return "El vehículo tiene nivel bajo de combustible."
        else:
            return "El vehículo tiene nivel alto de combustible."
   
    
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

vehiculo1 = Vehiculo("Mazda", 80, "Deportivo")
print(vehiculo1)
print(vehiculo1.encender())

moto1 = Moto("Honda", 50, "Deportivo")
print(moto1)
print(moto1.encender())

carro1 = Carro("Renault", 100, "Carro")
print(carro1)
print(carro1.encender())
