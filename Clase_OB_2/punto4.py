class Circulo:
    def __init__(self, radio: float):
        self.radio = radio

    def calcular_area(self) -> float:
        return 3.1416 * (self.radio * self.radio)

    def calcular_circunferencia(self) -> float:
        return 2 * 3.1416 * self.radio


radio = float(input("Ingrese el radio del círculo: "))

circulo = Circulo(radio)
area = circulo.calcular_area()
circunferencia = circulo.calcular_circunferencia()
print(f"Área del círculo: {area:.2f}")
print(f"Circunferencia del círculo: {circunferencia:.2f}")