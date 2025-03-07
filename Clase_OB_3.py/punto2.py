class FiguraGeometrica:
    def calcular_area(self) -> float:
        pass  # Método que será implementado en las clases hijas

class Triangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        self.base: float = base
        self.altura: float = altura
    
    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado: float):
        self.lado: float = lado
    
    def calcular_area(self) -> float:
        return self.lado * self.lado


print("Seleccione la figura geométrica:")
print("1. Triángulo")
print("2. Cuadrado")
opcion: int = int(input("Ingrese el número de la figura: "))

if opcion == 1:
    base: float = float(input("Ingrese la base del triángulo: "))
    altura: float = float(input("Ingrese la altura del triángulo: "))
    figura: Triangulo = Triangulo(base, altura)
    print(f"El área del triángulo es: {figura.calcular_area()}")

elif opcion == 2:
    lado: float = float(input("Ingrese el lado del cuadrado: "))
    figura: Cuadrado = Cuadrado(lado)
    print(f"El área del cuadrado es: {figura.calcular_area()}")

else:
    print("Opción no válida.")