class Electrodomestico:
    def __init__(self, marca: str, modelo: str, consumo_energetico: str):
        self.marca: str = marca
        self.modelo: str = modelo
        self.consumo_energetico: str = consumo_energetico
    
    def encender(self):
        print(f"El electrodoméstico {self.marca} modelo {self.modelo} está encendido.")

class Lavadora(Electrodomestico):
    def __init__(self, marca: str, modelo: str, consumo_energetico: str, capacidad: float):
        super().__init__(marca, modelo, consumo_energetico)
        self.capacidad: float = capacidad
    
    def encender(self):
        print(f"La lavadora {self.marca} modelo {self.modelo} está iniciando el ciclo de lavado.")

class Refrigerador(Electrodomestico):
    def __init__(self, marca: str, modelo: str, consumo_energetico: str, tiene_congelador: bool):
        super().__init__(marca, modelo, consumo_energetico)
        self.tiene_congelador: bool = tiene_congelador
    
    def encender(self):
        print(f"El refrigerador {self.marca} modelo {self.modelo} está regulando la temperatura.")

# Solicitar datos al usuario
print("Seleccione el electrodoméstico:")
print("1. Lavadora")
print("2. Refrigerador")
opcion: int = int(input("Ingrese el número del electrodoméstico: "))

marca: str = input("Ingrese la marca: ")
modelo: str = input("Ingrese el modelo: ")
consumo: str = input("Ingrese el consumo energético: ")

if opcion == 1:
    capacidad: float = float(input("Ingrese la capacidad de la lavadora en kg: "))
    electrodomestico: Lavadora = Lavadora(marca, modelo, consumo, capacidad)
    electrodomestico.encender()

elif opcion == 2:
    tiene_congelador: bool = input("¿Tiene congelador? (sí/no): ").strip().lower() == "sí"
    electrodomestico: Refrigerador = Refrigerador(marca, modelo, consumo, tiene_congelador)
    electrodomestico.encender()

else:
    print("Opción no válida.")
