import tkinter as tk
from tkinter import messagebox
from laberinto_simple import LaberintoSimple
from agente import AgenteInteligente
from constantes import TAM_CELDA, MARGEN


class InterfazLaberinto:
    """Interfaz gráfica para el juego del laberinto"""
    
    def __init__(self, master, filas, columnas, nivel):
        self.master = master
        self.filas = filas
        self.columnas = columnas
        self.nivel = nivel
        self.laberinto = LaberintoSimple(filas, columnas, nivel)
        self.modo_manual = False
        self.posicion_jugador = (0, 0)
        self.ruta_jugador = [(0, 0)]
        self.cola_resultados = None
        self.configurar_ventana()
        self.dibujar_laberinto()
        self.master.after(100, self.revisar_resultados)
    
    def configurar_ventana(self):
        """Configura los elementos de la ventana"""
        # Canvas para dibujar el laberinto
        self.canvas = tk.Canvas(
            self.master,
            width=self.columnas * TAM_CELDA + 2 * MARGEN,
            height=self.filas * TAM_CELDA + 2 * MARGEN,
            bg="white"
        )
        self.canvas.pack(side="left", padx=10, pady=10)
        
        # Panel de controles
        panel = tk.Frame(self.master)
        panel.pack(side="right", padx=10, pady=10)
        
        tk.Label(
            panel,
            text=f"Nivel {self.nivel}",
            font=("Arial", 16, "bold")
        ).pack(pady=10)
        
        self.btn_resolver = tk.Button(
            panel,
            text="Resolver con IA",
            command=self.resolver_con_ia,
            width=20,
            bg="lightblue",
            font=("Arial", 10)
        )
        self.btn_resolver.pack(pady=5)
        
        tk.Button(
            panel,
            text="Jugar Manualmente",
            command=self.activar_modo_manual,
            width=20,
            bg="lightgreen",
            font=("Arial", 10)
        ).pack(pady=5)
        
        tk.Button(
            panel,
            text="Nuevo Laberinto",
            command=self.nuevo_laberinto,
            width=20,
            bg="lightyellow",
            font=("Arial", 10)
        ).pack(pady=5)
        
        tk.Button(
            panel,
            text="Volver al Menú",
            command=self.volver_menu,
            width=20,
            bg="lightcoral",
            font=("Arial", 10)
        ).pack(pady=20)
        
        # Instrucciones
        tk.Label(
            panel,
            text="Instrucciones:",
            font=("Arial", 10, "bold")
        ).pack(pady=(20, 5))
        
        instrucciones = [
            "• Verde: Inicio",
            "• Rojo: Meta",
            "• Usar flechas del teclado",
            "• para jugar manualmente"
        ]
        
        for inst in instrucciones:
            tk.Label(
                panel,
                text=inst,
                font=("Arial", 9),
                anchor="w"
            ).pack(anchor="w")
        
        # Configurar eventos del teclado
        self.master.bind("<Key>", self.manejar_teclas)
        self.master.focus_set()
    
    def dibujar_laberinto(self, ruta_solucion=None):
        """Dibuja el laberinto completo"""
        self.canvas.delete("all")
        
        # Dibujar las paredes
        for fila in range(self.filas):
            for col in range(self.columnas):
                x1 = MARGEN + col * TAM_CELDA
                y1 = MARGEN + fila * TAM_CELDA
                x2 = x1 + TAM_CELDA
                y2 = y1 + TAM_CELDA
                
                # Dibujar paredes si existen
                if self.laberinto.paredes[fila][col][0]:  # Pared arriba
                    self.canvas.create_line(x1, y1, x2, y1, width=2, fill="black")
                if self.laberinto.paredes[fila][col][1]:  # Pared abajo
                    self.canvas.create_line(x1, y2, x2, y2, width=2, fill="black")
                if self.laberinto.paredes[fila][col][2]:  # Pared derecha
                    self.canvas.create_line(x2, y1, x2, y2, width=2, fill="black")
                if self.laberinto.paredes[fila][col][3]:  # Pared izquierda
                    self.canvas.create_line(x1, y1, x1, y2, width=2, fill="black")
        
        # Dibujar inicio y meta
        self.dibujar_celda(0, 0, "green")  # Inicio
        self.dibujar_celda(self.filas - 1, self.columnas - 1, "red")  # Meta
        
        # Dibujar ruta de solución si existe
        if ruta_solucion:
            self.dibujar_ruta(ruta_solucion, "blue")
        
        # Dibujar ruta del jugador si está activa
        if self.modo_manual and len(self.ruta_jugador) > 1:
            self.dibujar_ruta(self.ruta_jugador, "orange")
    
    def dibujar_celda(self, fila, col, color):
        """Dibuja un círculo coloreado en una celda"""
        x1 = MARGEN + col * TAM_CELDA + 4
        y1 = MARGEN + fila * TAM_CELDA + 4
        x2 = x1 + TAM_CELDA - 8
        y2 = y1 + TAM_CELDA - 8
        self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)
    
    def dibujar_ruta(self, ruta, color):
        """Dibuja una línea siguiendo la ruta"""
        for i in range(len(ruta) - 1):
            fila1, col1 = ruta[i]
            fila2, col2 = ruta[i + 1]
            
            # Calcular coordenadas del centro de cada celda
            x1 = MARGEN + col1 * TAM_CELDA + TAM_CELDA // 2
            y1 = MARGEN + fila1 * TAM_CELDA + TAM_CELDA // 2
            x2 = MARGEN + col2 * TAM_CELDA + TAM_CELDA // 2
            y2 = MARGEN + fila2 * TAM_CELDA + TAM_CELDA // 2
            
            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=3)
    
    def resolver_con_ia(self):
        """Inicia la resolución automática con IA"""
        self.btn_resolver.config(state=tk.DISABLED, text="Entrenando...")

    
    def _entrenar_agente(self):
        """Entrena al agente en un hilo separado"""
        try:
            agente = AgenteInteligente(self.laberinto, self.nivel)
            agente.entrenar()
            ruta = agente.encontrar_mejor_ruta()
            self.cola_resultados.put(("solucion", ruta))
        except Exception as e:
            self.cola_resultados.put(("error", str(e)))
    
    def revisar_resultados(self):
        """Revisa los resultados del entrenamiento"""
        try:
            while not self.cola_resultados.empty():
                tipo, datos = self.cola_resultados.get_nowait()
                
                if tipo == "solucion":
                    self.dibujar_laberinto(datos)
                    exito = datos[-1] == (self.filas - 1, self.columnas - 1)
                    mensaje = f"La IA {'encontró' if exito else 'no encontró'} la solución\n"
                    mensaje += f"Pasos utilizados: {len(datos)}"
                    messagebox.showinfo("Resultado", mensaje)
                    
                elif tipo == "error":
                    messagebox.showerror("Error", f"Error durante el entrenamiento: {datos}")
                
                self.btn_resolver.config(state=tk.NORMAL, text="Resolver con IA")
        except:
            pass
        
        self.master.after(100, self.revisar_resultados)
    
    def activar_modo_manual(self):
        """Activa el modo de juego manual"""
        self.modo_manual = True
        self.posicion_jugador = (0, 0)
        self.ruta_jugador = [(0, 0)]
        self.dibujar_laberinto()
        messagebox.showinfo("Modo Manual", "¡Usa las flechas del teclado para moverte!")
    
    def manejar_teclas(self, evento):
        """Maneja las teclas presionadas por el jugador"""
        if not self.modo_manual:
            return
        
        fila, col = self.posicion_jugador
        movimiento = None
        
        # Mapear teclas a direcciones
        if evento.keysym == 'Up':
            movimiento = 0  # Arriba
        elif evento.keysym == 'Down':
            movimiento = 1  # Abajo
        elif evento.keysym == 'Right':
            movimiento = 2  # Derecha
        elif evento.keysym == 'Left':
            movimiento = 3  # Izquierda
        
        if movimiento is not None and self.laberinto.puede_moverse(fila, col, movimiento):
            # Calcular nueva posición
            if movimiento == 0:  # Arriba
                nueva_pos = (fila - 1, col)
            elif movimiento == 1:  # Abajo
                nueva_pos = (fila + 1, col)
            elif movimiento == 2:  # Derecha
                nueva_pos = (fila, col + 1)
            elif movimiento == 3:  # Izquierda
                nueva_pos = (fila, col - 1)
            
            self.posicion_jugador = nueva_pos
            self.ruta_jugador.append(nueva_pos)
            self.dibujar_laberinto()
            
            # Verificar si llegó a la meta
            if nueva_pos == (self.filas - 1, self.columnas - 1):
                self.modo_manual = False
                mensaje = f"¡Felicidades!\n¡Completaste el nivel {self.nivel}!\n"
                mensaje += f"Pasos utilizados: {len(self.ruta_jugador)}"
                messagebox.showinfo("¡Victoria!", mensaje)
    
    def nuevo_laberinto(self):
        """Genera un nuevo laberinto del mismo nivel"""
        self.laberinto = LaberintoSimple(self.filas, self.columnas, self.nivel)
        self.modo_manual = False
        self.posicion_jugador = (0, 0)
        self.ruta_jugador = [(0, 0)]
        self.dibujar_laberinto()
    
    def volver_menu(self):
        """Regresa al menú principal"""
        for widget in self.master.winfo_children():
            widget.destroy()
        MenuPrincipal(self.master)


