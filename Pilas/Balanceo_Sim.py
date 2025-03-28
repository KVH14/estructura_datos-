def Balanceo_Simbolos(expresion: str) -> str:
    """Verifica si una expresión tiene los símbolos balanceados.
    Args:
        expresion (str): Expresión a evaluar.

    Returns:
        str: Mensaje indicando si la expresión está balanceada o detallando el error.
    """
    # Diccionario de pares de símbolos de apertura y cierre
    pares: dict[str, str] = {'(': ')', '[': ']', '{': '}'}

    # Pila para almacenar los símbolos de apertura junto con su posición
    pila: list[tuple[str, int]] = []

    # Recorrer cada carácter de la expresión con su índice
    for i, caracter in enumerate(expresion):
        if caracter in pares:
            # Si es un símbolo de apertura, lo apilamos con su posición
            pila.append((caracter, i))
        elif caracter in pares.values():
            # Si es un símbolo de cierre, verificamos si hay una apertura correspondiente
            if not pila:
                return f"Error en la posición {i}: símbolo '{caracter}' no tiene apertura correspondiente."

            simbolo_apertura, posicion = pila.pop()
            if pares[simbolo_apertura] != caracter:
                return f"Error en la posición {i}: símbolo '{caracter}' no coincide con '{simbolo_apertura}'."

    # Verificar si quedó algún símbolo de apertura sin su cierre
    if pila:
        simbolo_abierto, posicion = pila[-1]
        return f"Error en la posición {posicion}: símbolo '{simbolo_abierto}' no tiene cierre correspondiente."

    return "La expresión está balanceada."


# Solicitar entrada del usuario
expresion: str = input("Ingrese la expresión a evaluar: ")

# Evaluar si la expresión está balanceada
resultado: str = Balanceo_Simbolos(expresion)

# Imprimir el resultado
print(resultado)
