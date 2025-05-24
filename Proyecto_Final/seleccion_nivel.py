import tkinter as tk
from tkinter import ttk
from laberinto import Laberinto
from niveles import NIVELES

class SeleccionNivel:
    def __init__(self, root, callback_seleccion):
        self.root = root
        self.callback = callback_seleccion
        self.configurar_interfaz()
        
    def configurar_interfaz(self):
        self.root.title("Selección de Nivel")
        self.root.geometry("600x500")
        
        # Frame principal
        frame = ttk.Frame(self.root, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(frame, text="Seleccione un nivel", font=("Arial", 16)).pack(pady=10)
        
        # Tabla de niveles
        self.tree = ttk.Treeview(frame, columns=('dificultad', 'tamaño'), show='headings')
        self.tree.heading('#0', text='Nivel')
        self.tree.heading('dificultad', text='Dificultad')
        self.tree.heading('tamaño', text='Tamaño')
        
        for nivel in range(1, 6):
            config = NIVELES[nivel]
            self.tree.insert('', 'end', text=f"Nivel {nivel}", 
                           values=(config['dificultad'], f"{config['filas']}x{config['columnas']}"))
        
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Visualización del camino único
        self.canvas = tk.Canvas(frame, bg='white', height=150)
        self.canvas.pack(fill=tk.X, pady=10)
        
        # Botón de inicio
        ttk.Button(frame, text="Comenzar", command=self.iniciar_juego).pack(pady=10)
        
        # Evento de selección
        self.tree.bind('<<TreeviewSelect>>', self.mostrar_camino_nivel)
        
    def mostrar_camino_nivel(self, event):
        """Muestra el camino único del nivel seleccionado"""
        item = self.tree.selection()[0]
        nivel = int(item.split(' ')[-1])
        config = NIVELES[nivel]
        
        lab = Laberinto(config["filas"], config["columnas"])
        self.canvas.delete("all")
        tamaño_celda = min(300//config["filas"], 300//config["columnas"])
        
        # Dibujar laberinto miniaturizado
        for i in range(config["filas"]):
            for j in range(config["columnas"]):
                color = '#2c3e50' if lab.grid[i][j] == 1 else '#ecf0f1'
                self.canvas.create_rectangle(
                    j*tamaño_celda, i*tamaño_celda,
                    (j+1)*tamaño_celda, (i+1)*tamaño_celda,
                    fill=color, outline=''
                )
        
        # Dibujar camino único
        for paso in lab.camino_unico:
            i, j = paso
            self.canvas.create_oval(
                j*tamaño_celda + 2, i*tamaño_celda + 2,
                (j+1)*tamaño_celda - 2, (i+1)*tamaño_celda - 2,
                fill='#3498db', outline=''
            )
    
    def iniciar_juego(self):
        """Inicia el juego con el nivel seleccionado"""
        item = self.tree.selection()
        if item:
            nivel = int(item[0].split(' ')[-1])
            self.root.destroy()
            self.callback(nivel)
        else:
            tk.messagebox.showwarning("Selección requerida", "Por favor seleccione un nivel")