import numpy as np
import random

class AgenteInteligente:

    
    def __init__(self, laberinto, nivel):
        self.laberinto = laberinto
        self.nivel = nivel
        self.inicio = (0, 0)
        self.meta = (laberinto.filas - 1, laberinto.columnas - 1)
        self.episodios = 1000 + (nivel * 300)  # Más episodios para mejor aprendizaje
        self.velocidad_aprendizaje = 0.1  # Aprendizaje más gradual
        self.factor_descuento = 0.95  # Mayor importancia del futuro
        self.exploracion = 1.0
        self.exploracion_minima = 0.05
        self.reduccion_exploracion = 0.998  # Reducción más lenta
        self.tabla_q = np.zeros((laberinto.filas, laberinto.columnas, 4))# Tabla de valores Q inicializada en cero
        self.visitas = np.zeros((laberinto.filas, laberinto.columnas))# Contadores para ayudar al aprendizaje
        self.episodios_exitosos = 0
    
    def calcular_recompensa(self, posicion_anterior, posicion_actual):

        if posicion_actual == self.meta:
            return 100.0  # Gran recompensa por llegar a la meta
        
        if posicion_actual == posicion_anterior:
            return -5.0  # Penalidad por movimiento inválido
        # Recompensa por acercarse a la meta
        distancia_anterior = abs(posicion_anterior[0] - self.meta[0]) + abs(posicion_anterior[1] - self.meta[1])
        distancia_actual = abs(posicion_actual[0] - self.meta[0]) + abs(posicion_actual[1] - self.meta[1])
        
        if distancia_actual < distancia_anterior:
            recompensa = 2.0  # Recompensa por acercarse
        elif distancia_actual > distancia_anterior:
            recompensa = -1.0  # Penalidad por alejarse
        else:
            recompensa = -0.1  # Pequeña penalidad por moverse sin progreso
        
        return recompensa
    
    def elegir_accion(self, fila, col):
      acciones_validas = []
      for accion in range(4):
        if self.laberinto.puede_moverse(fila, col, accion):
             acciones_validas.append(accion)
        if not acciones_validas:
          return 0  # No hay acciones válidas, devuelve 0 por defecto
        if random.random() < self.exploracion:
          return random.choice(acciones_validas)# Exploración: elegir una acción válida al azar
       

    def mover(self, fila, col, accion):

        if not self.laberinto.puede_moverse(fila, col, accion):
            return (fila, col)  # No se puede mover, quedarse en el mismo lugar
        
        if accion == 0:  # Arriba
            return (fila - 1, col)
        elif accion == 1:  # Abajo
            return (fila + 1, col)
        elif accion == 2:  # Derecha
            return (fila, col + 1)
        elif accion == 3:  # Izquierda
            return (fila, col - 1)
        
        return (fila, col)
    
    def entrenar(self):

        print(f"Iniciando entrenamiento de {self.episodios} episodios...")
        
        for episodio in range(self.episodios):
            posicion_actual = self.inicio
            self.visitas[posicion_actual[0]][posicion_actual[1]] += 1
            
            # Límite de pasos para evitar bucles infinitos
            pasos = 0
            max_pasos = self.laberinto.filas * self.laberinto.columnas * 3
            ruta_episodio = [posicion_actual]
            
            while posicion_actual != self.meta and pasos < max_pasos: #que no pase el limite de pasos
                fila, col = posicion_actual
                accion = self.elegir_accion(fila, col)# Elegir acción para saber donde ir
                nueva_posicion = self.mover(fila, col, accion) #nueva posición después de la acción
                self.visitas[nueva_posicion[0]][nueva_posicion[1]] += 1 
                
                # Calcular recompensa
                recompensa = self.calcular_recompensa(posicion_actual, nueva_posicion)
                
                
                fila_nueva, col_nueva = nueva_posicion #ultima posicion de la accion
                if nueva_posicion == self.meta:
                    # Si llegamos a la meta, no hay futuro
                    mejor_q_futuro = 0
                    self.episodios_exitosos += 1
                else:
                   
                    q_futuros = [] #Buscamos acciones futuras 
                    for a in range(4):
                        q_futuros.append(self.tabla_q[fila_nueva][col_nueva][a])
                   
                
                # Actualización Q-Learning con la formula mejorada
                valor_actual = self.tabla_q[fila][col][accion]
                objetivo = recompensa + self.factor_descuento * mejor_q_futuro
                self.tabla_q[fila][col][accion] += self.velocidad_aprendizaje * (objetivo - valor_actual)
                
                ruta_episodio.append(nueva_posicion) #Guarda la nueva posición en la ruta.
                posicion_actual = nueva_posicion #Actualiza la posición actual.
                pasos += 1 #Incrementa el contador de pasos.
    
        
        tasa_exito = (self.episodios_exitosos / self.episodios) * 100
        print(f"Entrenamiento completado. Tasa de éxito: {tasa_exito:.1f}%")
        


