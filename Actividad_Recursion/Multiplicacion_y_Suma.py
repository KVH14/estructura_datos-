

def multiplicar (a,b):
    if b == 1:
      return a 
    return a + multiplicar(a, b - 1)

print("El resultado es:", multiplicar(3, 2))

def divide(a, b, precision=10):
    if a < b:
        if precision == 0:
            return 0
        return 0.1 * divide(a * 10, b, precision - 1)
    return 1 + divide(a - b, b, precision)