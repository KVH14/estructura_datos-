class Empleado:
    def __init__(self, nombre: str, salario: float, departamento: str):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def trabajar(self):
        print(f"{self.nombre} está trabajando en el departamento de {self.departamento}.")

class Gerente(Empleado):
    def __init__(self, nombre: str, salario: float, departamento: str, equipo: list):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo

    def trabajar(self):
        print(f"{self.nombre} está supervisando a su equipo en el departamento de {self.departamento}.")

class Desarrollador(Empleado):
    def __init__(self, nombre: str, salario: float, departamento: str, lenguajeDeProgramacion: str):
        super().__init__(nombre, salario, departamento)
        self.lenguajeDeProgramacion = lenguajeDeProgramacion

    def trabajar(self):
        print(f"{self.nombre} está escribiendo código en {self.lenguajeDeProgramacion}.")


nombre = input("Ingrese el nombre del empleado: ")
salario = float(input("Ingrese el salario del empleado: "))
departamento = input("Ingrese el departamento del empleado: ")
tipo_empleado = input("Es Gerente o Desarrollador? (G/D): ").upper()

if tipo_empleado == "G":
    equipo = input("Ingrese los nombres del equipo separados por coma: ").split(',')
    empleado = Gerente(nombre, salario, departamento, equipo)
elif tipo_empleado == "D":
    lenguaje = input("Ingrese el lenguaje de programación: ")
    empleado = Desarrollador(nombre, salario, departamento, lenguaje)
else:
    empleado = Empleado(nombre, salario, departamento)

empleado.trabajar()
