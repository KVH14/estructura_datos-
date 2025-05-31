
class Nodo:
    def __init__(self, fila, columna, anterior=None):
        self.fila = fila            # Coordenada fila de la posición
        self.columna = columna      # Coordenada columna de la posición
        self.anterior = anterior    # Referencia al nodo anterior (camino recorrido)


class Pila:
    def __init__(self):
        self.cima = None  # Referencia al nodo en la cima de la pila (el último apilado)
        
    def esta_vacia(self):
        return self.cima is None

    def apilar(self, fila, columna):
        nuevo = Nodo(fila, columna, self.cima)# Crea un nuevo nodo con la posición actual y lo coloca en la cima
        self.cima = nuevo

    def desapilar(self):
       
        if self.esta_vacia(): # Quita y retorna el nodo en la cima de la pila, si no está vacía
            return None  
        actual = self.cima
        self.cima = self.cima.anterior  # Actualiza la cima al nodo anterior
        return actual  # Devuelve el nodo desapilado

    def ver_cima(self):
        return self.cima # Retorna el nodo en la cima de la pila sin desapilarlo

    def camino_completo(self):
        camino = [] # Devuelve la lista del camino desde el inicio hasta la posición actual
        actual = self.cima
        while actual:
            camino.append((actual.fila, actual.columna))  # Añade la posición actual
            actual = actual.anterior  # Avanza hacia el nodo anterior
        return camino[::-1]  # Invierte la lista para que sea del inicio al fin


def resolver_laberinto(laberinto, inicio, fin):
    filas = len(laberinto)          
    columnas = len(laberinto[0]) 
    visitado = [[False]*columnas for _ in range(filas)] # Matriz para marcar las posiciones ya visitadas
    pila = Pila()                 

    # Movimientos posibles: derecha, abajo, izquierda, arriba
    dx_dy = [(0,1), (1,0), (0,-1), (-1,0)]

    fila_ini, col_ini = inicio     # Coordenadas de inicio
    fila_fin, col_fin = fin        # Coordenadas de destino

    pila.apilar(fila_ini, col_ini)    # Apilamos la posición inicial
    visitado[fila_ini][col_ini] = True  # Marcamos como visitada

    while not pila.esta_vacia():
        actual = pila.ver_cima()     # Obtenemos la posición actual (cima de la pila)
        f = actual.fila
        c = actual.columna
        if (f, c) == (fila_fin, col_fin): # Si llegamos a la posición final, devolvemos el camino completo
            return pila.camino_completo()
        # Revisamos todas las direcciones posibles
        for dx, dy in dx_dy:
            nuevafi, nuevaco = f + dx, c + dy  # Calculamos nueva fila y columna
    
            if 0 <= nuevafi < filas and 0 <= nuevaco < columnas: # Verificamos que la nueva posición esté dentro del laberinto
                # Verificamos que sea un camino (0) y no haya sido visitado
                if laberinto[nuevafi][nuevaco] == 0 and not visitado[nuevafi][nuevaco]:
                    pila.apilar(nuevafi, nuevaco)         # Apilamos la nueva posición
                    visitado[nuevafi][nuevaco] = True     # Marcamos como visitada
                    se_movio = True             # Indicamos que nos movimos
                    break                      # Salimos del ciclo para explorar desde la nueva posición

        # Si no hubo movimiento, significa que estamos en callejón sin salida
        if not se_movio:
            pila.desapilar()  # Retrocedemos quitando la posición actual

    return None  # No se encontró camino al final del laberinto

# Ejemplo de laberinto (0 = camino libre, 1 = pared)
laberinto = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
]

inicio = (0, 0)  # Punto de inicio en la esquina superior izquierda
fin = (3, 3)     # Punto final en la esquina inferior derecha

# Resolver el laberinto
camino = resolver_laberinto(laberinto, inicio, fin)

# Mostrar resultado
if camino:
    print("Camino encontrado:")
    for paso in camino:
        print(f"({paso[0]}, {paso[1]})", end=" ")
else:
    print("No hay solución.")

