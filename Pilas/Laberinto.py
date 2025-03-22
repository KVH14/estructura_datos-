# Resolver un laberinto usando una pila (estructura tipo stack)

# Definición del laberinto (0 = camino, 1 = pared)
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# Definir punto de inicio y punto de llegada
inicio = (0, 0)
fin = (4, 4)

# Dimensiones del laberinto
filas = len(laberinto)
columnas = len(laberinto[0])

# Movimientos posibles: Derecha, Abajo, Izquierda, Arriba
movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Implementación de la resolución del laberinto utilizando una pila
def resolver_laberinto(laberinto, inicio, fin):
    
    # Resuelve un laberinto utilizando una pila (backtracking).
    
    # Parámetros:
    # - laberinto: Lista de listas de enteros (0 = camino, 1 = pared).
    # - inicio: Tupla con la posición inicial (fila, columna).
    # - fin: Tupla con la posición final (fila, columna).
    
    # Retorna:
    # - Una lista con el camino desde inicio hasta fin, o None si no hay solución.

    pila = [inicio]  # Inicializar la pila con el punto de inicio
    visitado = set()  # Conjunto para rastrear posiciones visitadas
    
    while pila:
        x, y = pila[-1]  # Obtener la última posición en la pila
        
        if (x, y) == fin:  # Si llegamos al destino
            return pila  # Devolver el camino encontrado
        
        visitado.add((x, y))  # Marcar la posición como visitada
        
        camino_encontrado = False  # Bandera para verificar si hay movimientos válidos
        
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy  # Nueva posición a evaluar
            
            # Verificar si la nueva posición es válida y no ha sido visitada
            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] == 0 and (nx, ny) not in visitado:
                pila.append((nx, ny))  # Agregar la nueva posición a la pila
                camino_encontrado = True  # Marcar que encontramos un camino
                break  # Seguir explorando
        
        if not camino_encontrado:
            pila.pop()  # Retroceder si no hay movimientos válidos
    
    return None  # No se encontró un camino válido

# Llamar a la función para resolver el laberinto
trayectoria = resolver_laberinto(laberinto, inicio, fin)

# Imprimir el resultado
if trayectoria:
    print("Camino encontrado:", trayectoria)
else:
    print("No hay solución")
