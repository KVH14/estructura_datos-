import random
from collections import deque

class GeneradorLaberintos:
    """Generador de laberintos usando DFS con opción de perturbaciones"""

    def __init__(self, filas=15, columnas=15):
        self.filas = filas
        self.columnas = columnas

    def ajustar_entrada_salida(self, grid):
        """Asegura que haya entrada y salida en el laberinto"""
        grid[1][0] = 0
        grid[self.filas - 2][self.columnas - 1] = 0

    def generar_con_dfs(self):
        """Generación básica de laberintos usando DFS"""
        grid = [[1] * self.columnas for _ in range(self.filas)]
        stack = [(1, 1)] #inicio en (1, 1)
        grid[1][1] = 0

        while stack:
            x, y = stack[-1]
            vecinos = []

            # Explora vecinos a dos pasos
            for dx, dy in [(-2,0), (2,0), (0,-2), (0,2)]:
                nx, ny = x + dx, y + dy
                if 0 < nx < self.filas - 1 and 0 < ny < self.columnas - 1 and grid[nx][ny] == 1:
                    vecinos.append((nx, ny, dx//2, dy//2))

            if vecinos:
                nx, ny, px, py = random.choice(vecinos)
                grid[x + px][y + py] = 0
                grid[nx][ny] = 0
                stack.append((nx, ny))
            else:
                stack.pop()

        self.ajustar_entrada_salida(grid)
        return grid

    def tiene_solucion(self, grid):
        """Comprueba si existe camino entre entrada y salida usando BFS"""
        entrada = (1, 0)
        salida = (self.filas - 2, self.columnas - 1)
        cola = deque([entrada])
        visitados = {entrada}

        while cola:
            i, j = cola.popleft()
            if (i, j) == salida:
                return True
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + di, j + dj
                if (0 <= ni < self.filas and 0 <= nj < self.columnas and
                    grid[ni][nj] == 0 and (ni, nj) not in visitados):
                    cola.append((ni, nj))
                    visitados.add((ni, nj))
        return False

    def generar_laberinto(self, perturbaciones=10, intentos=10):
        """Genera laberinto con perturbaciones sin perder la solución"""
        for _ in range(intentos):
            grid = self.generar_con_dfs()

            # Realiza perturbaciones aleatorias
            for _ in range(perturbaciones):
                i = random.randint(1, self.filas - 2)
                j = random.randint(1, self.columnas - 2)
                grid[i][j] = 1 - grid[i][j]  # Alterna muro/camino

            self.ajustar_entrada_salida(grid)

            if self.tiene_solucion(grid):
                return grid

        return self.generar_con_dfs()
