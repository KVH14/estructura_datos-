class Producto:
    def __init__(self, nombre: str, precio: float, cantidad_disponible: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def calcular_total(self, cantidad: int) -> float:
        if cantidad > self.cantidad_disponible:
            print("No hay suficiente stock disponible.")
            return 0.0
        return cantidad * self.precio


nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad_disponible = int(input("Ingrese la cantidad disponible: "))


producto = Producto(nombre, precio, cantidad_disponible)

cantidad_a_comprar = int(input("Ingrese la cantidad que desea comprar: "))
total = producto.calcular_total(cantidad_a_comprar)
if total > 0:
    print(f"Total a pagar por {cantidad_a_comprar} unidades de {nombre}: ${total:.2f}")
