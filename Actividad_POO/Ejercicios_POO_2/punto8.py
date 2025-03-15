class Estudiante:
    def __init__(self, nombre: str, edad: int, curso: str):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = []

    def agregar_calificacion(self, calificacion: float):
        self.calificaciones.append(calificacion)

    def calcular_promedio(self) -> float:
        if len(self.calificaciones) == 0:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)

    def determinar_estado(self) -> str:
        return "Aprobado" if self.calcular_promedio() >= 3.0 else "Reprobado"

nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
curso = input("Ingrese el curso del estudiante: ")

estudiante = Estudiante(nombre, edad, curso)


total_calificaciones = int(input("¿Cuántas calificaciones desea ingresar?: "))
for _ in range(total_calificaciones):
    calificacion = float(input("Ingrese una calificación: "))
    estudiante.agregar_calificacion(calificacion)


print(f"Promedio: {estudiante.calcular_promedio()}")
print(f"Estado: {estudiante.determinar_estado()}")