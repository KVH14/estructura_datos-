import random
from collections import deque
from generador import GeneradorLaberintos

class Laberinto:
    """Clase que maneja la lógica del laberinto con ambos generadores (neuronal y DFS)"""
    
    def __init__(self, filas, columnas, usar_neuronal=True):
        """
        Inicializa el laberinto
        Args:
            filas: número de filas del laberinto
            columnas: número de columnas del laberinto
            usar_neuronal: si True, intenta usar el generador neuronal primero
        """
        self.filas = filas
        self.columnas = columnas
        self.usar_neuronal = usar_neuronal
        self.generador_neuronal = GeneradorLaberintos(filas, columnas) if usar_neuronal else None
        self.grid = self.generar_laberinto()
        self.entrada = (1, 0)
        self.salida = (filas-2, columnas-1)
        self.solucion = self.encontrar_solucion()
    
    
    def generar_laberinto(self):
     """Intenta generar un laberinto con IA; si falla, usa DFS"""
     if self.usar_neuronal and self.generador_neuronal:
        for _ in range(10):  # Intenta varias veces
            grid = self.generador_neuronal.generar_laberinto()
            if self.verificar_solucion(grid):
                print("✔️ Laberinto generado con IA.")
                return grid
        print("Falló la IA. Se usa DFS.")
    
     return self.generar_con_dfs()

    def generar_con_dfs(self):
        """Generación tradicional con DFS iterativo"""
        grid = [[1 for _ in range(self.columnas)] for _ in range(self.filas)]
        stack = [(1, 1)]
        grid[1][1] = 0
        
        while stack:
            x, y = stack[-1]
            vecinos = []
            
            # Explorar vecinos a 2 celdas de distancia
            for dx, dy in [(-2,0),(2,0),(0,-2),(0,2)]:
                nx, ny = x+dx, y+dy
                if 0 < nx < self.filas-1 and 0 < ny < self.columnas-1 and grid[nx][ny] == 1:
                    # Verificar que no cree ciclos
                    vecinos_disponibles = 0
                    for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                        if 0 <= nx+di < self.filas and 0 <= ny+dj < self.columnas:
                            if grid[nx+di][ny+dj] == 0:
                                vecinos_disponibles += 1
                    if vecinos_disponibles <= 1:  # Evita crear múltiples caminos
                        vecinos.append((nx, ny, dx//2, dy//2))
            
            if vecinos:
                nx, ny, px, py = random.choice(vecinos)
                grid[x+px][y+py] = 0  # Conecta la celda actual con la nueva
                grid[nx][ny] = 0      # Marca la nueva celda como camino
                stack.append((nx, ny))
            else:
                stack.pop()
        
        # Asegurar entrada y salida
        grid[1][0] = 0
        grid[self.filas-2][self.columnas-1] = 0
        return grid
    
    def verificar_solucion(self, grid):
        """Verifica si el laberinto generado tiene solución"""
        entrada = (1, 0)
        salida = (self.filas-2, self.columnas-1)
        visitados = set()
        cola = deque([entrada])
        
        while cola:
            i, j = cola.popleft()
            if (i, j) == salida:
                return True
            
            for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i+di, j+dj
                if (0 <= ni < self.filas and 0 <= nj < self.columnas and 
                    grid[ni][nj] == 0 and (ni,nj) not in visitados):
                    visitados.add((ni,nj))
                    cola.append((ni,nj))
        return False
    
    def encontrar_solucion(self):
        """Encuentra la solución usando BFS y la almacena"""
        entrada = self.entrada
        salida = self.salida
        visitados = set()
        cola = deque([(entrada, [entrada])])  # Almacena el camino completo
        visitados.add(entrada)
        
        while cola:
            pos, camino = cola.popleft()
            
            if pos == salida:
                return camino
            
            for vecino in self.obtener_vecinos(pos):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, camino + [vecino]))
        
        return None
    
    def obtener_vecinos(self, posicion):
        """Devuelve las celdas accesibles desde una posición dada"""
        i, j = posicion
        vecinos = []
        
        # Movimientos posibles (arriba, abajo, izquierda, derecha)
        for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < self.filas and 0 <= nj < self.columnas and self.grid[ni][nj] == 0:
                vecinos.append((ni, nj))
        
        return vecinos
    
    def dibujar_ascii(self):
        """Muestra una representación ASCII del laberinto (para depuración)"""
        for i in range(self.filas):
            fila = ''
            for j in range(self.columnas):
                if (i,j) == self.entrada:
                    fila += 'E'
                elif (i,j) == self.salida:
                    fila += 'S'
                elif self.grid[i][j] == 1:
                    fila += '#'
                else:
                    fila += ' '
            print(fila)