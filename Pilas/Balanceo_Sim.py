class Nodo:
    def __init__(self, valor, posicion):
        self.valor = valor
        self.posicion = posicion
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None
    
    def esta_vacia(self):
        return self.tope is None
    
    def apilar(self, valor, posicion):
        nuevo_nodo = Nodo(valor, posicion)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
    
    def desapilar(self):
        if self.esta_vacia():
            return None, None
        valor = self.tope.valor
        posicion = self.tope.posicion
        self.tope = self.tope.siguiente
        return valor, posicion

    def ver_tope(self):
        if self.esta_vacia():
            return None, None
        return self.tope.valor, self.tope.posicion


def verificar_balanceo(expresion):
    pares = {'(': ')', '[': ']', '{': '}'}
    pila = Pila()

    for i, caracter in enumerate(expresion):
        if caracter in pares:
            pila.apilar(caracter, i)
        elif caracter in pares.values():
            if pila.esta_vacia():
                return f"Error en posición {i}: '{caracter}' no tiene apertura."
            simbolo_abierto, posicion = pila.desapilar()
            if pares[simbolo_abierto] != caracter:
                return f"Error en posición {i}: '{caracter}' no coincide con '{simbolo_abierto}' (abierto en posición {posicion})."
    
    if not pila.esta_vacia():
        simbolo_abierto, posicion = pila.ver_tope()
        return f"Error en posición {posicion}: '{simbolo_abierto}' no tiene cierre."
    
    return "La expresión está correctamente balanceada."

# Mini menú para ingresar y verificar expresiones
while True:
    expresion = input("\nIngrese una expresión para verificar (o 'salir' para terminar): ").strip()
    if expresion.lower() == 'salir':
        print("¡Hasta luego!")
        break
    if not expresion:
        print("Por favor ingrese una expresión válida.")
        continue
    
    resultado = verificar_balanceo(expresion)
    print(resultado)
