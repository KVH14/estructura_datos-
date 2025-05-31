class Nodo:
    """Clase que representa un nodo en una pila"""
    def __init__(self, valor, posicion, siguiente=None):
        self.valor = valor       # Símbolo de apertura
        self.posicion = posicion # Posición en la cadena
        self.siguiente = siguiente # Referencia al siguiente nodo

class Pila:
    """Implementación de pila usando nodos enlazados"""
    def __init__(self):
        self.tope = None  # El nodo en la cima de la pila
    
    def esta_vacia(self):
        """Verifica si la pila está vacía"""
        return self.tope is None
    
    def apilar(self, valor, posicion):
        """Agrega un elemento a la pila"""
        nuevo_nodo = Nodo(valor, posicion, self.tope)
        self.tope = nuevo_nodo
    
    def desapilar(self):
        """Elimina y devuelve el elemento en la cima de la pila"""
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        valor = self.tope.valor
        posicion = self.tope.posicion
        self.tope = self.tope.siguiente
        return valor, posicion
    
    def ver_tope(self):
        """Devuelve el elemento en la cima sin eliminarlo"""
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.tope.valor, self.tope.posicion

def verificar_balanceo(expresion: str) -> str:
    """Verifica si una expresión tiene los símbolos balanceados usando una pila con nodos.
    
    Args:
        expresion (str): Expresión a evaluar.

    Returns:
        str: Mensaje indicando si la expresión está balanceada o detallando el error.
    """
    # Diccionario de pares de símbolos
    pares = {'(': ')', '[': ']', '{': '}'}
    
    # Crear una pila vacía
    pila = Pila()
    
    # Recorrer cada carácter de la expresión con su índice
    for i, caracter in enumerate(expresion):
        if caracter in pares:
            # Si es un símbolo de apertura, lo apilamos con su posición
            pila.apilar(caracter, i)
        elif caracter in pares.values():
            # Si es un símbolo de cierre, verificamos si hay una apertura correspondiente
            if pila.esta_vacia():
                return f"Error en posición {i}: '{caracter}' no tiene apertura."
            
            simbolo_apertura, posicion = pila.desapilar()
            if pares[simbolo_apertura] != caracter:
                return f"Error en posición {i}: '{caracter}' no coincide con '{simbolo_apertura}' (abierto en posición {posicion})."
    
    # Verificar si quedó algún símbolo de apertura sin su cierre
    if not pila.esta_vacia():
        simbolo_abierto, posicion = pila.ver_tope()
        return f"Error en posición {posicion}: '{simbolo_abierto}' no tiene cierre."
    
    return "La expresión está correctamente balanceada."

def main():
    """Función principal para interactuar con el usuario"""
    print("Verificador de Balanceo de Símbolos")
    print("Símbolos válidos: (), [], {}")
    
    while True:
        expresion = input("\nIngrese una expresión (o 'salir' para terminar): ").strip()
        
        if expresion.lower() == 'salir':
            break
        
        if not expresion:
            print("Por favor ingrese una expresión válida.")
            continue
            
        resultado = verificar_balanceo(expresion)
        print(resultado)

if __name__ == "__main__":
    main()