import tkinter as tk
import random
import numpy as np
from tkinter import messagebox

# Configuración básica
TAM_CELDA = 40
MARGEN = 20
COLORES = {
    "inicio": "green",
    "meta": "red",
    "ruta": "blue",
    "jugador": "purple",
    "pared": "black"
}

class LaberintoSimple:
    def __init__(self, filas, columnas, nivel=1): 
        self.filas = filas
        self.columnas = columnas
        self.nivel = nivel      
        self.paredes = [[[True for _ in range(4)] for _ in range(columnas)] for _ in range(filas)]
        self.crear_laberinto()
    
    def crear_laberinto(self):
        """Crea el laberinto usando DFS"""
        visitadas = set()
        pila = [(0, 0)]
        visitadas.add((0, 0))
        
        while pila:
            fila_actual, col_actual = pila[-1]
            vecinos = self.obtener_vecinos_no_visitados(fila_actual, col_actual, visitadas)
            
            if vecinos:
                fila_vecino, col_vecino = random.choice(vecinos)
                self.quitar_pared(fila_actual, col_actual, fila_vecino, col_vecino)
                visitadas.add((fila_vecino, col_vecino))
                pila.append((fila_vecino, col_vecino))
            else:
                pila.pop()
        
        self.ajustar_dificultad()
    
    def obtener_vecinos_no_visitados(self, fila, col, visitadas):
        """Obtiene vecinos no visitados"""
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
        """Quita la pared entre dos celdas adyacentes"""
        if fila1 == fila2:  # Movimiento horizontal
            if col1 < col2:  # Derecha
                self.paredes[fila1][col1][2] = False
                self.paredes[fila2][col2][3] = False
            else:  # Izquierda
                self.paredes[fila1][col1][3] = False
                self.paredes[fila2][col2][2] = False
        else:  # Movimiento vertical
            if fila1 < fila2:  # Abajo
                self.paredes[fila1][col1][1] = False
                self.paredes[fila2][col2][0] = False
            else:  # Arriba
                self.paredes[fila1][col1][0] = False
                self.paredes[fila2][col2][1] = False
    
    def ajustar_dificultad(self):
        """Ajusta la dificultad según el nivel"""
        # Para niveles más altos, agregamos más caminos alternativos
        if self.nivel <= 2:
            # Niveles fáciles: agregar algunos caminos extra
            num_caminos_extra = int(self.filas * self.columnas * 0.05)
        else:
            # Niveles difíciles: agregar más caminos alternativos
            num_caminos_extra = int(self.filas * self.columnas * 0.1)

        for _ in range(num_caminos_extra):
            fila = random.randint(1, self.filas - 2)
            col = random.randint(1, self.columnas - 2)
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
    
    def movimiento_es_valido(self, fila, col, direccion):
        """Verifica si se puede mover en una dirección"""
        if direccion == 0:  # Arriba
            return not self.paredes[fila][col][0] and fila > 0
        elif direccion == 1:  # Abajo
            return not self.paredes[fila][col][1] and fila < self.filas - 1
        elif direccion == 2:  # Derecha
            return not self.paredes[fila][col][2] and col < self.columnas - 1
        elif direccion == 3:  # Izquierda
            return not self.paredes[fila][col][3] and col > 0
        return False

class AgenteLaberintoQLearning:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.posicion_inicial = (0, 0)
        self.posicion_meta = (laberinto.filas-1, laberinto.columnas-1)
        self.tabla_valores_q = np.zeros((laberinto.filas, laberinto.columnas, 4))
        self.tasa_aprendizaje = 0.1
        self.factor_descuento = 0.9
        self.probabilidad_exploracion = 0.1
    
    def entrenar(self, episodios=100):
        for _ in range(episodios):
            posicion_actual = self.posicion_inicial
            
            while posicion_actual != self.posicion_meta:
                if random.random() < self.probabilidad_exploracion:
                    accion = random.randint(0, 3)
                else:
                    accion = np.argmax(self.tabla_valores_q[posicion_actual[0]][posicion_actual[1]])
                
                nueva_posicion = self.mover(posicion_actual, accion)
                recompensa = 100 if nueva_posicion == self.posicion_meta else -1
                
                mejor_valor_futuro = np.max(self.tabla_valores_q[nueva_posicion[0]][nueva_posicion[1]])
                valor_actual = self.tabla_valores_q[posicion_actual[0]][posicion_actual[1]][accion]
                
                self.tabla_valores_q[posicion_actual[0]][posicion_actual[1]][accion] += (
                    self.tasa_aprendizaje * 
                    (recompensa + self.factor_descuento * mejor_valor_futuro - valor_actual)
                )
                
                posicion_actual = nueva_posicion
    
    def mover(self, posicion, direccion):
        fila, col = posicion
        
        if direccion == 0:   # ARRIBA
            nueva_pos = (fila-1, col)
        elif direccion == 1: # ABAJO
            nueva_pos = (fila+1, col)
        elif direccion == 2: # DERECHA
            nueva_pos = (fila, col+1)
        else:                # IZQUIERDA
            nueva_pos = (fila, col-1)
        
        return nueva_pos if self.laberinto.movimiento_es_valido(fila, col, direccion) else posicion
    
    def encontrar_ruta(self):
        ruta = [self.posicion_inicial]
        pos_actual = self.posicion_inicial
        limite = 100
        
        while pos_actual != self.posicion_meta and len(ruta) < limite:
            direccion = np.argmax(self.tabla_valores_q[pos_actual[0]][pos_actual[1]])
            pos_actual = self.mover(pos_actual, direccion)
            ruta.append(pos_actual)
        
        return ruta

