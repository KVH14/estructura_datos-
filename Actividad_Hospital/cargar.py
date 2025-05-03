import pandas as pd  # libreria

# Clase que representa un hospital con sus datos principales
class Hospital:
    def __init__(self, nombre: str, nit: int, sede: str, municipio: str):
        self.nombre = nombre           # Nombre del hospital
        self.nit = nit                 # Número de identificación tributaria
        self.sede = sede               # Sede del hospital
        self.municipio = municipio     # Municipio donde se ubica

    def __str__(self):
        # Devuelve una representación en texto del hospital
        return f"Nombre: {self.nombre}, NIT:{self.nit}, Sede:{self.sede}, Municipio:{self.municipio}"

# Nodo para el árbol binario de búsqueda (BST)
class Nodo:
    def __init__(self, hospital):
        self.hospital = hospital       # Contiene un objeto Hospital
        self.izquierda = None          # Nodo izquierdo
        self.derecha = None            # Nodo derecho

# Clase del árbol binario de búsqueda basado en NIT
class ArbolHospital:
    def __init__(self):
        self.raiz = None               # Nodo raíz del árbol

    # Inserta un hospital en el árbol según su NIT
    def insertar(self, hospital):
        if self.raiz is None:
            self.raiz = Nodo(hospital)
        else:
            self._insertar_recursivo(self.raiz, hospital)

    def _insertar_recursivo(self, nodo_actual, hospital):
        if hospital.nit < nodo_actual.hospital.nit:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(hospital)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, hospital)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(hospital)
            else:
                self._insertar_recursivo(nodo_actual.derecha, hospital)

    # Recorre el árbol in-order e imprime hospitales ordenados por NIT
    def inorden(self):
        self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierda)
            print(nodo.hospital)
            self._inorden_recursivo(nodo.derecha)

    # Busca un hospital por su NIT
    def buscar(self, nit_buscado):
        return self._buscar_recursivo(self.raiz, nit_buscado)

    def _buscar_recursivo(self, nodo, nit_buscado):
        if nodo is None:
            return None
        if nodo.hospital.nit == nit_buscado:
            return nodo.hospital
        elif nit_buscado < nodo.hospital.nit:
            return self._buscar_recursivo(nodo.izquierda, nit_buscado)
        else:
            return self._buscar_recursivo(nodo.derecha, nit_buscado)


# Carga el archivo CSV con pandas (ajusta la ruta si es necesario)
hospitales = pd.read_csv('/workspaces/estructura_datos-/Actividad_Hospital/Directorio_E.S.E._Hospitales_de_Antioquia_con_coordenadas_20250426.csv')

# Renombra columnas para que tengan nombres más fáciles de manejar
hospitales.rename(columns={
    'Razón Social Organización': 'nombre2',
    'Número NIT': 'nit',
    'Nombre Sede': 'sede',
    'Nombre Municipio': 'municipio'
}, inplace=True)

# Elimina comas del NIT y lo convierte a tipo entero
hospitales['nit'] = hospitales['nit'].str.replace(',', '')
hospitales['nit'] = hospitales['nit'].astype(int)

# Muestra una vista previa y los tipos de datos
print(hospitales.head())
print(hospitales.dtypes)

# CONSTRUCCIÓN DEL ÁRBOL 

# Crea una instancia del árbol
arbol = ArbolHospital()

# Recorre el DataFrame e inserta cada hospital en el árbol
for index, row in hospitales.iterrows():
    hospital = Hospital(
        nombre=row['nombre2'],
        nit=row['nit'],
        sede=row['sede'],
        municipio=row['municipio']
    )
    arbol.insertar(hospital)


print("HOSPITALES ORDENADOS POR NIT (inorden)")
arbol.inorden()

#BUSQUEDAD
# Solicita al usuario un NIT para buscar
try:
    nit_input = int(input("Ingrese el NIT del hospital que desea buscar: "))
    resultado = arbol.buscar(nit_input)
    if resultado:
        print("Hospital Encontrado")
        print(resultado)
    else:
        print("Hospital no encontrado.")
except ValueError:
    print("Error: Ingrese un número válido para el NIT.")
