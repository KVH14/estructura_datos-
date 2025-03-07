class Usuario:
    def __init__(self, nombre_usuario: str, contraseña: str):
        self.nombre_usuario: str = nombre_usuario
        self.contraseña: str = contraseña
    
    def iniciar_sesion(self, usuario: str, contraseña: str):
        if self.nombre_usuario == usuario and self.contraseña == contraseña:
            print(f"Inicio de sesión exitoso para {self.nombre_usuario}.")
        else:
            print("Nombre de usuario o contraseña incorrectos.")

class Administrador(Usuario):
    def __init__(self, nombre_usuario: str, contraseña: str):
        super().__init__(nombre_usuario, contraseña)
    
    def gestionar_usuarios(self):
        print(f"El administrador {self.nombre_usuario} está gestionando usuarios.")

class Cliente(Usuario):
    def __init__(self, nombre_usuario: str, contraseña: str):
        super().__init__(nombre_usuario, contraseña)
    
    def realizar_compra(self):
        print(f"El cliente {self.nombre_usuario} está realizando una compra.")


nombre: str = input("Ingrese su nombre de usuario: ")
contraseña: str = input("Ingrese su contraseña: ")

print("Seleccione su tipo de usuario:")
print("1. Administrador")
print("2. Cliente")
opcion: int = int(input("Ingrese el número correspondiente: "))

if opcion == 1:
    usuario: Administrador = Administrador(nombre, contraseña)
    usuario.iniciar_sesion(nombre, contraseña)
    usuario.gestionar_usuarios()

elif opcion == 2:
    usuario: Cliente = Cliente(nombre, contraseña)
    usuario.iniciar_sesion(nombre, contraseña)
    usuario.realizar_compra()

else:
    print("Opción no válida.")