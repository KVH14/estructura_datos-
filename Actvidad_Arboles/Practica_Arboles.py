class Nodo:
    """Clase Nodo con valor, hijo izquierdo y derecho"""
    def __init__(self, valor):
        self.valor = valor # Valor del nodo 
        self.izq = None
        self.der = None

    def __str__(self):
        return str(self.valor)

class ArbolBinario:

    def __init__(self): 
        self.raiz = None #Nodo raíz del árbol

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)  # Si el árbol está vacío, creamos la raíz con el valor
        else:
            self._insertar(valor, self.raiz) # Si no está vacío, llamamos al método recursivo

    def _insertar(self, valor, nodo): # Método recursivo para insertar un nuevo nodo
        if valor < nodo.valor: # Si el valor es menor que el nodo actual, lo insertamos en la izquierda
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar(valor, nodo.izq) #El valor a insertar es menor que el nodo actual
        else:
            if nodo.der is None: # hace lo mismo que el izquierdo solo que en el derecho 
                nodo.der = Nodo(valor) 
            else:
                self._insertar(valor, nodo.der)

    
    def preorden(self):
        if self.raiz is not None: 
            # Si el árbol no está vacío, comienza el recorrido en preorden
            self._preorden(self.raiz)

    def _preorden(self, nodo):
        """Método recursivo para imprimir el árbol en preorden"""
        # Imprime el valor del nodo actual
        print(nodo.valor, end=", ")
        # Si existe un Nodo izquierdo, se recurre al subárbol izquierdo
        if nodo.izq is not None:
            self._preorden(nodo.izq)
        # Si existe un Nodo derecho, se recurre al subárbol derecho
        if nodo.der is not None:
            self._preorden(nodo.der)

    def imprimir(self):
        """Imprimir el árbol de forma estructurada"""
        if self.raiz is not None:
            # Si el árbol no está vacío, comienza el proceso de impresión estructurada
            self._imprimir(self.raiz, 0)

    def _imprimir(self, nodo, nivel):
        """Método recursivo para imprimir el árbol de forma estructurada"""
        if nodo is not None:
            # Primero imprime el subárbol derecho (más profundo)
            self._imprimir(nodo.der, nivel + 1) #nivel + 1 sirve para incrementar el nivel de profundidad
            # Imprime el valor del nodo actual con una indentación según el nivel
            print("   " * nivel + str(nodo.valor))  
            # Luego imprime el subárbol izquierdo
            self._imprimir(nodo.izq, nivel + 1)

    def buscar(self, valor):
        return self._buscar(valor, self.raiz)

    def _buscar(self, valor, nodo):
        """Método recursivo para buscar un valor en el árbol"""
        if nodo is None:
            # Si llegamos a un nodo vacío (None), significa que el valor no existe
            return False
        if valor == nodo.valor:
            # Si encontramos el valor en el nodo actual, retornamos True
            return True
        elif valor < nodo.valor:
            # Si el valor es menor que el nodo actual, se busca en el subárbol izquierdo
            return self._buscar(valor, nodo.izq)
        else:
            # Si el valor es mayor que el nodo actual, se busca en el subárbol derecho
            return self._buscar(valor, nodo.der)

   

# -------------------------------------
# Ejecución del ejercicio
valores = [20, 10, 30, 5, 15, 25, 35]

arbol = ArbolBinario()
for v in valores:
    # Insertar cada valor en el árbol
    arbol.insertar(v)

print("Árbol en preorden:")
# Imprimir el árbol en preorden
arbol.preorden()

print("Árbol estructurado:")
# Imprimir el árbol de forma estructurada
arbol.imprimir()

# Búsqueda con input
valor_buscar = int(input("Ingresa un valor para buscar en el árbol: "))
if arbol.buscar(valor_buscar):
    print(f"El valor {valor_buscar} sí existe en el árbol.")
else:
    print(f"El valor {valor_buscar} no existe en el árbol.")