class NodoPosicion:
    """Clase que representa una posición en el laberinto con referencia al nodo anterior"""
    def __init__(self, x: int, y: int, anterior=None):
        self.x = x              # Coordenada x (fila)
        self.y = y              # Coordenada y (columna)
        self.anterior = anterior  # Referencia al nodo anterior en el camino

class PilaLaberinto:
    """Implementación de pila para el laberinto usando nodos"""
    def __init__(self):
        self.tope = None  # Nodo en la cima de la pila
        self.tamano = 0   # Tamaño actual de la pila
    
    def esta_vacia(self) -> bool:
        """Verifica si la pila está vacía"""
        return self.tope is None
    
    def apilar(self, x: int, y: int):
        """Agrega una nueva posición a la pila"""
        nuevo_nodo = NodoPosicion(x, y, self.tope)
        self.tope = nuevo_nodo
        self.tamano += 1
    
    def desapilar(self) -> tuple[int, int]:
        """Elimina y devuelve la posición en el tope de la pila"""
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        posicion = (self.tope.x, self.tope.y)
        self.tope = self.tope.anterior
        self.tamano -= 1
        return posicion
    
    def ver_tope(self) -> tuple[int, int]:
        """Devuelve la posición en el tope sin eliminarla"""
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return (self.tope.x, self.tope.y)
    
    def obtener_camino(self) -> list[tuple[int, int]]:
        """Reconstruye el camino desde el tope hasta el inicio"""
        camino = []
        actual = self.tope
        while actual is not None:
            camino.append((actual.x, actual.y))
            actual = actual.anterior
        return camino[::-1]  # Invertir para que sea inicio -> fin

def resolver_laberinto_con_nodos(laberinto: list[list[int]], 
                                inicio: tuple[int, int], 
                                fin: tuple[int, int]) -> list[tuple[int, int]] | None:
    """
    Resuelve un laberinto usando una pila implementada con nodos.
    
    Args:
        laberinto: Matriz donde 0 es camino y 1 es pared
        inicio: Tupla (fila, columna) de inicio
        fin: Tupla (fila, columna) de destino
        
    Returns:
        Lista de tuplas con el camino o None si no hay solución
    """
    # Movimientos posibles (derecha, abajo, izquierda, arriba)
    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Inicializar pila con nodo de inicio
    pila = PilaLaberinto()
    pila.apilar(inicio[0], inicio[1])
    
    # Matriz para marcar posiciones visitadas
    visitado = [[False for _ in range(len(laberinto[0]))] 
               for _ in range(len(laberinto))]
    visitado[inicio[0]][inicio[1]] = True
    
    while not pila.esta_vacia():
        x, y = pila.ver_tope()
        
        # Verificar si llegamos al destino
        if (x, y) == fin:
            return pila.obtener_camino()
        
        # Buscar movimientos válidos
        movimiento_valido = False
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            
            # Verificar si la nueva posición es válida
            if 0 <= nx < len(laberinto) and (0 <= ny < len(laberinto[0])):
                if laberinto[nx][ny] == 0 and not visitado[nx][ny]:
                    pila.apilar(nx, ny)
                    visitado[nx][ny] = True
                    movimiento_valido = True
                    break
        
        # Si no hay movimientos válidos, retroceder
        if not movimiento_valido:
            pila.desapilar()
    
    return None  # No se encontró solución

# Definición del laberinto (0 = camino, 1 = pared)
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Puntos de inicio y fin
inicio = (0, 0)
fin = (4, 4)

# Resolver el laberinto
solucion = resolver_laberinto_con_nodos(laberinto, inicio, fin)

# Mostrar resultados
if solucion:
    print("Camino encontrado:")
    for paso in solucion:
        print(f"-> ({paso[0]}, {paso[1]})", end=" ")
    print("\nRepresentación gráfica:")
    
    # Mostrar laberinto con el camino marcado
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if (i, j) in solucion:
                print("X", end=" ")  # Marcar el camino
            else:
                print(laberinto[i][j], end=" ")
        print()
else:
    print("No se encontró solución para el laberinto")