import tkinter as tk
import random
from tkinter import messagebox


class LaberintoSimple:
    def __init__(self, filas, columnas, nivel):
        self.filas = filas
        self.columnas = columnas
        self.nivel = nivel        
        # Inicializar laberinto con todas las paredes
        # True = hay pared, False = no hay pared
        self.paredes = [[[True for _ in range(4)] for _ in range(columnas)] for _ in range(filas)]
        # Crear el laberinto
        self.crear_laberinto()
    
    def crear_laberinto(self): #Laberinto con DFS

        visitadas = set()
        pila = [(0, 0)]  # Comenzar desde la esquina superior izquierda
        visitadas.add((0, 0))
        
        while pila:
            fila_actual, col_actual = pila[-1] #el último elemento de la pila
            vecinos = self.obtener_vecinos_no_visitados(fila_actual, col_actual, visitadas) # obtener vecinos no visitados
            
            if vecinos:
                fila_vecino, col_vecino = random.choice(vecinos) # Elegir un vecino aleatoriamente
                self.quitar_pared(fila_actual, col_actual, fila_vecino, col_vecino) # Quitar la pared entre la celda actual y el vecino
                visitadas.add((fila_vecino, col_vecino)) # Marcar vecino como visitado y agregarlo a la pila
                pila.append((fila_vecino, col_vecino))
            else:
                pila.pop()# No hay vecinos no visitados, retroceder
        
        self.ajustar_dificultad()
    
    def obtener_vecinos_no_visitados(self, fila, col, visitadas):

        vecinos = []
        # Arriba
        if fila > 0 and (fila - 1, col) not in visitadas:
            vecinos.append((fila - 1, col))
        # Abajo
        if fila < self.filas - 1 and (fila + 1, col) not in visitadas:
            vecinos.append((fila + 1, col))
        
        # Derecha
        if col < self.columnas - 1 and (fila, col + 1) not in visitadas:
            vecinos.append((fila, col + 1))
        # Izquierda
        if col > 0 and (fila, col - 1) not in visitadas:
            vecinos.append((fila, col - 1))
        
        return vecinos
    
    def quitar_pared(self, fila1, col1, fila2, col2):
        # Determinar la dirección
        if fila1 == fila2:  # Movimiento horizontal
            if col1 < col2:  # Movimiento hacia la derecha
                self.paredes[fila1][col1][2] = False  # Quitar pared derecha de celda1
                self.paredes[fila2][col2][3] = False  # Quitar pared izquierda de celda2
            else:  # Movimiento hacia la izquierda
                self.paredes[fila1][col1][3] = False  # Quitar pared izquierda de celda1
                self.paredes[fila2][col2][2] = False  # Quitar pared derecha de celda2
        else:  # Movimiento vertical
            if fila1 < fila2:  # Movimiento hacia abajo
                self.paredes[fila1][col1][1] = False  # Quitar pared abajo de celda1
                self.paredes[fila2][col2][0] = False  # Quitar pared arriba de celda2
            else:  # Movimiento hacia arriba
                self.paredes[fila1][col1][0] = False  # Quitar pared arriba de celda1
                self.paredes[fila2][col2][1] = False  # Quitar pared abajo de celda2
    
    def ajustar_dificultad(self):
        if self.nivel <= 2:
            # Niveles fáciles: agregar algunos caminos extra
            num_caminos_extra = int(self.filas * self.columnas * 0.05)
        else:
            # Niveles difíciles: agregar más caminos alternativos
            num_caminos_extra = int(self.filas * self.columnas * 0.1)
        
        # Agregar caminos extra aleatoriamente
        for _ in range(num_caminos_extra):
            fila = random.randint(1, self.filas - 2)
            col = random.randint(1, self.columnas - 2)
            
            # Elegir una dirección aleatoria para quitar una pared
            direccion = random.randint(0, 3)
            
            if direccion == 0 and fila > 0:  # Arriba
                self.paredes[fila][col][0] = False
                self.paredes[fila - 1][col][1] = False
            elif direccion == 1 and fila < self.filas - 1:  # Abajo
                self.paredes[fila][col][1] = False
                self.paredes[fila + 1][col][0] = False
            elif direccion == 2 and col < self.columnas - 1:  # Derecha
                self.paredes[fila][col][2] = False
                self.paredes[fila][col + 1][3] = False
            elif direccion == 3 and col > 0:  # Izquierda
                self.paredes[fila][col][3] = False
                self.paredes[fila][col - 1][2] = False
    
    def puede_moverse(self, fila, col, direccion):

        if direccion == 0:  # Arriba
            return not self.paredes[fila][col][0] and fila > 0
        elif direccion == 1:  # Abajo
            return not self.paredes[fila][col][1] and fila < self.filas - 1
        elif direccion == 2:  # Derecha
            return not self.paredes[fila][col][2] and col < self.columnas - 1
        elif direccion == 3:  # Izquierda
            return not self.paredes[fila][col][3] and col > 0
        return False
    
    def obtener_movimientos_posibles(self, fila, col):
        movimientos = []
        
        if self.puede_moverse(fila, col, 0):  # Arriba
            movimientos.append((fila - 1, col))
        if self.puede_moverse(fila, col, 1):  # Abajo
            movimientos.append((fila + 1, col))
        if self.puede_moverse(fila, col, 2):  # Derecha
            movimientos.append((fila, col + 1))
        if self.puede_moverse(fila, col, 3):  # Izquierda
            movimientos.append((fila, col - 1))
        
        return movimientos





