class Cancion:
    def __init__(self, titulo: str, artista: str, album: str, duracion: float):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion

    def reproducir(self):
        print(f"Reproduciendo: {self.titulo} - {self.artista} ({self.duracion} min)")


titulo = input("Ingrese el título de la canción: ")
artista = input("Ingrese el artista: ")
album = input("Ingrese el álbum: ")
duracion = float(input("Ingrese la duración en minutos: "))


cancion = Cancion(titulo, artista, album, duracion)
cancion.reproducir()