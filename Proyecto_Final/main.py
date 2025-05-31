import tkinter as tk
from interfaz import MenuPrincipal

def main():
    ventana = tk.Tk()
    ventana.title("Laberinto con Inteligencia Artificial")
    ventana.geometry("1200x800")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla - 1200) // 2
    y = (alto_pantalla - 800) // 2
    ventana.geometry(f"1200x800+{x}+{y}")
    MenuPrincipal(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()