class MenuPrincipal:
  
   def __init__(self, master):
        self.master = master
        self.master.title("Laberinto con Inteligencia Artificial")
        self.nivel_elegido = tk.IntVar(value=1)
        self.crear_menu()
    
   def crear_menu(self):
        """Crea la interfaz del menú principal"""
        frame = tk.Frame(self.master, padx=40, pady=40)
        frame.pack()
        
        # Título
        tk.Label(
            frame,
            text="🧩 Laberinto con IA 🧩",
            font=("Arial", 20, "bold"),
            fg="darkblue"
        ).pack(pady=20)
        
        tk.Label(
            frame,
            text="Elige el nivel de dificultad:",
            font=("Arial", 14)
        ).pack(pady=15)
        
        # Opciones de nivel
        niveles = {
            1: "⭐ Principiante (12x12)",
            2: "⭐⭐ Fácil (15x15)",
            3: "⭐⭐⭐ Intermedio (18x18)",
            4: "⭐⭐⭐⭐ Difícil (22x22)",
            5: "⭐⭐⭐⭐⭐ Experto (25x25)"
        }
        
        for nivel, descripcion in niveles.items():
            tk.Radiobutton(
                frame,
                text=descripcion,
                variable=self.nivel_elegido,
                value=nivel,
                font=("Arial", 12)
            ).pack(anchor="w", pady=3)
        
        # Botón para empezar
        tk.Button(
            frame,
            text="🚀 ¡Empezar Aventura!",
            command=self.empezar_juego,
            font=("Arial", 14, "bold"),
            bg="lightgreen",
            width=25,
            height=2
        ).pack(pady=30)
        
   def empezar_juego(self):
        """Inicia el juego con el nivel seleccionado"""
        nivel = self.nivel_elegido.get()
        tamaños = {1: (12, 12), 2: (15, 15), 3: (18, 18), 4: (22, 22), 5: (25, 25)}
        filas, columnas = tamaños.get(nivel, (12, 12))
        
        # Limpiar ventana
        for widget in self.master.winfo_children():
            widget.destroy()
        
        # Crear juego
        InterfazLaberinto(self.master, filas, columnas, nivel)