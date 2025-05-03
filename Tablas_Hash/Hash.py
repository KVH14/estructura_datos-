class TablaHashLibreta:
    # Inicializa la tabla hash con un tamaño predeterminado y un contador
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.tabla = [] 
        self.contador = 0

    # Agrega un nuevo contacto a la tabla0
    # Muestra todos los contactos en la tabla
    def mostrar(self):
        print("\nDirectorio Telefónico:")
        for i in range(self.tamaño):
            lista = self.tabla[i]
            if lista:
                clave, valor, hash_clave = lista
                print(f"   Índice {i} | Hash: {hash_clave} → {clave}: {valor}")
            else:
                print(f"   Índice {i}: Vacío")
    
    # Busca un contacto por su clave
    def buscar(self, clave: str):
        for i in range(self.tamaño):
            lista = self.tabla[i]
            if lista and lista[0] == clave:
                clave, valor, hash_clave = lista
                print(f"\nContacto encontrado:")
                print(f"   Nombre  : {clave}")
                print(f"   Teléfono: {valor}")
                print(f"   Hash    : {hash_clave}")
                print(f"   Índice  : {i}")
                return
        print("\nContacto no encontrado.")
    
    # Elimina un contacto por su clave
    def eliminar(self, clave: str):
        for i in range(self.tamaño):
            lista = self.tabla[i]
            if lista and lista[0] == clave:
                self.tabla[i] = None
                print(f"\nContacto {clave} eliminado.")
                return
        print("\nContacto no encontrado.")
    
    # Lista todos los contactos almacenados
    def listar(self):
        contactos = [lista for lista in self.tabla if lista]
        if contactos:
            print("\nLista de contactos:")
            for clave, valor, _ in contactos:
                print(f"   {clave}: {valor}")
        else:
            print("\nNo hay contactos guardados.")

# Creación de la tabla hash para gestionar los contactos
tabla = TablaHashLibreta()

# Menú de opciones para interactuar con la tabla
while True:
    opcion = input("\nSeleccione una opción: agregar, buscar, eliminar, listar, salir: ").lower()
    if opcion == 'salir':
        break
    elif opcion == 'agregar':
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        tabla.agregar(nombre, telefono)
    elif opcion == 'buscar':
        nombre_buscar = input("Ingrese el nombre del contacto a buscar: ")
        tabla.buscar(nombre_buscar)
    elif opcion == 'eliminar':
        nombre_eliminar = input("Ingrese el nombre del contacto a eliminar: ")
        tabla.eliminar(nombre_eliminar)
    elif opcion == 'listar':
        tabla.listar()
    else:
        print("Opción no válida.")