class InterfazLaberinto:
    def __init__(self, master):
        self.master = master
        self.modo_jugador = False
        self.pos_jugador = (0, 0)
        self.configurar_interfaz()
        self.iniciar_nuevo_juego()
    
    def configurar_interfaz(self):
        """Configura la interfaz de usuario"""
        self.master.title("Laberinto con Q-Learning - Nivel 1")
        
        # Frame principal
        self.frame_principal = tk.Frame(self.master)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)
        
        # Canvas para el laberinto
        self.canvas = tk.Canvas(
            self.frame_principal,
            bg="white",
            highlightthickness=0
        )
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Frame de controles
        self.frame_controles = tk.Frame(self.frame_principal, width=200)
        self.frame_controles.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
        
        # Controles de nivel
        tk.Label(self.frame_controles, text="Nivel de Dificultad:").pack(pady=(10, 0))
        self.nivel_var = tk.IntVar(value=1)
        tk.Scale(
            self.frame_controles,
            from_=1,
            to=5,
            orient=tk.HORIZONTAL,
            variable=self.nivel_var,
            command=self.cambiar_nivel
        ).pack(pady=5)
        
        # Botones de control
        tk.Button(
            self.frame_controles,
            text="Nuevo Juego",
            command=self.iniciar_nuevo_juego
        ).pack(pady=5, fill=tk.X)
        
        tk.Button(
            self.frame_controles,
            text="Entrenar Agente",
            command=self.entrenar_agente
        ).pack(pady=5, fill=tk.X)
        
        tk.Button(
            self.frame_controles,
            text="Mostrar Ruta Óptima",
            command=self.mostrar_ruta
        ).pack(pady=5, fill=tk.X)
        
        # Modo jugador
        self.modo_var = tk.BooleanVar(value=False)
        tk.Checkbutton(
            self.frame_controles,
            text="Modo Jugador",
            variable=self.modo_var,
            command=self.cambiar_modo
        ).pack(pady=10)
        
        # Teclado para modo jugador
        self.master.bind("<KeyPress>", self.manejar_teclado)
    
    def cambiar_nivel(self, nivel):
        """Cambia el nivel de dificultad"""
        self.iniciar_nuevo_juego()
    
    def cambiar_modo(self):
        """Alterna entre modo jugador y modo visualización"""
        self.modo_jugador = self.modo_var.get()
        if self.modo_jugador:
            self.pos_jugador = (0, 0)
            self.dibujar_laberinto()
            messagebox.showinfo("Modo Jugador", "Usa las flechas del teclado para moverte.\nLlega a la casilla roja!")
        else:
            self.dibujar_laberinto()
    
    def manejar_teclado(self, event):
        """Maneja las teclas en modo jugador"""
        if not self.modo_jugador:
            return
            
        direccion = None
        if event.keysym == "Up":
            direccion = 0
        elif event.keysym == "Down":
            direccion = 1
        elif event.keysym == "Right":
            direccion = 2
        elif event.keysym == "Left":
            direccion = 3
        
        if direccion is not None:
            nueva_pos = self.agente.mover(self.pos_jugador, direccion)
            if nueva_pos != self.pos_jugador:
                self.pos_jugador = nueva_pos
                self.dibujar_laberinto()
                
                if self.pos_jugador == self.laberinto.posicion_meta:
                    messagebox.showinfo("¡Ganaste!", "¡Felicidades! Has llegado a la meta.")
                    self.modo_var.set(False)
                    self.cambiar_modo()
    
    def iniciar_nuevo_juego(self):
        """Inicia un nuevo juego con el nivel seleccionado"""
        nivel = self.nivel_var.get()
        self.master.title(f"Laberinto con Q-Learning - Nivel {nivel}")
        
        # Tamaño del laberinto basado en nivel
        tamaño = 5 + nivel * 2
        self.laberinto = LaberintoSimple(tamaño, tamaño, nivel)
        self.agente = AgenteLaberintoQLearning(self.laberinto)
        self.pos_jugador = (0, 0)
        
        self.dibujar_laberinto()
    
    def entrenar_agente(self):
        """Entrena al agente"""
        self.agente.entrenar(episodios=50)
        messagebox.showinfo("Entrenamiento", "Agente entrenado con éxito!")
    
    def mostrar_ruta(self):
        """Muestra la mejor ruta encontrada"""
        if self.modo_jugador:
            messagebox.showwarning("Modo Jugador", "Desactiva el modo jugador para ver la ruta óptima")
            return
            
        ruta = self.agente.encontrar_ruta()
        self.dibujar_laberinto(ruta)
        
        if ruta[-1] == self.laberinto.posicion_meta:
            messagebox.showinfo("Ruta Óptima", f"Ruta encontrada con {len(ruta)} pasos!")
        else:
            messagebox.showwarning("Ruta", "No se encontró una ruta completa")
    
    def dibujar_laberinto(self, ruta=None):
        """Dibuja el laberinto en el canvas"""
        self.canvas.delete("all")
        
        # Ajustar tamaño del canvas
        canvas_width = self.laberinto.columnas * TAM_CELDA + 2 * MARGEN
        canvas_height = self.laberinto.filas * TAM_CELDA + 2 * MARGEN
        self.canvas.config(width=canvas_width, height=canvas_height)
        
        # Dibujar celdas
        for fila in range(self.laberinto.filas):
            for col in range(self.laberinto.columnas):
                x1 = MARGEN + col * TAM_CELDA
                y1 = MARGEN + fila * TAM_CELDA
                x2 = x1 + TAM_CELDA
                y2 = y1 + TAM_CELDA
                
                # Dibujar paredes
                if self.laberinto.paredes[fila][col][0]:  # Arriba
                    self.canvas.create_line(x1, y1, x2, y1, width=2, fill=COLORES["pared"])
                if self.laberinto.paredes[fila][col][1]:  # Abajo
                    self.canvas.create_line(x1, y2, x2, y2, width=2, fill=COLORES["pared"])
                if self.laberinto.paredes[fila][col][2]:  # Derecha
                    self.canvas.create_line(x2, y1, x2, y2, width=2, fill=COLORES["pared"])
                if self.laberinto.paredes[fila][col][3]:  # Izquierda
                    self.canvas.create_line(x1, y1, x1, y2, width=2, fill=COLORES["pared"])
        
        # Dibujar inicio y meta
        self.dibujar_celda(0, 0, COLORES["inicio"])
        self.dibujar_celda(self.laberinto.filas-1, self.laberinto.columnas-1, COLORES["meta"])
        
        # Dibujar ruta si existe
        if ruta:
            self.dibujar_ruta(ruta)
        
        # Dibujar jugador en modo jugador
        if self.modo_jugador:
            self.dibujar_celda(self.pos_jugador[0], self.pos_jugador[1], COLORES["jugador"])
    
    def dibujar_celda(self, fila, col, color):
        """Dibuja un círculo en una celda"""
        x = MARGEN + col * TAM_CELDA + TAM_CELDA//2
        y = MARGEN + fila * TAM_CELDA + TAM_CELDA//2
        self.canvas.create_oval(x-10, y-10, x+10, y+10, fill=color, outline="")
    
    def dibujar_ruta(self, ruta):
        """Dibuja la ruta encontrada"""
        for i in range(len(ruta)-1):
            fila1, col1 = ruta[i]
            fila2, col2 = ruta[i+1]
            
            x1 = MARGEN + col1 * TAM_CELDA + TAM_CELDA//2
            y1 = MARGEN + fila1 * TAM_CELDA + TAM_CELDA//2
            x2 = MARGEN + col2 * TAM_CELDA + TAM_CELDA//2
            y2 = MARGEN + fila2 * TAM_CELDA + TAM_CELDA//2
            
            self.canvas.create_line(x1, y1, x2, y2, fill=COLORES["ruta"], width=2)

def main():
    root = tk.Tk()
    app = InterfazLaberinto(root)
    root.mainloop()

if __name__ == "__main__":
    main()