
print("Multiplicacion")
def multiplicar (a,b):
    if b == 1:
      return a 
    return a + multiplicar(a, b - 1)

print("El resultado es:", multiplicar(3, 2))


print("Division")
def divide(a,b):
    if a < b:
        return 0
    return 1 + divide(a-b,b)
print("El resultado es:", divide(6, 2))