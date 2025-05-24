import tkinter as tk
from tkinter import messagebox, ttk
from collections import deque
from niveles import NIVELES
from laberinto import Laberinto

class VentanaLaberinto:
    """Interfaz gráfica del juego de laberintos con selección de niveles"""
    
    COLORES = {
        'fondo': '#f0f0f0',
        'pared': '#2c3e50',
        'camino': '#ecf0f1',
        'entrada': '#2ecc71',
        'salida': '#e74c3c',
        'jugador': '#3498db',
        'solucion': '#9b59b6'
    }
    
    def __init__(self, root):
        self.root = root
        self.root.title("Laberinto por Niveles")
        self.configurar_interfaz()
        self.mostrar_selector_niveles()
    
    def mostrar_selector_niveles(self):
        """Muestra la pantalla de selección de niveles"""
        self.selector = tk.Toplevel(self.root)
        self.selector.title("Seleccione Nivel")
        self.selector.geometry("500x400")
        
        # Frame principal
        frame = ttk.Frame(self.selector, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(frame, text="Seleccione un nivel", font=("Arial", 14)).pack(pady=10)
        
        # Tabla de niveles
        self.tree = ttk.Treeview(frame, columns=('dificultad', 'tamaño'), show='headings', height=5)
        self.tree.heading('#0', text='Nivel')
        self.tree.heading('dificultad', text='Dificultad')
        self.tree.heading('tamaño', text='Tamaño')
        
        for nivel in range(1, 6):
            config = NIVELES[nivel]
            self.tree.insert('', 'end', text=f"Nivel {nivel}", 
                           values=(config['dificultad'], f"{config['filas']}x{config['columnas']}"))
        
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Botón de inicio
        ttk.Button(frame, text="Comenzar", command=self.iniciar_juego_seleccionado).pack(pady=10)
        
        # Centrar ventana
        self.selector.transient(self.root)
        self.selector.grab_set()
        self.root.wait_window(self.selector)
    
    def iniciar_juego_seleccionado(self):
        """Inicia el juego con el nivel seleccionado"""
        item = self.tree.selection()
        if item:
            # Obtener el texto del ítem seleccionado
            item_text = self.tree.item(item, 'text')
            # Extraer el número del nivel (ej: "Nivel 1" -> 1)
            nivel = int(item_text.split()[-1])
            self.selector.destroy()
            self.cargar_nivel(nivel)
        else:
            messagebox.showwarning("Selección requerida", "Por favor seleccione un nivel")
    
    def configurar_interfaz(self):
        """Configura los elementos visuales principales"""
        self.root.geometry("900x700")
        self.root.configure(bg=self.COLORES['fondo'])
        
        # Frame principal
        self.frame = tk.Frame(self.root, bg=self.COLORES['fondo'])
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Panel de información
        self.frame_info = tk.Frame(self.frame, bg=self.COLORES['fondo'])
        self.frame_info.pack(fill=tk.X, pady=5)
        
        self.label_nivel = tk.Label(
            self.frame_info,
            text="Nivel 1",
            font=("Arial", 12, "bold"),
            bg=self.COLORES['fondo']
        )
        self.label_nivel.pack(side=tk.LEFT)
        
        # Canvas para el laberinto
        self.canvas = tk.Canvas(self.frame, bg='white', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Controles
        self.frame_controles = tk.Frame(self.frame, bg=self.COLORES['fondo'])
        self.frame_controles.pack(fill=tk.X, pady=10)
        
        # Botón para cambiar de nivel
        tk.Button(
            self.frame_controles,
            text="Cambiar Nivel",
            command=self.mostrar_selector_niveles,
            bg='#95a5a6',
            fg='white',
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT, padx=5)
        
        # Botón para resolver con BFS
        tk.Button(
            self.frame_controles,
            text="Mostrar Mejor Camino",
            command=self.mostrar_mejor_camino,
            bg=self.COLORES['solucion'],
            fg='white',
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT, padx=5)
        
        # Eventos de teclado
        self.root.bind("<Up>", lambda e: self.mover_jugador(-1, 0))
        self.root.bind("<Down>", lambda e: self.mover_jugador(1, 0))
        self.root.bind("<Left>", lambda e: self.mover_jugador(0, -1))
        self.root.bind("<Right>", lambda e: self.mover_jugador(0, 1))
    
    def cargar_nivel(self, nivel):
        """Carga un nuevo nivel del laberinto"""
        self.nivel_actual = nivel
        config = NIVELES[nivel]
        self.laberinto = Laberinto(config["filas"], config["columnas"])
        self.jugador_pos = self.laberinto.entrada
        self.tamaño_celda = config["tamaño_celda"]
        self.label_nivel.config(text=f"Nivel {nivel} - {config['dificultad']}")
        self.dibujar_laberinto()
    
    def dibujar_laberinto(self):
        """Dibuja todo el laberinto en el canvas"""
        self.canvas.delete("all")
        self.canvas.config(
            width=self.laberinto.columnas * self.tamaño_celda,
            height=self.laberinto.filas * self.tamaño_celda
        )
        
        # Dibujar celdas
        for i in range(self.laberinto.filas):
            for j in range(self.laberinto.columnas):
                self.dibujar_celda(i, j)
        
        # Dibujar jugador
        self.dibujar_jugador()
    
    def dibujar_celda(self, i, j):
        """Dibuja una celda individual"""
        x1 = j * self.tamaño_celda
        y1 = i * self.tamaño_celda
        x2 = x1 + self.tamaño_celda
        y2 = y1 + self.tamaño_celda
        
        if (i,j) == self.laberinto.entrada:
            color = self.COLORES['entrada']
        elif (i,j) == self.laberinto.salida:
            color = self.COLORES['salida']
        elif self.laberinto.grid[i][j] == 1:
            color = self.COLORES['pared']
        else:
            color = self.COLORES['camino']
        
        self.canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=color,
            outline=self.COLORES['pared'],
            width=1
        )
    
    def dibujar_jugador(self):
        """Dibuja al jugador en su posición actual"""
        i, j = self.jugador_pos
        margen = self.tamaño_celda * 0.25
        x1 = j * self.tamaño_celda + margen
        y1 = i * self.tamaño_celda + margen
        x2 = (j + 1) * self.tamaño_celda - margen
        y2 = (i + 1) * self.tamaño_celda - margen
        
        self.canvas.create_oval(
            x1, y1, x2, y2,
            fill=self.COLORES['jugador'],
            outline='#2980b9',
            width=2,
            tags="jugador"
        )
    
    def mover_jugador(self, di, dj):
        """Mueve al jugador en la dirección especificada"""
        i, j = self.jugador_pos
        nueva_pos = (i + di, j + dj)
        
        if nueva_pos in self.laberinto.obtener_vecinos(self.jugador_pos):
            self.jugador_pos = nueva_pos
            self.canvas.delete("jugador")
            self.dibujar_jugador()
            
            if nueva_pos == self.laberinto.salida:
                self.nivel_completado()
    
    def nivel_completado(self):
        """Maneja la finalización de un nivel"""
        messagebox.showinfo(
            "¡Nivel Completado!", 
            f"¡Has completado el nivel {self.nivel_actual}!"
        )
        
        if self.nivel_actual < len(NIVELES):
            self.cargar_nivel(self.nivel_actual + 1)
        else:
            messagebox.showinfo(
                "¡Felicidades!", 
                "¡Has completado todos los niveles!"
            )
            self.mostrar_selector_niveles()
    
    def mostrar_mejor_camino(self):
        """Muestra el mejor camino encontrado por BFS"""
        if hasattr(self, 'laberinto') and hasattr(self.laberinto, 'solucion'):
            for paso in self.laberinto.solucion[1:-1]:  # Excluir entrada y salida
                i, j = paso
                self.dibujar_celda_especial((i,j), self.COLORES['solucion'])
    
    def dibujar_celda_especial(self, posicion, color):
        """Dibuja una celda con un color especial para la solución"""
        i, j = posicion
        margen = self.tamaño_celda * 0.3
        x1 = j * self.tamaño_celda + margen
        y1 = i * self.tamaño_celda + margen
        x2 = (j + 1) * self.tamaño_celda - margen
        y2 = (i + 1) * self.tamaño_celda - margen
        
        self.canvas.create_oval(
            x1, y1, x2, y2,
            fill=color,
            outline='#34495e',
            width=2,
            tags="solucion"
        )
    